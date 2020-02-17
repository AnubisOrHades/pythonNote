import requests

def translate(word):
    try:

        url = "http://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={}".format(word)
        response = requests.post(url)
    except Exception as e:
        print("Error:{}".format(e))
    else:
        return response.json()["translateResult"][0][0]["tgt"]
        pass
    finally:
        pass
