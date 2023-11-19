import tempfile


def tts(word: str, *, types: int = 1):
    import requests

    url = f"https://dict.youdao.com/dictvoice?audio={word}&type={types}"

    payload = {}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
        temp_file.write(response.content)
    return temp_file.name
