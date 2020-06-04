import os

from PIL import Image
from aip import AipOcr


def img_shape(path):
    """
    获取图片形状（宽高）
    :param path: 文件路径
    :return: 图片形状（width：宽，height：高）
    """
    img = Image.open(path)
    shape = img.size
    return {"width": shape[0], "height": shape[1]}


def cut(path_in, path_out, box):
    """
    剪切图片并保存
    :param path_in: 图片路径
    :param path_out: 剪切后保存路径
    :param box: 剪切范围 元组类型 (left, upper, right, lower)
    :return:
    """
    try:
        img = Image.open(path_in)
        cropped = img.crop(box)  # (left, upper, right, lower)
        cropped.save(path_out)
    except Exception as e:
        print("Error:{}".format(e))
    else:
        pass
    finally:
        pass


def get_txt_img(path):
    """ 这里输入你创建应用获得的三个参数"""
    APP_ID = '15803909'
    API_KEY = 'd8voMcnrHZ6vadX578TvhRfd'
    SECRET_KEY = 'FjLk1qojipmN5Pcfuj3Wo2SAzX9lURKX'

    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    if os.path.exists(path):
        image = open(path, 'rb')
    else:
        print("Error:{}不存在".format(path))
        return None
    try:
        data = client.basicAccurate(image.read()).get("words_result")
        result = "\n".join([d["words"] for d in data])
    except Exception as e:
        print("Error:{}".format(e))
    else:
        return result
    finally:
        image.close()
        pass
