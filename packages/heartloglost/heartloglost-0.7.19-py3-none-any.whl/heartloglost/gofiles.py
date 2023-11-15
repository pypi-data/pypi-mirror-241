import requests
from .reqsession import reqsession, Advreqsession
from bs4 import BeautifulSoup
import json
import os
import asyncio
import math

class GoClient:
    def __init__(self, api_key = None):
        self.api_key = api_key or os.environ['gofiles_key'] or None
    def upload_video(self, file_path: str, folder_id=None):
        '''
        client = GoClient()
        client.upload_video(file_path, folder_id)
        ```json
        {
            "status": "ok",
            "data": {
                "downloadPage": "https://gofile.io/d/Z19n9a",
                "code": "Z19n9a",
                "parentFolder": "3dbc2f87-4c1e-4a81-badc-af004e61a5b4",
                "fileId": "4991e6d7-5217-46ae-af3d-c9174adae924",
                "fileName": "example.mp4",
                "md5": "10c918b1d01aea85864ee65d9e0c2305"
            }
        }
        ```
        '''
        try:
            upload_url = get_go_server()
            data = {}
            if folder_id:
                data["folderId"] = folder_id
            if self.api_key:
                data["token"] = self.api_key
            files = {'file': open(file_path, 'rb')}
            response = requests.post(upload_url, files=files, data=data)
            data_f = json.loads(response.text)
            return data_f
        except requests.exceptions.RequestException as e:
            print("Request Exception:", e)
            return f"Error {e}"

def get_go_server():
    api = "https://api.gofile.io/getServer"
    response = Advreqsession(api)
    json_data = json.loads(response.text)
    server_id = json_data["data"]["server"]
    upload_url = f"https://{server_id}.gofile.io/uploadFile"
    return upload_url
    