import requests
import os


if __name__ == '__main__':
    i = 317
    while i < 568:
        # ii = "0" * (5 - len(str(i))) + str(i)
        # print(ii)
        url = "https://s1.maomibf1.com/common/zw/2019_06/04/zw_vwfkCWxC_wm/zw_vwfkCWxC_wm{}.ts".format(i)
        print(url)
        html = requests.get(url)

        with open(r"D:\Anubis\猥琐中出\{}.ts".format(i), "wb")as f:
            f.write(html.content)
            # c = f.read()
            # with open(r"D:\Anubis\通姦女同性恋.mp4", "ab")as t:
            #     t.write(c)
        i += 1
    os.system(r"copy/b  D:\Anubis\猥琐中出\*.ts  D:\Anubis\猥琐中出\猥琐中出.ts")
"""
copy/b D:\Anubis\通姦女同性恋\*.ts D:\Anubis\通姦女同性恋\new.ts
"""
