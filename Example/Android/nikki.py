from Example.Android.command import *
import json


def import_data(path='nikki.json'):
    """
    获取json数据
    :param path: json文件地址
    :return: json数据
    """
    with open(path, 'r', encoding='UTF-8')as f:
        json_data = json.loads(f.read())
    return json_data["data"]


def get_clothes_set():
    """
    获取衣服集合
    :return:
    """
    clothes_set = set()
    for i in import_data():
        for c in import_data()[i]:
            clothes_set.add(c)
    print("共有衣服：{}件".format(clothes_set.__len__()))
    return clothes_set


def in_game():
    """
    进入游戏
    :return:
    """
    click(400, 1350)
    time.sleep(11)
    click(550, 1695)
    time.sleep(3)
    click(570, 1395)
    time.sleep(3)
    click(500, 1600)
    time.sleep(8)
    print("已进入游戏")


def free():
    """
    点击空格
    :return:
    """
    click(950, 1800)
    time.sleep(1)


def go_break():
    """
    返回
    :return:
    """
    click(80, 90)


def house_of_mystery():
    """
    迷之屋
    :return:
    """
    # 进入
    click(700, 350)
    # 幻之阁

    click(350, 1700)
    free()
    time.sleep(1)
    free()
    click(350, 1050)
    click(1050, 810)
    # slide()
    # 迷之阁
    for i in range(4):
        click(200, 1710)
        time.sleep(2)
        free()
        free()
    # 返回主页
    go_break()


def union():
    """
    塔配师联盟
    :return:
    """
    # 进入
    click(800, 730)
    # # 委托
    # click(550, 1150)
    # # 进行任务
    # click(890, 1200)
    # click(450, 1400)
    # free()
    # time.sleep(2)
    # free()

    click(90, 310)
    # 图书馆
    click(880, 1500)
    for i in range(3):
        click(300, 660)
        free()
    go_break()
    # 返回主页
    go_break()


def dream():
    """
    织梦人学会
    :return:
    """
    # 进入
    click(700, 1050)
    # 学会委托
    click(300, 940)
    y = 800
    for i in range(3):
        click(540, y)
        click(720, 1100)
        click(500, 600)
        click(500, 600)
        y += 300
        time.sleep(1)
    free()

    # 浮梦岛
    click(300, 1500)
    click(300, 1750)
    free()
    time.sleep(1)
    free()
    # 返回主页
    go_break()
    time.sleep(2)
    go_break()
    go_break()


def garden():
    """
    御园琼芳
    :return:
    """
    # 进入
    slide(800, 1100, 200, 1100, 300)
    click(850, 1500)
    for i in range(2):
        # 过关
        click(90, 1620)
        click(600, 970)
        free()
        time.sleep(1)
        free()
        free()

        click(970, 1620)
        click(600, 970)
        free()
        time.sleep(1)
        free()
        if i == 0:
            click(970, 1800)
            click(900, 900)

    # 返回主页
    go_break()


def sports():
    """
    搭配竞技场
    :return:
    """
    # 进入
    click(170, 540)
    # 登台
    for i in range(5):
        click(550, 1570, 3)
        click(870, 1600, 2)
        free()
        time.sleep(1)
        free()

    # 返回主页
    go_break()


def cabana():
    """
    小屋家具
    :return:
    """
    # 进入
    click(850, 1700)

    import time

    time_start = "2019-09-29 01:12:12"
    n = time.mktime(time.strptime(time_start, "%Y-%m-%d %H:%M:%S"))
    s = (time.time() - n) // 60 // 60 // 24
    if s % 2 == 0:
        # 愿之庭
        click(1000, 1240)
        click(300, 1820)
        y = 350 + 400
        for i in range(3):
            click(500, y)
            click(350, 1750)
            free()
            time.sleep(1)
            free()
            click(350, 1070)
            go_break()
            y += 400
        go_break()
    time.sleep(2)

    # 外出拜访5次
    click(1000, 1100)
    click(550, 1000)
    time.sleep(3)
    for i in range(8):
        click(1000, 1800)
        time.sleep(2)

    go_break()
    time.sleep(2)

    # 返回主页
    go_break()


def open_box(n):
    """
    打开失落之匣
    :return:
    """
    code = "adb shell input tap {} {}".format(100, 230)
    for i in range(n):
        os.system(code)
        time.sleep(0.5)
        click(100, 230)
        free()


def furniture(n):
    """
    获取家具
    :param n: 票数量
    :return:
    """
    click(880, 420)
    n = n // 5
    for i in range(n):
        print(1)
        click(740, 1000)
        time.sleep(1)
        print(2)
        click(970, 1670)
        print(3)
        click(530, 1540)
    free()


def reward():
    """
    领取奖励
    :return:
    """
    click(1000, 500)
    for i in range(12):
        click(900, 850)
        free()

    time.sleep(1)
    x = 250
    for i in range(5):
        click(x, 670)
        free()
        x += 160


def buy():
    """
    购买灵幔
    :return:
    """
    # 进入商店
    click(200, 1400)
    slide(500, 1500, 500, 750, 300)
    # 购买3件灵幔
    click(660, 1300)
    click(800, 850)
    click(850, 840)
    click(850, 840)
    click(750, 1150)
    # 返回主页
    go_break()


def decompose():
    """
    分解灵幔
    :return:
    """

    # 进入分解
    click(250, 1000)
    click(550, 1300)
    # 分解灵幔
    long_press(150, 1300)
    click(550, 800)
    click(720, 1070)
    for i in range(4):
        time.sleep(1)
        free()
    # 返回主页
    go_break()


def end_game():
    """
    退出游戏
    :return:
    """
    break_adb()
    click(550, 1600)


def judges():
    """
    当评委
    :return:
    """
    click(120, 760)
    time.sleep(2)
    click(670, 1800)
    time.sleep(2)
    for i in range(30):
        click(800, 1720)
        time.sleep(3)
    go_break()
    time.sleep(2)
    go_break()


def my_task():
    """
    过关做任务
    :return:
    """
    click(80, 310)
    click(610, 520)
    x = 300
    y = 1300
    for i in range(1, 7):
        click(x, y)
        click(800, 900)
        click(470, 1400)
        click(450, 1400)
        free()
        time.sleep(2)
        free()
        click(80, 300)
        if i % 2 == 1:
            x += 500
        else:
            y += 130
            x -= 500
    free()


def change_clothes(collocation):
    """
    更换搭配
    :param collocation: 搭配列表
    :return:
    """
    click(800, 1400)
    click(60, 880, 3)
    # 清空搭配
    click(680, 1580)
    # 切换adbkeyboard输入法
    os.system("adb shell ime set com.android.adbkeyboard/.AdbIME")
    for clothes in collocation:
        # 搜索
        click(680, 1000)
        # 输入衣服
        click(500, 820)
        input_abd(clothes)
        click(500, 300)
        # 选中衣服
        click(900, 170)
    # 保存搭配
    click(160, 1780)
    # 切换搜狗输入法
    os.system("adb shell ime set com.sohu.inputmethod.sogou/.SogouIME")
    go_break()


def task():
    # 开始任务
    click(840, 1400)
    click(980, 1850)
    click(720, 1050)
    # 选择搭配
    click(680, 1220)
    click(930, 520)
    click(170, 1770)

    click(915, 1770)
    time.sleep(1)
    click(170, 1770)
    time.sleep(1)
    click(670, 1770)
    time.sleep(1)
    click(460, 1770)
    time.sleep(1)
    click(170, 1770)

    free()
    free()
    free()
    free()


def chose(clothes, f="("):
    for c in clothes.split(">"):
        print(c.split(f)[0])
        click(680, 1000)
        # 输入衣服
        click(500, 820)
        input_abd(c.split(f)[0])
        click(500, 300)
        time.sleep(1)
        if len(clothes.split(">")) == 1 or c.split(f)[0] in CLOTHES:
            click(900, 170)
            break


def judges_box(n):
    click(120, 760)
    time.sleep(2)
    click(670, 1800)
    time.sleep(2)
    for i in range(n // 10):
        click(690, 1870)
        free()
    go_break()
    time.sleep(2)
    go_break()


if __name__ == '__main__':
    # CLOTHES = get_clothes_set()
    CLOTHES = {'牵心结缘灯', '星夜梦话', '甜奶酪', '星辰华尔兹', '年份羁绊', '团子', '随心幻想', '天星草', '泡沫·华丽', '蜜圆', '怪盗面具', '梦礼纱', '舞娘足饰',
               '青凰曲', '烟竹伴雪', '凤冥圣后', '童话猎枪', '光明手杖·华丽', '回旋乐章', '吉祥花结', '梦中的婚礼', '复古单镜', '毛绒猴帽', '思君归', '狸仙咒语', '萌熊挎包',
               '热情阳光', '海上花·珍稀', '落蕊珠', '莉莉安娜·梦', '舞动梦想·华丽', '修女的忏悔', '神秘夜会', '永恒信仰·夜', '上弦之月', '飘雪沁人心', '魅惑蔓延', '寒霜之环',
               '塔罗·珍稀', '初云裤·蓝', '莓果奶昔', '清心悦影笛', '刺客大腿袜', '双瑞', '风华·墨', '提线木偶', '吉祥坠', '花香雪', '舞会假面·梦', '夜芙海棠', '衔叶小鹿',
               '心形糖纸', '白喵尾', '构界手套', '镂空小礼袖', '莹缀彩结', '花嫁', '北国春声', '余韵轻绕', '万圣巫师帽·绮夜', '魅惑蔓延·奇迹', '程序规则', '地狱来使',
               '百合长袜', '洗沙', '蛾纹长靴', '青鸾环', '轻柔粉结', '花嫁头纱', '百海结福', '凌乱萌', '断空·晖云', '樱月夜', '天水碧衫', '荣耀之名', '暖棕喵尾',
               '甜蜜陪伴', '亚尼拉海盗', '星海链', '水绕环', '皇族身份·珍稀', '刺客信念·华丽', '星河纱巾', '太古祷歌', '红枫缎·珍稀', '汤姆挎包', '千罂狐尾', '美味糕点',
               '毛绒兔耳·华丽', '极星眼镜', '缀樱语', '蝴蝶舞', '饼干胸针·珍稀', '丛林之王', '团簇锦', '猎杀双刃', '心之光彩', '梦泛涟漪', '名门淑女', '祥云盘蕊',
               '暖心相伴', '石桥路', '浪带·华丽', '简易竹筷', '碧海青天', '镭射手枪', '月桂手环', '天使翅膀', '绮花灼火', '野性颈圈', '机械天使', '草莓糕点·珍稀',
               '丢丢遮阳伞', '蝶舞轻饶·珍惜', '爆米花机', '星夜卜', '锦缎鼓', '炮火如兰', '变幻', '心笙遥寄', '新的家人', '暖心玩偶·头', '奇幻魔术', '裙摆微扬', '曼殊沙华',
               '圣灵天使', '坠萦牵梦', '魅惑颈圈·奇迹', '骑士之靴', '昊天云冠', '萤火', '金福猴尾', '古典书架', '胡萝卜美梦', '刺客腰饰·华丽', '真实谎言', '芊眠·晨',
               '冠蓝鸦', '娇俏劳模·上', '四象之灵', '棕熊短裤', '魔幻领结', '闪耀夏日', '梦纱', '残破木偶', '玉匣开新境', '梦古', '吉祥扣', '隐士披风', '强烈的思念',
               '明日的一步', '白雪歌谣', '萌宠之心', '蔚海·华丽', '恶魔手环', '雷克斯暴龙', '羊毛短袜', '灵瑞猴尾', '凌乱纷扰', '吸血花蕊', '金耀手链', '缎带颈饰·珍稀',
               '尘封回忆', '夜影迷踪', '纯真天使', '魂令', '星之魔法阵', '曲意怜心', '筋斗云', '风起叶落', '钻链', '心折冰炭', '彩虹奶霜', '绮丽兔帽', '刀锋短剑',
               '铭刻永恒', '轻松木屐', '叶萦牵梦', '梦幻之辉', '花昔少女·珍稀', '束缚绷带', '金猴送福', '梦溪履', '白鹿青崖', '染殷华', '荒漠', '竹节骨', '柔雪落樱',
               '晨雾漫舞', '樱花茶', '鹤膝竹', '爱心礼盒', '轻絮', '淡墨痕', '薄荷糖', '月宫玉兔', '小桃红', '暖心相随', '丛林印记', '粉色兔子', '维纳斯之舞', '白果耳坠',
               '彩面小丑', '轻甜回忆', '玲珑戏蝶', '小红帽的篮子', '灵隐彩珠·华丽', '守望之星', '时间指向·夜', '薄纱蕾丝', '枯骨', '清甜回忆', '信使臂环·信件', '月明千里',
               '撒菱', '女仆颈圈', '玛格丽特', '提线枷锁', '轻熟心情', '左右逢源·蓝', '血色牢笼', '古堡迷失·珍稀', '越空追击', '飘摇之舞', '贪嘴小熊猫', '冬日相遇',
               '绮梦星光', '轮回指针', '芝士蛋糕·珍稀', '星尘华尔兹', '花月斐', '雪山回响', '喔喔的提篮', '兽人之耳', '祈愿斗篷', '麦浪', '阴阳黑白', '瑰丽人生', '青墨',
               '幻夜魔尾', '恋爱数据', '首领徽记', '孤寂余音', '波浪马尾', '天国信使·信件', '恢宏时代', '猫咪指挥', '桃心骑士', '灯笼褶裤', '浅粉幻想', '敛烟蛾', '暗夜摩托',
               '红斗篷·珍稀', '信使臂环', '真皮钱包', '千层雪', '圣夜之愿', '欢愉魔法', '摇摆熊', '梦落心尖', '人偶丝带', '神圣之音', '水纱少灵·夏', '彩夜星光', '银翼之瞳',
               '残破枷锁', '软萌印花袜', '荒原挎包', '吉祥如意·蓝', '鹤之影', '呆萌高跟', '海上珠链·珍稀', '深渊咏叹', '梅雪细钿', '虹色落影', '枯叶鳞翅', '呆呆脸',
               '公主的戎装', '雾鬓风鬟', '花蜜语', '柳眉星眼', '怪盗面具·华丽', '竹墨书', '翻糖蝴蝶结'}
    # slide(500, 1500, 500, 750, 300)
    # click(980, 1750)
    # click(900, 900)
    wem = ""
    # change_clothes(import_data()["3-6"])

    C = """海空之吻(1763夏沫海歌)>鹊桥相会(1637缘梦七夕)>提琴幽语(1438古典之声音乐会)"""
    chose(C)
