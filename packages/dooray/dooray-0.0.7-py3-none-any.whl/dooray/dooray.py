import os
import json
import requests


class Dooray:
    def __init__(self, token, download=False):
        self._token = token

        self._headers = {'Content-Type': 'application/json',
                         'charset': 'UTF-8',
                         'Accept': '*/*',
                         'Authorization': f'dooray-api {self._token}'}

        if download is True:
            endpoint = "https://file-api.gov-dooray.com"
        else:
            endpoint = "https://api.gov-dooray.com"
        self._endpoint = endpoint

    def send_api(self, path, method, body=None, download=False, filename=None):
        endpoint = self._endpoint + path
        try:
            status_code, response = None, None
            if method == 'GET':
                response = requests.get(endpoint, headers=self._headers)
            elif method == 'POST':
                response = requests.post(endpoint, headers=self._headers, data=json.dumps(body, ensure_ascii=False, indent="\t").encode('utf-8'))
            elif method == 'PUT':
                response = requests.put(endpoint, headers=self._headers, data=json.dumps(body, ensure_ascii=False, indent="\t").encode('utf-8'))
            elif method == 'DELETE':
                response = requests.delete(endpoint, headers=self._headers)
            status_code, response_txt = response.status_code, response.text
            return status_code, response_txt
        except Exception as e:
            print(e)