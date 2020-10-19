import requests
import hashlib


def get_str_md5(string):
    """
    获取字符串哈希值
    :param string: 字符串
    :return: 字符串哈希值
    """
    try:
        md5_obj = hashlib.md5()
        md5_obj.update(string.encode("utf8"))
        pass
    except Exception as e:
        print("Error:{}".format(e))
    else:
        return md5_obj.hexdigest()
        pass
    finally:
        pass


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


if __name__ == '__main__':
    pass
