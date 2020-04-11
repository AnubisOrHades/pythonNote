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
