import json
import os

import requests


def getIdFromUrl(wordUrl: str):
    token = os.getenv("MARKJI_TOKEN")
    url = "https://www.markji.com/api/v1/files/url"

    payload = json.dumps({"url": wordUrl})
    headers = {
        'token': token,
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return json.loads(response.text)['data']['file']['id']


def upload_voice(filepath: str, markji_token: str = ""):
    if markji_token == "":
        raise Exception("【错误】MARKJI_TOKEN未提供")

    url = "https://www.markji.com/api/v1/files"

    payload = {}
    files = [
        ('file', (os.path.basename(filepath), open(filepath, 'rb'), 'audio/mpeg'))
    ]
    headers = {
        'token': markji_token.strip(),
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    if (response.status_code == 401):
        raise ValueError("【错误】MARKJI_TOKEN错误，请检查")

    id = json.loads(response.text)['data']['file']['id']
    return f"[Audio#ID/{id}#]"
