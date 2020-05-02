#!/usr/bin/env python

# dnac_login.py
# learning dna center without the SDK

import sys
import requests


def login(host, username, password, verify=False):

    """ function to login to DNA Center and return a token """

    login_url = f"https://{host}/dna/system/api/v1/auth/token"

    headers = {
        "Content-Type": "application/json"
    }

    session = requests.session()
    session.verify = verify
    session.auth = (username, password)
    session.headers = headers

    results = session.post(login_url)

    return results
