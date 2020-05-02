import settings
from dnacentersdk import api
from pprint import pprint
from dotenv import load_dotenv
import os

# There is an anomaly with how the SDK ingests environment variables.  It is done at the time of import of the sdk only.
# This means the credentials must already be defined in the environment and precludes the use of dotenv or similar
# techniques to programmatically configure the environment.
#
username = "wwt"
password = "WWTwwt1!"
version = "1.3.0"
verify = False
base_url = "https://dna-3-dnac.campus.wwtatc.local:443"

dnac = api.DNACenterAPI(
    username = username,
    password = password,
    version = version,
    base_url = base_url,
    verify = verify,
)

# Create a sample site - note the use of additional header __runsync
# central = {
#     "type": "area",
#     "site": {
#         "area": {
#             "name": "Central",
#             "parentName": "Global"
#         }
#     }
# }
headers = {"__runsync": True}
# results = dnac.sites.create_site(
#     payload=central,
#     headers=headers
# )

# print(results)

sites = dnac.sites.get_site()
pprint(sites)

# Delete Site
# central_id = [site["id"] for site in sites["response"] if site["name"]=="Central"]
# if len(central_id) > 0:
#     central_id = central_id[0]

# print(f"Attempting to delete site Central")
# if isinstance(central_id, str):
#     result = dnac.sites.delete_site(central_id)
#     print(result)
# else:
#     print(f"str object expected. you provided {type(central_id)} ")
