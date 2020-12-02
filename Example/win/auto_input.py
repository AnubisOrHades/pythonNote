import keyboard

from Example.win.winInput import input_txt

INFO1 = """入职要求
1. 年龄限制：男性16-----45周岁，女性16-----38周岁
2. 文化限制：初中以上文化（包括初中），必须不会26个英文字母（熟练读写）
3. 身高限制：男性1.60米以上，女性1.50米以上
4. 身体限制：需要身体健康，无任何传染疾病，身体无残疾，无钢1板/钢筋，没有急性病，无案底
5. 民族限制：四川彝族、回族、维吾尔族、藏族 不要，其他都要
6. 公司要求：严禁打架斗殴、辱骂他人、迟到、早退、旷工；服从公司领导安排
7. 有经验者、退伍军人优先录取
"""
INFO2 = """工作自责：主要负责指定物品送达，保证能够安全到达指定地点
"""
INFO3 = """薪资：短途6500/长途8500  + 出差补助 +全勤+五险一金
"""
INFO4 = """上岗前要接受公司培训的，培训通过才能上岗，
培训周期15天左右，具体看个人掌握情况，
带薪培训，培训期底薪6500
"""
INFO5 = """面试时间：早上：8:30----10:00，记得带行李，
面试通过后，公司当然安排入职、住宿的
"""
INFO6 = """《报名表》
姓名：
性别：
年龄：
民族：
籍贯：
应聘岗位：
电话号码：
身份证号码：
有无犯罪记录：无
是否有纹身烟疤：无
是否有残疾和疾病：无
报道日期：
注：以上内容请根据真实情况填写，如有隐瞒不给予入职，
表格填写好，我们会根据车票日期帮您保留岗位和报道日期安排面试入职手续和报道当天的食宿问题！
"""
INFO7 = """
"""
INFO8 = """
"""
INFO9 = """
"""
INFO10 = """
"""
if __name__ == '__main__':
    keyboard.add_hotkey("f1", input_txt, args=(INFO1,))
    keyboard.add_hotkey("f2", input_txt, args=(INFO2,))
    keyboard.add_hotkey("f3", input_txt, args=(INFO3,))
    keyboard.add_hotkey("f4", input_txt, args=(INFO4,))
    keyboard.add_hotkey("f4", input_txt, args=(INFO4,))
    keyboard.add_hotkey("f5", input_txt, args=(INFO5,))
    keyboard.add_hotkey("f6", input_txt, args=(INFO6,))
    keyboard.add_hotkey("f7", input_txt, args=(INFO7,))
    keyboard.add_hotkey("f8", input_txt, args=(INFO8,))
    keyboard.add_hotkey("f9", input_txt, args=(INFO9,))
    keyboard.add_hotkey("f10", input_txt, args=(INFO10,))

    keyboard.wait()
