from Example.win.winInput import *
from pothoto import get_host
import win32gui


def open_chrome():
    key_input("windows", "r")
    input_txt("chrome")
    key_input("enter")


def run(code):
    print(code)
    # 复制文本
    time.sleep(0.5)
    mouse_click((300, 600))
    time.sleep(0.5)
    key_input("ctrl", "a")
    time.sleep(0.5)
    key_input("ctrl", "c")
    # 打开浏览器
    open_chrome()
    time.sleep(2)
    # 油侯脚本
    mouse_click((1435, 50))
    time.sleep(0.5)
    # 脚本管理
    mouse_click((1305, 250))
    time.sleep(0.5)
    # 选择编辑脚本
    mouse_click((250, 250))
    time.sleep(0.5)
    # 确定光标
    mouse_click((1000, 500))
    time.sleep(0.5)

    # 替换文本
    key_input("ctrl", "a")
    time.sleep(0.5)
    key_input("ctrl", "v")
    time.sleep(0.5)
    # 编辑文本
    mouse_click((64, 360))
    for i in range(200):
        key_input("backspace")
    time.sleep(0.5)

    # 保存文本
    key_input("ctrl", "s")
    time.sleep(1)

    # 退出chorme
    key_input("alt", "F4")
    pass


if __name__ == '__main__':
    HOST = "www.986uy.com"
    HOST = get_host()
    code = r"""
// ==UserScript==
// @name         New Userscript
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://%s/shipin/list-*
// @grant        none
// @require      https://code.jquery.com/jquery-1.12.4.min.js
// ==/UserScript==

(function() {
    'use strict';
    $(document).ready(function () {
        var Ahref = $("#grid>li>a");
        for (var i = 0; i <Ahref.length;i++) {
            Ahref[i]["href"]="https://%s/shipin/play-" + Ahref[i]["href"].split("/")[4] + "?road=1"
            //console.log(Ahref[i]["href"].split("/"));
            }
        });
    // Your code here...
})();
    """ % (HOST, HOST)
    run(code)
