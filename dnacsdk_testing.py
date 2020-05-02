from dnacentersdk import DNACenterAPI
from dotenv import load_dotenv
from tabulate import tabulate
from pprint import pprint
from operator import itemgetter

dnac = DNACenterAPI(
    base_url="https://sandboxdnac2.cisco.com:443",
    version="1.3.0",
    username="devnetuser",
    password="Cisco123!",
    verify=False
)

# Retrieve all Sites
# sites = dnac.sites.get_site()

# site_header = ["Name","Site Hierarchy"]

# site_data =[[site['name'],site['siteNameHierarchy']] for site in sites.response]

# for site in sites.response:
#     site_data.append([site['name'],site['siteNameHierarchy']])

# print(
#     tabulate(
#         sorted(
#             site_data, key=itemgetter(0)
#             ),
#         headers=site_header, tablefmt="fancy_grid"))

# print(
#     f"There are {dnac.sites.get_site_count().response} sites in your DNACENTER..."
# )

# Get Client Detail
# clients = dnac.clients.get_client_detail("00:00:2A:01:00:47")
# print(clients["detail"])

# Get Device List
# Retrieve all devices in the "Swithces and Hubs" family
try:
    devices = dnac.devices.get_device_list(family="Switches and Hubs")
    for device in devices.response:
        print(f"{device.hostname:20s}{device.upTime}")
except ApiError as e:
    print(e)

pprint(devices)