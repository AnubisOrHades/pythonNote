import requests
from lxml import etree
import xlwt
workbook = xlwt.Workbook(encoding = 'utf-8')
worksheet = workbook.add_sheet('经销商')
# worksheet.write(0, 0, label = '00')
# worksheet.write(1, 0, label = '10')
# worksheet.write(0, 1, label = '01')

url = ["https://www.tianyancha.com/search/p{}?key=%E5%86%9C%E8%B5%84%E7%BB%8F%E9%94%80&base=hen".format(i) for i in
       range(1, 6)]
result=[]
# for u in url:
#     header = {
#         "Accept": "text / html,application /xhtml+ xml,application/xml;q=0.9,image/webp,image/apng,*/*;q = 0.8,application/signed-exchange;v=b3",
#         "Accept - Encoding": "gzip, deflate, br",
#         "Accept - Language": "zh - CN, zh;q = 0.9",
#         "Cache - Control": "max - age = 0",
#         "Connection": "keep - alive",
#         "Cookie": "aliyungf_tc=AQAAAPZlH267dQ4ABuvFAUKCfs5gmMSr; ssuid=6381984362; csrfToken=9Bl_zR7NVyUhK0AcZCtqJRVr; TYCID=6db8cbe089a411e98faa2330b5b68aa7; undefined=6db8cbe089a411e98faa2330b5b68aa7; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1559967492; _ga=GA1.2.1468280039.1559967493; _gid=GA1.2.1945556441.1559967493; RTYCID=4b6adfb82b5345e8bc1d10cf0441e991; CT_TYCID=6f1c3091af61465d9c005846b5e3b9fb; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E9%2599%2588%25E6%25B1%25A4%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTkzNjM0Njk4MSIsImlhdCI6MTU1OTk2NzYyNSwiZXhwIjoxNTkxNTAzNjI1fQ.vQjXU2h7wr_C90Wg4T7Z2V2QLihGjGDn50uIJ0x7oN7LO2z4KSpPbdGhNdpMXhBGo2QMgrLov6w6yJWOc6jtOQ%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252215936346981%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTkzNjM0Njk4MSIsImlhdCI6MTU1OTk2NzYyNSwiZXhwIjoxNTkxNTAzNjI1fQ.vQjXU2h7wr_C90Wg4T7Z2V2QLihGjGDn50uIJ0x7oN7LO2z4KSpPbdGhNdpMXhBGo2QMgrLov6w6yJWOc6jtOQ; __insp_wid=677961980; __insp_slim=1559967823937; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93d3cudGlhbnlhbmNoYS5jb20vY2xhaW0vZW50cnkvNTcxMDQ0Mzg0; __insp_targlpt=5aSp55y85p_lLeWVhuS4muWuieWFqOW3peWFt1%2FkvIHkuJrkv6Hmga%2Fmn6Xor6Jf5YWs5Y_45p_l6K_iX_W3peWVhuafpeivol%2FkvIHkuJrkv6HnlKjkv6Hmga%2Fns7vnu58%3D; __insp_norec_howoften=true; __insp_norec_sess=true; bannerFlag=true; cloud_token=3a75cce828b8457ab8a7d90dcfb5754d; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1559970481",
#         "Host": "www.tianyancha.com",
#         "Upgrade - Insecure - Requests": "1",
#         "User - Agent": "Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML,likeGecko)Chrome/73.0.3683.103Safari/537.36"
#     }
#     html = requests.get(u, headers=header)
#     # print(html.text)
#     html = etree.HTML(html.text)
#     lis = html.xpath('//div[@class="search-item sv-search-company"]')
#     print(len(lis))
#     for l in lis:
#         # title = l.xpath("./text()")
#         print(l)
#     # break

base_path = r"C:\Users\武晓涛\Desktop\农资"
x = 1
for i in range(2, 6):
    with open("{}\\{}.html".format(base_path, i), "r", encoding="utf8")as f:
        html = etree.HTML(f.read())
        lis = html.xpath('//div[@class="search-result-single   "]')
        company_details = {}
        # print(len(lis))

        for company in lis:
            company_details["name"] = company.xpath('./div[@class="content"]/div[@class="header"]/a/text()')[
                                          0] + "农资经销" + \
                                      company.xpath('./div[@class="content"]/div[@class="header"]/a/text()')[-1]
            # company_details["name"]=company.xpath()
            company_details["mater"] = \
                company.xpath('./div[@class="content"]/div[@class="info row text-ellipsis"]/div[1]/a/text()')[0]
            company_details["assets"] = \
                company.xpath('./div[@class="content"]/div[@class="info row text-ellipsis"]/div[2]/span/text()')[0]
            company_details["born"] = \
                company.xpath('./div[@class="content"]/div[@class="info row text-ellipsis"]/div[3]/span/text()')[0]
            if len(company.xpath(
                    './div[@class="content"]//span/text()')) > 2:
                company_details["tel"] = \
                    company.xpath('./div[@class="content"]//span/text()')[3]

            else:
                company_details["tel"] = "-"

            if "销" in company_details["tel"]:
                company_details["tel"] = "-"

            # if len(company.xpath('./div[@class="content"]/div[@class="contact row"]/div[2]/span[2]/text()')) == 0:
            #     company_details["email"] = "None"
            # else:
            # try:
            #     company_details["email"] = \
            #     company.xpath('./div[@class="content"]/div[@class="contact row"]//span/text()')[0]
            # except:
            #     company_details["email"] = "None"
            y=0
            for k,v in company_details.items():
                print(v,end="\t\v")
                worksheet.write(x, y, label=v)
                y+=1
            x+=1
            print()
if __name__ == '__main__':
    workbook.save('农资.xls')
