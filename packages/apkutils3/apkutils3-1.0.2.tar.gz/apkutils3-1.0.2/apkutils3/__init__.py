# coding: utf-8
import binascii
from pathlib import Path
import re
from typing import Dict, List, Optional, Set, Union, TYPE_CHECKING
import xml
import zipfile
import xmltodict
from zipfile import ZipFile

from .consts import MANIFEST_XMLTODICT_FORCE_LIST, RESOURCE_XMLTODICT_FORCE_LIST
from .axml.arscparser import ARSCParser
from .axml.axmlparser import AXML

if TYPE_CHECKING:
    from .cert import CertType
from .custom_typing import ChildItem, OpCodeItem
from .dex.dexparser import DexFile
from .manifest import Manifest
from cigam import Magic

__version__ = "1.0.2"


class APK:
    def __init__(self, apk_path: Union[str, Path]):
        self.apk_path: str = str(apk_path)
        self.dex_files: List[DexFile] = []
        self.children: List[ChildItem] = []
        self.org_manifest: str = ""
        self.strings: List[str] = []
        self.org_strings: List[str] = []
        self.opcodes: List[OpCodeItem] = []
        self.certs: List[CertType] = []
        self.arsc: ARSCParser
        self.strings_refx: Optional[Dict[str, Dict[str, Set[bytes]]]] = None
        self.app_icon: Optional[str] = None
        self.app_icons: Set[str] = set()
        self._manifest: dict = {}

    def get_all_app_icons(self) -> Set[str]:
        """
        获取应用图标对应的所有图标文件的路径
        """
        if self.app_icons:
            return self.app_icons
        self._init_app_icon()
        return self.app_icons

    def get_app_icon(self) -> Optional[str]:
        """
        获取应用图标对应的所有图标文件中的一个的路径
        """
        if self.app_icon:
            return self.app_icon
        self._init_app_icon()
        return self.app_icon

    def _init_app_icon(self) -> None:
        files = self.get_files()
        result = re.search(r':icon="@(.*?)"', self.get_org_manifest())
        if not result:
            return
        ids = "0x" + result.groups()[0].lower()
        try:
            with ZipFile(self.apk_path, "r") as z:
                data = z.read("resources.arsc")
                self.arscobj = ARSCParser(data)
                self.package = self.arscobj.get_packages_names()[0]
                datas = xmltodict.parse(
                    self.arscobj.get_public_resources(self.package),
                    force_list=RESOURCE_XMLTODICT_FORCE_LIST,
                )
                for item in datas["resources"]["public"]:
                    if ids != item["@id"]:
                        continue
                    for f in files:
                        name = f["name"]
                        if item["@type"] in name and item["@name"] in name:
                            self.app_icon = name
                            self.app_icons.add(name)
        except Exception as ex:
            raise ex

    def _init_strings_refx(self) -> None:
        if not self.dex_files:
            self._init_dex_files()

        self.strings_refx = {}
        for dex_file in self.dex_files:
            for dexClass in dex_file.classes:
                try:
                    dexClass.parseData()
                except IndexError:
                    continue
                assert dexClass.data is not None
                for method in dexClass.data.methods:
                    if not method.code:
                        continue

                    for bc in method.code.bytecode:
                        # 1A const-string
                        # 1B const-string-jumbo
                        if bc.opcode not in {26, 27}:
                            continue

                        clsname = method.id.cname.decode()
                        mtdname = method.id.name.decode()
                        dexstr = dex_file.string(bc.args[1])
                        if clsname in self.strings_refx:
                            if mtdname in self.strings_refx[clsname]:
                                self.strings_refx[clsname][mtdname].add(dexstr)
                            else:
                                self.strings_refx[clsname][mtdname] = set()
                                self.strings_refx[clsname][mtdname].add(dexstr)
                        else:
                            self.strings_refx[clsname] = {}
                            self.strings_refx[clsname][mtdname] = set()
                            self.strings_refx[clsname][mtdname].add(dexstr)

    def get_strings_refx(self) -> Dict[str, Dict[str, Set[bytes]]]:
        """获取字符串索引，即字符串被那些类、方法使用了。

        :return: 字符串索引
        :rtype: [dict]
        """
        if self.strings_refx is None:
            self._init_strings_refx()
        assert self.strings_refx is not None
        return self.strings_refx

    def get_dex_files(self) -> List[DexFile]:
        if not self.dex_files:
            self._init_dex_files()
        return self.dex_files

    def _init_dex_files(self) -> None:
        self.dex_files = []
        try:
            with ZipFile(self.apk_path, "r") as z:
                for name in z.namelist():
                    data = z.read(name)
                    if (
                        name.startswith("classes")
                        and name.endswith(".dex")
                        and Magic(data).get_type() == "dex"
                    ):
                        dex_file = DexFile(data)
                        self.dex_files.append(dex_file)
        except Exception as ex:
            raise ex

    def get_strings(self) -> List[str]:
        if not self.strings:
            self._init_strings()
        return self.strings

    def get_org_strings(self) -> List[str]:
        if not self.org_strings:
            self._init_strings()
        return self.org_strings

    def _init_strings(self) -> None:
        if not self.dex_files:
            self._init_dex_files()

        str_set = set()
        org_str_set = set()
        for dex_file in self.dex_files:
            for i in range(dex_file.string_ids.size):
                ostr = dex_file.string(i)
                org_str_set.add(ostr)
                str_set.add(binascii.hexlify(ostr).decode())

        self.strings = list(str_set)
        self.org_strings = list(org_str_set)

    def get_files(self) -> List[ChildItem]:
        if not self.children:
            self._init_children()
        return self.children

    def _init_children(self) -> None:
        self.children = []
        try:
            with ZipFile(self.apk_path, mode="r") as zf:
                for name in zf.namelist():
                    try:
                        data = zf.read(name)
                        mine = Magic(data).get_type()
                        info = zf.getinfo(name)
                    except Exception as ex:
                        print(name, ex)
                        continue
                    crc = str(hex(info.CRC)).upper()[2:]
                    crc = "0" * (8 - len(crc)) + crc
                    # item["sha1"] = ""
                    item: ChildItem = {
                        "name": name,
                        "type": mine,
                        "time": "%d%02d%02d%02d%02d%02d" % info.date_time,
                        "crc": crc,
                    }
                    self.children.append(item)
        except Exception as e:
            raise e

    def get_org_manifest(self) -> str:
        if not self.org_manifest:
            self._init_manifest()
        return self.org_manifest

    @property
    def resources(self) -> ARSCParser:
        with zipfile.ZipFile(self.apk_path, mode="r") as zf:
            data = zf.read("resources.arsc")
            return ARSCParser(data)

    def _init_org_manifest(self) -> None:
        ANDROID_MANIFEST = "AndroidManifest.xml"
        try:
            with ZipFile(self.apk_path, mode="r") as zf:
                if ANDROID_MANIFEST in zf.namelist():
                    data = zf.read(ANDROID_MANIFEST)
                    try:
                        axml = AXML(data)
                        if axml.is_valid:
                            self.org_manifest = axml.get_xml()
                    except Exception as e:
                        raise e
        except Exception as e:
            raise e

    def get_manifest(self) -> dict:
        if not self._manifest:
            self._init_manifest()
        return self._manifest

    @property
    def manifest(self) -> Manifest:
        return Manifest(self.get_org_manifest())

    def _init_manifest(self) -> None:
        if not self.org_manifest:
            self._init_org_manifest()

        if self.org_manifest:
            try:
                self._manifest = xmltodict.parse(
                    self.org_manifest, force_list=MANIFEST_XMLTODICT_FORCE_LIST
                )["manifest"]
            except xml.parsers.expat.ExpatError as e:
                pass
            except Exception as e:
                raise e

    def _init_arsc(self) -> None:
        ARSC_NAME = "resources.arsc"
        try:
            with ZipFile(self.apk_path, mode="r") as zf:
                if ARSC_NAME in zf.namelist():
                    data = zf.read(ARSC_NAME)
                    self.arsc = ARSCParser(data)
        except Exception as e:
            raise e

    def get_arsc(self) -> ARSCParser:
        if not hasattr(self, "arsc"):
            self._init_arsc()

        return self.arsc

    def get_certs(self) -> List["CertType"]:
        if not self.certs:
            self._init_certs()
        return self.certs

    def _init_certs(self) -> None:
        try:
            with ZipFile(self.apk_path, mode="r") as zf:
                for name in zf.namelist():
                    if "META-INF" in name:
                        data = zf.read(name)
                        mine = Magic(data).get_type()
                        if mine != "txt":
                            from cert import Certificate

                            cert = Certificate(data)
                            self.certs = cert.get()
        except Exception as e:
            raise e

    def get_opcodes(self) -> List[OpCodeItem]:
        if not self.dex_files:
            self._init_opcodes()
        return self.opcodes

    def _init_opcodes(self) -> None:
        if not self.dex_files:
            self._init_dex_files()

        self.opcodes = []
        for dex_file in self.dex_files:
            for dexClass in dex_file.classes:
                try:
                    dexClass.parseData()
                except IndexError:
                    continue
                assert dexClass.data is not None
                for method in dexClass.data.methods:
                    opcodes = ""
                    if method.code:
                        for bc in method.code.bytecode:
                            opcode = str(hex(bc.opcode)).upper()[2:]
                            if len(opcode) == 2:
                                opcodes = opcodes + opcode
                            else:
                                opcodes = opcodes + "0" + opcode

                    proto = self.get_proto_string(
                        method.id.return_type, method.id.param_types
                    )
                    assert dexClass.super is not None
                    item: OpCodeItem = {
                        "super_class": dexClass.super.decode(),
                        "class_name": method.id.cname.decode(),
                        "method_name": method.id.name.decode(),
                        "method_desc": method.id.desc.decode(),
                        "proto": proto,
                        "opcodes": opcodes,
                    }
                    self.opcodes.append(item)

    @staticmethod
    def get_proto_string(return_type: bytes, param_types: List[bytes]) -> str:
        proto = return_type.decode()
        if len(proto) > 1:
            proto = "L"

        for item in param_types:
            param_type = item.decode()
            proto += "L" if len(param_type) > 1 else param_type

        return proto
