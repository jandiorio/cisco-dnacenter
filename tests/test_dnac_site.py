#!/usr/bin/env python

import sys
from dnac import dnac_api as api

dnac_details = {
  "host": "dna-3-dnac.campus.wwtatc.local",
  "username": "wwt",
  "password": "WWTwwt1!",
  "verify": False
}


def test_create_site_success():

    d = api.dnaCenterAPI(**dnac_details)

    site = {
        "type": "area",
        "site": {
            "area": {
                "name": "test_site",
                "parentName": "Global"
            }
        }
    }

    results = d.create_site(site)
    print(results.json())
    assert results.status_code == 200


# def test_create_site_success():

#     d = api.dnaCenterAPI(**dnac_details)

#     site = {
#         "type": "area",
#         "site":{
#             "area":{
#                 "name": "test_site",
#                 "parentName": "Global"
#             }
#         }
#     }

#     results = d.create_site(site)
#     print(results.json())
#     assert results.status_code == 200


def test_get_site_success():
    d = api.dnaCenterAPI(**dnac_details)
    name = "Global/test_site"
    results, site = d.get_site(name=name)

    assert results.status_code == 200
    assert len(site["response"]) == 1
    assert site["response"][0]["name"] == "test_site"

    print(results.json())

def test_get_site_failure():

    d = api.dnaCenterAPI(**dnac_details)
    name = "Global/test_sit"
    results, site = d.get_site(name=name)

    assert results.status_code == 500
    assert results.json()["message"][0] == "The input site is not valid or site is not present."

    print(results.json())
