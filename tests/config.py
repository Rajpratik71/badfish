import os

MOCK_HOST = "f01-h01-000-r630.host.io"
MOCK_USER = "mock_user"
MOCK_PASS = "mock_pass"
JOB_ID = "JID_498218641680"
BAD_DEVICE_NAME = "BadIF.Slot.x-y-z"
DEVICE_NIC_I = "NIC.Integrated.1"
DEVICE_NIC_S = "NIC.Slot.1"
MAC_ADDRESS = "40:A6:B7:0C:01:A0"


def render_device_dict(index, device):
    device_dict = {
        "Index": index,
        "Enabled": "True",
        "Id": "BIOS.Setup.1-1#BootSeq#{name}#{hash}".format(**device),
        "Name": device["name"],
    }
    return device_dict


DEVICE_HDD_1 = {
    "name": "HardDisk.List.1-1",
    "hash": "c9203080df84781e2ca3d512883dee6f"
}
DEVICE_NIC_1 = {
    "name": "NIC.Integrated.1-2-1",
    "hash": "bfa8fe2210d216298c7c53aedfc7e21b",
}
DEVICE_NIC_2 = {
    "name": "NIC.Slot.2-1-1",
    "hash": "135ac45c488549c04a21f1c199c2044a"
}

BOOT_SEQ_RESPONSE_DIRECTOR = [
    render_device_dict(0, DEVICE_NIC_1),
    render_device_dict(1, DEVICE_HDD_1),
    render_device_dict(2, DEVICE_NIC_2),
]
BOOT_SEQ_RESPONSE_FOREMAN = [
    render_device_dict(0, DEVICE_NIC_2),
    render_device_dict(1, DEVICE_HDD_1),
    render_device_dict(2, DEVICE_NIC_1),
]
BOOT_SEQ_RESPONSE_NO_MATCH = [
    render_device_dict(0, DEVICE_HDD_1),
    render_device_dict(1, DEVICE_NIC_1),
    render_device_dict(2, DEVICE_NIC_2),
]

RESPONSE_WITHOUT = (
    "- INFO     - Current boot order:\n"
    "- INFO     - 1: NIC.Integrated.1-2-1\n"
    "- INFO     - 2: HardDisk.List.1-1\n"
    "- INFO     - 3: NIC.Slot.2-1-1\n"
)
RESPONSE_NO_MATCH = (
    "- INFO     - Current boot order:\n"
    "- INFO     - 1: HardDisk.List.1-1\n"
    "- INFO     - 2: NIC.Integrated.1-2-1\n"
    "- INFO     - 3: NIC.Slot.2-1-1\n"
)
WARN_NO_MATCH = (
        "- WARNING  - Current boot order does not match any of the given.\n%s"
        % RESPONSE_NO_MATCH
)
RESPONSE_DIRECTOR = "- WARNING  - Current boot order is set to: director.\n"

RESPONSE_FOREMAN = "- WARNING  - Current boot order is set to: foreman.\n"
INTERFACES_PATH = os.path.join(
    os.path.dirname(__file__), "../config/idrac_interfaces.yml"
)

# test_boot_to constants
ERROR_DEV_NO_MATCH = (
        "- ERROR    - Device %s does not match any of the available boot devices for host %s\n"
        "- ERROR    - There was something wrong executing Badfish\n"
        % (BAD_DEVICE_NAME, MOCK_HOST)
)
RESPONSE_BOOT_TO = (
    f"- WARNING  - Job queue already cleared for iDRAC {MOCK_HOST}, DELETE command will not execute.\n"
    "- INFO     - Command passed to set BIOS attribute pending values.\n"
    "- INFO     - POST command passed to create target config job.\n"
)
RESPONSE_BOOT_TO_BAD_TYPE = (
    "- ERROR    - Expected values for -t argument are: ['director', 'foreman']\n"
    "- ERROR    - There was something wrong executing Badfish\n"
)
RESPONSE_BOOT_TO_BAD_FILE = (
    "- ERROR    - No such file or directory: bad/bad/file.\n"
    "- ERROR    - There was something wrong executing Badfish\n"
)
RESPONSE_BOOT_TO_BAD_MAC = (
    "- ERROR    - MAC Address does not match any of the existing\n"
    "- ERROR    - There was something wrong executing Badfish\n"
)

# test_reboot_only
RESPONSE_REBOOT_ONLY_SUCCESS = (
    "- INFO     - Command passed to GracefulRestart server, code return is 204.\n"
    "- INFO     - Polling for host state: Off\n"
    "- INFO     - Polling for host state: Not Down\n"
    "- INFO     - Command passed to On server, code return is 204.\n"
)

# test_reset_%s
RESPONSE_RESET = (
    "- INFO     - Status code 204 returned for POST command to reset %s.\n"
    "- INFO     - %s will now reset and be back online within a few minutes.\n"
)

# test_change_boot
RESPONSE_CHANGE_BOOT = (
    f"- WARNING  - Job queue already cleared for iDRAC {MOCK_HOST}, DELETE command will not "
    "execute.\n"
    "- INFO     - PATCH command passed to update boot order.\n"
    "- INFO     - POST command passed to create target config job.\n"
    "- INFO     - Command passed to ForceOff server, code return is 200.\n"
    "- INFO     - Polling for host state: Not Down\n"
    "- INFO     - Command passed to On server, code return is 200.\n"
)
RESPONSE_CHANGE_BAD_TYPE = (
    "- ERROR    - Expected values for -t argument are: ['director', 'foreman']\n"
    "- ERROR    - There was something wrong executing Badfish\n"
)
RESPONSE_CHANGE_TO_SAME = "- WARNING  - No changes were made since the boot order already matches the requested.\n"
RESPONSE_CHANGE_NO_INT = (
    "- ERROR    - You must provide a path to the interfaces yaml via `-i` optional argument.\n"
    "- ERROR    - There was something wrong executing Badfish\n"
)

ROOT_RESP = '{"Managers":{"@odata.id":"/redfish/v1/Managers"},"Systems":{"@odata.id":"/redfish/v1/Systems"}}'
SYS_RESP = '{"Members":[{"@odata.id":"/redfish/v1/Systems/System.Embedded.1"}]}'
MAN_RESP = '{"Members":[{"@odata.id":"/redfish/v1/Managers/iDRAC.Embedded.1"}]}'
RESET_TYPE_RESP = (
    '{"Actions":{"#Manager.Reset":{"ResetType@Redfish.AllowableValues":["GracefulRestart"],'
    '"target":"/redfish/v1/Managers/iDRAC.Embedded.1/Actions/Manager.Reset"}}} '
)
INIT_RESP = [ROOT_RESP, SYS_RESP, ROOT_RESP, MAN_RESP]

STATE_OFF_RESP = '{"PowerState": "Off"}'
STATE_ON_RESP = '{"PowerState": "On"}'

BOOT_MODE_RESP = '{"Attributes": {"BootMode": "Bios"}}'
BOOT_SEQ_RESP = '{"Attributes": {"BootSeq": %s}}'

ETHERNET_INTERFACES_RESP = (
    '{"Members":['
    '{"@odata.id":"/redfish/v1/Systems/System.Embedded.1/EthernetInterfaces/NIC.Slot.1-1-1"},'
    '{"@odata.id":"/redfish/v1/Systems/System.Embedded.1/EthernetInterfaces/NIC.Integrated.1-1-1"}'
    ']}'
)


NETWORK_ADAPTERS_RESP = (
    '{"Members": ['
    f'{{"@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/{DEVICE_NIC_I}"}},'
    f'{{"@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/{DEVICE_NIC_S}"}}'
    ']}'
)
NETWORK_PORTS_ROOT_RESP = (
    '{"Members": ['
    '{"@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/%s/NetworkPorts/%s-1"} '
    ']}'
)
NETWORK_DEV_FUNC_RESP = (
    '{"Members": ['
    '{"@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/%s/NetworkDeviceFunctions/%s-1"}'
    ']}'
)
NETWORK_DEV_FUNC_DET_RESP = (
    '{"Ethernet": {"MACAddress": "B0:26:28:D8:68:C0"},'
    '"Oem": {"Dell": {"DellNIC": {"VendorName": "Intel"}}}}'
)
NETWORK_PORTS_RESP = (
    '{"Id": "%s-1", "LinkStatus": "Down", "SupportedLinkCapabilities": [{"LinkSpeedMbps": 1000}]}'
)
RESPONSE_LS_INTERFACES = (
    "- INFO     - NIC.Integrated.1-1:\n"
    "- INFO     -     Id: NIC.Integrated.1-1\n"
    "- INFO     -     LinkStatus: Down\n"
    "- INFO     -     LinkSpeedMbps: 1000\n"
    "- INFO     -     MACAddress: B0:26:28:D8:68:C0\n"
    "- INFO     -     Vendor: Intel\n"
    "- INFO     - NIC.Slot.1-1:\n"
    "- INFO     -     Id: NIC.Slot.1-1\n"
    "- INFO     -     LinkStatus: Down\n"
    "- INFO     -     LinkSpeedMbps: 1000\n"
    "- INFO     -     MACAddress: B0:26:28:D8:68:C0\n"
    "- INFO     -     Vendor: Intel\n"
)

INTERFACES_RESP = (
    f'{{"Id":"NIC.Integrated.1-2-1","MACAddress":"{MAC_ADDRESS}"}}'
)

RESPONSE_LS_JOBS = (
    "- INFO     - Found active jobs:\n"
    f"- INFO     - {JOB_ID}\n"
)
RESPONSE_CLEAR_JOBS = (
    f"- INFO     - Job queue for iDRAC {MOCK_HOST} successfully cleared.\n"
)

BLANK_RESP = '"OK"'
TASK_OK_RESP = '{"Message": "Task successfully scheduled."}'
JOB_OK_RESP = '{"JobID": "%s"}' % JOB_ID

