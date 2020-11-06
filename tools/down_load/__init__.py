import requests
from fake_useragent import UserAgent

headers = {
    'User-Agent': UserAgent().chrome
}


def ordinary_down_load(url, file_path):
    try:
        response = requests.get(url, heders=headers)
        if response.status_code == 200:
            with open(file_path, "wb") as f:
                f.write(response.content)
        else:
            return 0
    except Exception as e:
        print("Error:{}".format(e))
        return 0
    else:
        return 1
        pass
    finally:
        pass
