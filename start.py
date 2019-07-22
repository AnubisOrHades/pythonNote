from Example.win.winInput import *
import os

tasks = [
    {"code": "jupyter notebook", "program": "jupyter notebook"},
    {"code": "", "program": ""},
    {"code": "", "program": ""},
    {"code": "", "program": ""},
    {"code": "", "program": ""},
    {"code": "", "program": ""},
    {"code": "", "program": ""},
    {"code": "", "program": ""},
    {"code": "", "program": ""},
    {"code": "", "program": ""},
]


def run():
    for index, task in enumerate(tasks):
        print("{}\t{}".format(index + 1, task["program"]), end="\t\t")
        if (index + 1) % 3 == 0:
            print()
    print()
    print("按b键退出")
    while 1:
        choice = input("请选择程序的启动编号>>>")
        if choice == "b":
            break
        try:
            print(tasks[int(choice)-1])
            os.system(tasks[int(choice)-1]["code"])
        except:
            print("序号输入错误")
        else:
            print("{}已经启动成功！")


def test(*args):
    for i in args:
        print(i)


if __name__ == '__main__':
    run()
    # key_input("ctrl","backspace")
    # win32api.keybd_event(VK_CODE["ctrl"], 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
    # win32api.keybd_event(VK_CODE["backspace"], 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
    # win32api.keybd_event(VK_CODE["backspace"], 0, win32con.KEYEVENTF_KEYUP, 0)
    # win32api.keybd_event(VK_CODE["ctrl"], 0, win32con.KEYEVENTF_KEYUP, 0)

    # [3, 226, 25, 1, 2, 1, 1, 0, 1, 3, 0, 0, 255]
    # s = b'\x03\xe2\x19\x01\x02\x01\x01\x00\x01\x03\x00\x00\xff'
    # result = [i for i in s]
    # for i in s:
    #     result.append(i)

    from pymongo import MongoClient

    # conn = MongoClient("localhost", 27017)
    # db = conn["SpiderData"]
    # table = db["zhilian"]
    # keys = ["_id", "applyType", "updateDate", "refreshMulscore", "g_sort", "endDate", "city", "showLicence", "saleType",
    #         "positionURL", "g_weight", "industry", "welfare", "salary", "SOU_POSITION_ID", "duplicated", "geo", "score",
    #         "number", "vipLevel", "recruitCount", "workingExp", "companyScore", "tagIntHighend", "company", "seo",
    #         "jobType", "g_query", "resumeCount", "createDate", "jobName", "manualScore", "eduLevel", "companyLogo",
    #         "futureJob", "emplType", "g_source", "SOU_POSITION_SOURCE_TYPE", "recentAndTotal", "tags", "businessArea",
    #         "positionLabel", "expandCount", "jobTag", "feedbackRation", "interview", "selected", "applied", "collected",
    #         "isShow", "timeState", "rate", ]
    # result = []
    # for i in table.find():
    #     lis = ["None"] * 52
    #     for k in i:
    #         # print('"{}",'.format(k), end="\t")
    #
    #         if k in keys:
    #             lis[keys.index(k)] = i[k]
    #     result.append(lis)
    # for i in result:
    #     print(i[0])
