import requests
import os
import re
from lxml import etree

HOST = "https://www.runoob.com"
startUrl = "https://www.runoob.com/numpy/numpy-tutorial.html"

task_url = []

path = r"D:\Anubis\Note\runoob\numpy"


# 获取所有连接

def get_url_list(url):
    try:
        html = requests.get(url)
        html.encoding = "UTF-8"
        html = etree.HTML(html.text)
        lis = html.xpath('//div[@id="leftcolumn"]/a')
        for url in lis:
            name = url.xpath('./text()')[0]
            link = url.xpath('./@href')[0]
            print(name.strip(), "\t:", link)
            task_url.append({"name": name.strip(), "link": link})
        pass
    except Exception as e:
        print("Error:{}".format(e))
    else:
        pass
    finally:
        pass


# 创建文件夹

# 爬取网页保存
def down_html(task):
    try:
        html = requests.get(HOST + task["link"])
        html.encoding = "utf8"

        file_name = "{}\\{}.html".format(path, task["name"])
        with open(file_name, "wb")as f:
            f.write(html.content)
    except Exception as e:
        print("Error:{}".format(e))
    else:
        pass
    finally:
        pass


def text_clear(text):
    try:
        header_text = """<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <meta property="qc:admins" content="465267610762567726375" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<title>NumPy 教程 | 菜鸟教程</title>

  <link rel='dns-prefetch' href='https://www.runoob.com//s.w.org' />
<link rel="canonical" href="http:https://www.runoob.com//www.runoob.com/numpy/numpy-tutorial.html" />
<meta name="keywords" content="NumPy 教程,numpy">
<meta name="description" content="NumPy 教程    NumPy(Numerical Python) 是 Python 语言的一个扩展程序库，支持大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库。  NumPy 的前身 Numeric 最早是由 Jim Hugunin 与其它协作者共同开发，2005 年，Travis Oliphant 在 Numeric 中结合了另一个同性质的程序库 Numarray 的特色，并加入了其它扩展而开发了 NumPy。N..">
		
	<link rel="shortcut icon" href="https://www.runoob.com//static.runoob.com/images/favicon.ico" mce_href="https://www.runoob.com//static.runoob.com/images/favicon.ico" type="image/x-icon" >
	<link rel="stylesheet" href="https://www.runoob.com/wp-content/themes/runoob/style.css?v=1.154" type="text/css" media="all" />	
	<link rel="stylesheet" href="https://www.runoob.com//static.runoob.com/assets/font-awesome/4.7.0/css/font-awesome.min.css" media="all" />	
  <!--[if gte IE 9]><!-->
  <script src="https://www.runoob.com//static.runoob.com/assets/jquery/2.0.3/jquery.min.js"></script>
  <!--<![endif]-->
  <!--[if lt IE 9]>
     <script src="https://www.runoob.com//cdn.staticfile.org/jquery/1.9.1/jquery.min.js"></script>
     <script src="https://www.runoob.com//cdn.staticfile.org/html5shiv/r29/html5.min.js"></script>
  <![endif]-->
  <link rel="apple-touch-icon" href="https://www.runoob.com//static.runoob.com/images/icon/mobile-icon.png"/>
  <meta name="apple-mobile-web-app-title" content="菜鸟教程">
</head>"""
        pattern_header = ''
        re.sub(pattern_header, header_text, text, count=1)
    except Exception as e:
        print("Error:{}".format(e))
        return False
    else:
        pass
    finally:
        pass


if __name__ == '__main__':
    get_url_list(startUrl)
    for t in task_url:
        down_html(t)
        break
