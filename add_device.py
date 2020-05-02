from dnacentersdk import DNACenterAPI
from pprint import pprint

dev = {
  "cliTransport": "ssh",
  #"computeDevice": true,
  "enablePassword": "WWTwwt1!",
  #"extendedDiscoveryInfo": "string",
#   "httpPassword": "string",
#   "httpPort": "string",
#   "httpSecure": true,
#   "httpUserName": "string",
  "ipAddress": [
    "192.168.200.1"
  ],
#   "merakiOrgId": [
#     "string"
#   ],
  "netconfPort": "830",
  "password": "WWTwwt1!",
  "serialNumber": "abcdefg",
#   "snmpAuthPassphrase": "string",
#   "snmpAuthProtocol": "string",
#   "snmpMode": "string",
#   "snmpPrivPassphrase": "string",
#   "snmpPrivProtocol": "string",
  "snmpROCommunity": "WWTwwt1!",
  "snmpRWCommunity": "WWTwwt1!",
  "snmpRetry": 0,
  "snmpTimeout": 0,
#   "snmpUserName": "SNMP-READ",
  "snmpVersion": "v2",
  "type": "NETWORK_DEVICE",
#   "updateMgmtIPaddressList": [
#     {
#       "existMgmtIpAddress": "string",
#       "newMgmtIpAddress": "string"
#     }
#   ],
  "userName": "wwt"
}



username = "wwt"
password = "WWTwwt1!"
version = "1.3.0"
verify = False
base_url = "https://dna-3-dnac.campus.wwtatc.local:443"

dnac = DNACenterAPI(
    base_url = base_url,
    username = username,
    password = password,
    version = version,
    verify = verify,
)

header = {"__runsync": True}

result = dnac.devices.add_device(**dev, headers=header)
response = dnac.task.get_task_by_id(result["response"]["taskId"])

pprint(response)