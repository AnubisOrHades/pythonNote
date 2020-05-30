from PIL import Image


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
        print(img.size)
        cropped = img.crop(box)  # (left, upper, right, lower)
        cropped.save(path_out)
    except Exception as e:
        print("Error:{}".format(e))
    else:
        pass
    finally:
        pass
