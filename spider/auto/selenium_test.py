import time

from selenium import webdriver  # 导入库
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

setup = Options()  # 实例化设置功能（启动参数对象）

# setup.add_argument() # 设置浏览器以无界面方式运行

# setup.add_argument('--disable-gpu')  #   官方文档表示这一句在之后的版本会消失，但目前版本需要加上此参数

setup.add_argument("--start-maximized")  # 最大化浏览器

# setup.add_argument('--window-size=1366,768')  #  设置系统的浏览器窗口大小
browser = webdriver.Chrome(chrome_options=setup)
# browser.maximize_window()
# url = 'https://www.youku.com/'
item_id = 60703097098

url = "https://air.alibaba.com/intl/18ac8/mobile/homepage/hotsale.html?" \
      "spm=a2706.8172434.mod-top-selling.2.3b29284f8vZHBT&wh_weex=true&product&Ids={}".format(item_id)
browser.get(url)  # 打开浏览器预设网址
# print(browser.page_source)  # 打印网页源代码

# browser.find_elements_by_xpath('//*[@id="uerCenter"]/div[6]/div/a/img')[0].click()
# time.sleep(10)
#
# browser.find_elements_by_xpath('//*[@id="login"]/div[1]/i')[0].click()
# time.sleep(122)
# browser.close()  # 关闭浏览器
