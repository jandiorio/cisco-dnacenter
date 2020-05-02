#!/usr/bin/env python

import json
import requests

class dnaCenterAPI():

    def __init__(self, host, username, password, verify=False):
        self.host = host
        self.username = username
        self.password = password
        self.verify = verify
        self.session = None
        self.login_status = None

        self.login()


    def login(self):

        """ function to login to DNA Center and return a token """

        login_url = f"https://{self.host}/dna/system/api/v1/auth/token"

        headers = {
            "Content-Type": "application/json"
        }

        session = requests.session()
        session.verify = self.verify
        session.auth = (self.username, self.password)
        session.headers = headers

        results = session.post(login_url)

        if results.status_code == 200:
            self.session = session
            self.login_status = results.status_code
            self.session.headers.update({"X-Auth-Token": results.json()["Token"]})
        elif results.status_code == 401:
            self.login_status = results.status_code


    def get_site(self, name, siteId=None, type=None):

        _url = f"https://{self.host}/dna/intent/api/v1/site"

        if name:
            self.session.params.update({"name": name})
        elif siteId:
            self.session.params.update({"siteId": siteId})
        elif type:
            self.session.params.update({"type": type})

        results = self.session.get(_url)

        site = results.json()

        return results, site


    def create_site(self, payload):

        _url = f"https://{self.host}/dna/intent/api/v1/site"
        self.session.headers.update({"__runsync": "true"})

        siteHierarchyName = f"{payload['site'][payload['type']]['parentName']}/{payload['site'][payload['type']]['name']}"
        results, site = self.get_site(siteHierarchyName)

        if results.status_code == 500:
            # 500 means site doesn't exist need to create
            results = self.session.post(_url, json=payload)

        return results


    def get_command_runner_commands(self):

        _url = f"https://{self.host}/dna/intent/api/v1/network-device-poller/cli/legit-reads"

        results = self.session.get(_url)

        return results


    def command_runner(self, devices, commands):

        _url = f"https://{self.host}/dna/intent/api/v1/network-device-poller/cli/read-request"

        payload = {
            "commands": commands,
            "deviceUuids": devices
        }

        results = self.session.post(_url, json=payload)
        task_results = self.task_checker(results.json()["response"]["taskId"])

        file = json.loads(task_results.json()["response"]["progress"])
        command_results = self.get_file(file["fileId"])
        response = {
            "file": file,
            "command_runner_results": results.json(),
            "tasks_checker_results": task_results.json(),
            "file_results": command_results.json()
        }
        return response


    def create_cli_credentials(self, payload):
        _url = f"https://{self.host}/dna/intent/api/v1/global-credential/cli"
        results = self.session.post(_url, json=payload)
        task_results = self.task_checker(results.json()["response"]["taskId"])
        return task_results


    def create_snmp_write_community(self, payload):
        _url = f"https://{self.host}/dna/intent/api/v1/global-credential/snmpv2-write-community"
        results = self.session.post(_url, json=payload)
        task_results = self.task_checker(results.json()["response"]["taskId"])
        return task_results


    def start_discovery(self, payload):
        _url = f"https://{self.host}/dna/intent/api/v1/discovery"
        result = self.session.post(_url, json=payload)
        return result


    def get_file(self, fileId):
        _url = f"https://{self.host}/dna/intent/api/v1/file/{fileId}"
        results = self.session.get(_url)
        return results


    def task_checker(self, taskId):
        _url = f"https://{self.host}/api/v1/task/{taskId}"
        results = self.session.get(_url)
        print(results.text, results.url)
        while not results.json()["response"].get("endTime"):
            results = self.session.get(_url)

        return results


    def get_devices(self):

        _url = f"https://{self.host}/dna/intent/api/v1/network-device"

        results = self.session.get(_url)

        devices = results.json()

        return devices