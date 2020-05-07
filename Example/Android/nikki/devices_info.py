devices_set = {
    "magic_20": {
        "free": (1050, 1500),
        "break": (75, 190),
        # 迷之屋
        "house_of_mystery": {
            "door": (700, 650),
            "magical": (350, 2000),
            "cancel": (350, 1300),
            "right": (1040, 1040),
            "mystery": (200, 2000),

        },
        # 搭配师联盟
        "union": {
            "door": (800, 1050),
            "library": (900, 1850),
            "cleared": (300, 888),
        },
        # 织梦人学会
        "dream": {
            "door": (700, 1350),
            "go_tasks": (300, 1250),
            "enter": (748, 1290),
            "free": (540, 800),
            "tasks": [(550, 1030), (550, 1300), (550, 1560), ],
            "break": (600, 2000),
            "islands": (300, 1850),
            "explore": (300, 2100),
        },
        # 御苑琼芳
        "garden": {
            "door": (850, 1800),
            "task1": (90, 2000),
            "task2": (1000, 2000),
            "third": (600, 1180),
            "free": (500, 1800),
            "change": (1000, 2160),
            "go_one": (900, 1100),

        },
        # 搭配竞技场
        "sports": {
            "door": (175, 900),
            "stage": (570, 1950),
            "quick": (880, 1960),
        },
        # 小屋
        "cabana": {
            "door": (850, 2000),
            "wish": (1000, 1550),
            "long": (330, 2200),
            "wishing": (350, 2050),
            "cancel": (350, 1300),
            "task": [
                (500, 480),
                (500, 850),
                (500, 1200),
                (500, 1600)
            ],
            "stroll": [(1000, 1330), (500, 1200)],
            "visit": (950, 2200),
        },
        "furniture": {
            "door": (9, 9),
        },
        # 服装店
        "shopping": {
            "door": (170, 1700),
            "clothe": (400, 1550),
            "buy": (800, 1100),
            "add": (880, 1070),
            "buy_enter": (780, 1350)
        },
        # 设计工坊
        "design_center": {
            "door": (300, 1250),
            "decompose_door": (500, 1500),
            "clothe": (200, 1550),
            "decompose": (550, 1000),
            "decompose_enter": (750, 1300)
        },
        # 搭配评选赛
        "judges": {
            "door": (135, 1050),
            "vote_door": (650, 2175),
            "vote": (780, 2050),
        },
    }
}
if __name__ == '__main__':

    s = """house_of_mystery 迷之屋
union 搭配师联盟
dream 织梦人学会
garden 御苑琼芳
sports 搭配竞技场
cabana 小屋
shopping 服装店
design_center  设计工坊
judges 搭配评选赛"""

    for i in s.split("\n"):
        e = i.split()[0]
        c = i.split()[1]
        # print('"{}":{{\n"door":(9,9),\n}},'.format(i))
        # print("""def {}(self):
        # try:
        #     click(self.android["{}"]["door"][0], self.android["{}"]["door"][1])
        # except Exception as e:
        #     print(e)
        # else:
        #     pass
        # finally:
        #     pass
        #     """.format(i, i, i))
        print("""#{}
self.{}()
print("{}\t完成！！！".center(100,"="))""".format(c, e, c))
