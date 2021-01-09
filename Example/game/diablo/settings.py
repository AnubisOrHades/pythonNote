# 技能搭配列表
skill_matching = {
    "three_lights": {
        "one": 2,
        "two": 1,
        "three": 1,
        "four": 1
    },
    "three_lights_q": {
        "one": 14,
        "two": 21,
        "three": 1000,
        "four": 21
    },
    "wind": {
        "one": 21,
        "two": 50,
        "three": 60,
        "four": 4
    },
    "wind_q": {
        "one": 21,
        "two": 20,
        "three": 6,
        "four": 400
    },
    "witcher": {
        "one": 1,
        "two": 1,
        "three": 7,
        "four": 400
    },
    "death": {
        "one": 120,
        "two": 120,
        "three": 1,
        "four": 120
    },
    "house": {
        "one": 15000,
        "two": 15,
        "three": 15,
        "four": 45
    }
}

# 设备列表
devices = {
    "magic": {
        # 物品栏左上坐标
        "left_top": [1165, 450],
        # 物品栏右下坐标
        "right_button": [1530, 690],
        # 铁匠分解坐标
        "decompose": [125, 225],
        # 宝石升级坐标
        "upgrading": [200, 440],
        # 宝石坐标
        "gemstone": [300, 500]
    },
    "free": {
        "left_top": [1455, 560],
        "right_button": [1905, 860],
        "decompose": [150, 300]
    }
}

# 选择设备
device = "magic"

# 选择技能搭配
DIABLO_ROLE = skill_matching["death"]

LEFT_TOP = devices[device]["left_top"]
RIGHT_BOTTOM = devices[device]["right_button"]
DECOMPOSE = devices[device]["decompose"]
UPGRADING = devices[device]["upgrading"]
GEMSTONE = devices[device]["gemstone"]

