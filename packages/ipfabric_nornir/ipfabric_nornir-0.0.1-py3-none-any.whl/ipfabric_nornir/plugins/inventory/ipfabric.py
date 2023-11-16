"""ipfabric_nornir.inventory.ipfabric"""
import logging
from typing import Any, Dict, Optional, Type, Union

from ipfabric import IPFClient
from nornir.core.inventory import Defaults, Groups, Host, HostOrGroup, Inventory

logger = logging.getLogger(__name__)


def _get_inventory_element(typ: Type[HostOrGroup], device: Dict[str, Any], defaults: Defaults) -> HostOrGroup:
    # map IPF family to netmiko platform names / netmiko device_type
    # list of IP Fabric supported device families https://docs.ipfabric.io/matrix/
    # list of netmiko supported device_types https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py
    netmiko_platform_map = {
        "asa": "cisco_asa",
        "ios": "cisco_ios",
        "ios-xe": "cisco_xe",
        "ios-xr": "cisco_xr",
        "nx-os": "cisco_nxos",
        "pa-os": "paloalto_panos",
        "wlc-air": "cisco_wlc",
        "junos": "juniper_junos",
        "aos": "alcatel_aos",
        "eos": "arista_eos",
        "fastiron": "brocade_fastiron",
        "gaia": "checkpoint_gaia",
        "gaia-embedded": "checkpoint_gaia",
        "ftd": "cisco_ftd",
        "viptela": "cisco_viptela",
        "os10": "dell_os10",
        "powerconnect": "dell_powerconnect",
        "ftos": "dell_force10",
        "exos": "extreme_exos",
        "prisma": "cloudgenix_ion",
        "fortigate": "fortinet",
        "comware": "hp_comware",
        "vrp": "huawei_vrp",
        "routeros": "mikrotik_routeros",
        "enterasys": "enterasys",
        # "timos"
        # aruba
        # "big-ip: "f5_ltm",
        # extreme boss, voss
    }
    # napalm platform mapping https://napalm.readthedocs.io/en/latest/support/
    # napalm_platform_map = {
    #     "nx-os": "nxos_ssh",
    #     "ios": "ios",
    #     "ios-xe": "ios",
    #     "ios-rx": "iosxr",
    #     "eos": "eos",
    #     "junos": "junos",
    # }
    # # genie platform mapping https://github.com/CiscoTestAutomation/unicon.plugins/tree/master/src/unicon/plugins
    # genie_platform_map = {
    #     "nx-os": "nxos",
    #     "ios": "ios",
    #     "ios-xe": "iosxe",
    #     "ios-rx": "iosxr",
    #     "asa": "asa",
    #     "apic": "apic",
    #     "comware": "comware",
    #     "viptela": "viptela",
    #     "junos": "junos",
    #     "eos": "eos",
    # }
    data = {
        "address": (device.get("loginIp"),),
        "family": device.get("family") or device.get("vendor"),
        "hostname": device.get("hostname"),
        "ipf_platform": device.get("platform"),
        "protocol": device.get("loginType"),
        "serial": device.get("sn"),
        "siteName": device.get("siteName"),
        "vendor": device.get("vendor"),
        "version": device.get("version"),
    }

    return typ(
        name=device.get("hostname"),
        hostname=device.get("loginIp"),
        port=22 if device.get("loginType") == "ssh" else 23,
        # set netmiko platform, use family or vendor if no match
        platform=netmiko_platform_map.get(device["family"], device.get("platform", device.get("vendor", ""))),
        # set credentials from defaults
        username=defaults.username if defaults.username else None,
        password=defaults.password if defaults.password else None,
        groups=[],
        data=data,
        connection_options={},
        defaults=defaults,
    )


class IPFabricInventory(Inventory):
    """
    class IPFabricInventory(Inventory):
    """

    def __init__(
        self,
        base_url: Optional[str] = None,
        api_version: Optional[str] = None,
        token: Optional[str] = None,
        snapshot_id: str = "$last",
        username: Optional[str] = None,
        password: Optional[str] = None,
        verify: Union[bool, str] = True,
        default: Optional[dict] = None,
        defaults_data: Optional[dict] = None,
        defaults_connection_options: Optional[dict] = None,
        **ipfabric_kwargs,
    ) -> None:
        """
        IP Fabric plugin
        API docs https://docs.ipfabric.io/api/
        """

        self.ipf = IPFClient(
            base_url=base_url,
            api_version=api_version,
            auth=(username, password) if username and password else token,
            snapshot_id=snapshot_id,
            verify=verify,
            **ipfabric_kwargs,
        )
        self.default = default or {}
        self.defaults_data = defaults_data
        self.defaults_connection_options = defaults_connection_options

    def load(self) -> Inventory:
        """
        Load inventory
        """
        ipf_devices = self.ipf.inventory.devices.all(
            columns=[
                "loginIp",
                "family",
                "hostname",
                "platform",
                "loginType",
                "sn",
                "siteName",
                "vendor",
                "version",
            ]
        )

        groups = Groups()

        username = self.default.get("username", None)
        password = self.default.get("password", None)
        defaults = Defaults(username=username, password=password)

        serialized_hosts = {}
        for device in ipf_devices:
            serialized_hosts[device.get("loginIp")] = _get_inventory_element(Host, device, defaults)

        return Inventory(hosts=serialized_hosts, groups=groups, defaults=defaults)
