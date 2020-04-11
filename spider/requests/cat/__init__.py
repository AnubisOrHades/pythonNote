import requests


def get_host(url="https://www.766uy.com/enter/pc.html"):
    """
    获取猫咪社区主机地址
    :param url:
    :return: 主机地址
    """
    html = requests.get(url)
    host = html.url.split("/")[2]
    print("https://" + host)
    return host


if __name__ == '__main__':
    CAT_HOST = get_host()
    cat_dict = {
        "short_videos": "https://{}/shipin/list-%e7%9f%ad%e8%a7%86%e9%a2%91.html".format(CAT_HOST),
        "guo_videos": "https://{}/shipin/list-%E5%9B%BD%E4%BA%A7%E7%B2%BE%E5%93%81.html".format(CAT_HOST),
    }
    for k, v in cat_dict.items():
        print("{}:{}".format(k, v))
