#!/usr/bin/env python

import sys
import json
import yaml
from getpass import getpass
from dnac import dnac_api as api
from pprint import pprint

dnac_details = {
  "host": "dna-3-dnac.campus.wwtatc.local",
  "username": "wwt",
  "password": "WWTwwt1!",
  "verify": False
}

d = api.dnaCenterAPI(**dnac_details)

# devices = ["4da90012-3b23-4e98-86b2-237c347684aa"]
# commands = ["show ip route", "sh ip arp"]

# output = d.command_runner(devices, commands)

# pprint(output["file_results"])

# for device in output["file_results"]:
#     for cmd in commands:
#         for line in (device["commandResponses"]["SUCCESS"][cmd].split('\n')):
#             print(line)

# ================================================
# SITES
# with open("vars/sites.yml", "r") as file:
#     stream = file.read()
#     sites = yaml.safe_load(stream)

# pprint(sites)

# for site in sites:

#     result = d.create_site(site)
#     print(result.json())
# ================================================

# ================================================
# CLI Credentials
# with open("vars/cli_credentials.yml", "r") as file:
#     stream = file.read()
#     credentials = yaml.safe_load(stream)

# result = d.create_cli_credentials(credentials)
# print(result, result.text, result.json())
# ================================================

# ================================================
# SNMP Credentials
# with open("vars/snmp_write.yml", "r") as file:
#     stream = file.read()
#     credentials = yaml.safe_load(stream)

# result = d.create_snmp_write_community(credentials)
# print(result, result.text, result.json())
# ================================================

# ================================================
# Start Discovery
with open("vars/new_cred_discovery.json", "r") as file:
    stream = file.read()
    discovery = json.loads(stream)

result = d.start_discovery(discovery)
print(result, result.text, result.json())
# ================================================