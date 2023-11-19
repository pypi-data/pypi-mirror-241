import json
import os
import requests


def tts(text: str, locale: str = "en-GB"):
    token = os.getenv("MARKJI_TOKEN")
    if token is None:
        raise ValueError("【错误】MARKJI_TOKEN未提供")
    url = "https://www.markji.com/api/v1/files/tts"

    payload = json.dumps({
        "content_slices": [
            {
                "text": text,
                "locale": locale
            }
        ]
    })
    headers = {
        'token': token,
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if (response.status_code == 400):
        raise ValueError("【错误】请检查输入的单词文件是否有问题")
    if (response.status_code == 401):
        raise ValueError("【错误】MARKJI_TOKEN错误，请检查")
    return json.loads(response.text)['data']['url']
