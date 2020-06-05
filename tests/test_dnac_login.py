#!/usr/bin/env python

import sys
import pytest
from dnac import dnac_api as api
from requests.exceptions import HTTPError

dnac_details = {
  "host": "dna-3-dnac.campus.wwtatc.local",
  "username": "wwt",
  "password": "WWTwwt1!",
  "verify": False
}

def test_login_success():

    d = api.dnaCenterAPI(**dnac_details)

    assert d.login_status == 200
    assert "X-Auth-Token" in d.session.headers.keys()


def test_login_failure():

    dnac_details["password"] = "WRONGPASSWORD"

    with pytest.raises(HTTPError):
        d = api.dnaCenterAPI(**dnac_details)
        assert d.login_status == 401
