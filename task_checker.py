from dnacentersdk import DNACenterAPI
from pprint import pprint

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


task = "d6c41e57-def5-49af-a9fd-cee91e9e4994"

response = dnac.task.get_task_by_id(task)
print(response)