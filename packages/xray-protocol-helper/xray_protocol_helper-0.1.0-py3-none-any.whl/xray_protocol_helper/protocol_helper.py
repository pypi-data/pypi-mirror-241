import dataclasses
from abc import ABC, abstractmethod
from typing import Optional
from urllib.parse import urlparse, parse_qs

from xray_protocol_helper.base64_helper import Base64Helper
from xray_protocol_helper.xray_json_creator.xray_config_util import XrayConfigUtil


@dataclasses.dataclass
class XrayDecodeData:
    uri: str
    protocol: str
    address: str
    port: int
    sni: str = None
    host: str = None


class AbstractXrayProtocol(ABC):
    REPLACE_DATA_LIST = ("\'", "\"", "`", "*")

    def __init__(self, uri: str):
        self.uri = uri

    @property
    def pars_result(self):
        return urlparse(self.uri)

    @property
    def dict_uri(self) -> dict:
        return Base64Helper.decode_dict_base64(encoded_dict_data=self.pars_result.hostname)

    @classmethod
    def clean_uri_string(cls, uri):
        uri = uri.strip()
        for replace_char in cls.REPLACE_DATA_LIST:
            uri = uri.replace(replace_char, "")
        uri = uri.split("#")[0]
        return uri

    def get_data(self) -> Optional[XrayDecodeData]:
        self._clean_uri()
        self.validate_uri()
        return self._get_data()

    @abstractmethod
    def _get_data(self) -> Optional[XrayDecodeData]:
        pass

    def _clean_uri(self):
        self.uri = self.clean_uri_string(uri=self.uri)

    def validate_uri(self):
        result = XrayConfigUtil().get_xray_config(uri=self.uri, port=1080)
        if not result.status:
            raise ValueError("uri is not valid")


class VmessProtocol(AbstractXrayProtocol):
    def _get_data(self) -> Optional[XrayDecodeData]:
        dict_url = self.dict_uri
        if not dict_url:
            return
        address = dict_url.get("add")
        port = dict_url.get("port")
        sni = dict_url.get("sni")
        sni = None if sni == "" else sni
        host = dict_url.get("host")
        host = None if host == "" else host
        return XrayDecodeData(uri=self.uri, protocol="vmess", address=address, port=port, sni=sni, host=host)

    def _clean_uri(self):
        super()._clean_uri()
        dict_uri = self.dict_uri
        if not dict_uri:
            return
        dict_uri["ps"] = ""
        self.uri = f"vmess://{Base64Helper.encode_dict_base64(dict_data=dict_uri)}"


class VlessProtocol(AbstractXrayProtocol):
    PROTOCOL = "vless"

    def _get_data(self) -> Optional[XrayDecodeData]:
        return self.get_vless_data()

    def get_vless_data(self) -> Optional[XrayDecodeData]:
        pars_result = self.pars_result
        address = pars_result.hostname
        port = pars_result.port
        pars_query = parse_qs(pars_result.query)
        try:
            host = pars_query["host"][0]
            host = None if host == "" else host
        except KeyError:
            host = None
        try:
            sni = pars_query["sni"][0]
            sni = None if sni == "" else sni
        except KeyError:
            sni = None
        return XrayDecodeData(uri=self.uri, protocol=self.PROTOCOL, address=address, port=port, sni=sni, host=host)


class ShadowSocksProtocol(VlessProtocol):
    PROTOCOL = "ss"

    def _get_data(self) -> Optional[XrayDecodeData]:
        pars_result = self.pars_result
        if "@" in pars_result.netloc:
            return self.get_vless_data()
        # self.decode_data = Base64Helper.decode_base64(self.data)
        # if not self.decode_data:
        #     return
        # split_data = self.decode_data.split(":")
        # if len(split_data) < 3:
        #     return
        # self.address = split_data[1].split("@")[1]
        # self.port = split_data[2]


class TrojanProtocol(VlessProtocol):
    PROTOCOL = "trojan"

    def _get_data(self) -> Optional[XrayDecodeData]:
        return self.get_vless_data()


class ProtocolHelper:
    PROTOCOL_CLASS = {
        "vmess": VmessProtocol,
        "vless": VlessProtocol,
        "ss": ShadowSocksProtocol,
        "trojan": TrojanProtocol,
    }

    def __init__(self, uri: str):
        self.uri = uri

    def get_protocol_object(self, protocol) -> AbstractXrayProtocol:
        protocol_class = self.PROTOCOL_CLASS.get(protocol)
        if protocol_class is None:
            raise ValueError("not found protocol")
        return protocol_class(uri=self.uri)

    def get_data(self) -> Optional[XrayDecodeData]:
        self.uri = AbstractXrayProtocol.clean_uri_string(uri=self.uri)
        protocol = urlparse(self.uri).scheme
        protocol_obj = self.get_protocol_object(protocol=protocol)
        return protocol_obj.get_data()
