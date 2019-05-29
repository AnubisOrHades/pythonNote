class Player:
    def __init__(self, role, address, attack_distance=1, arms=None, shield=None, horse_plus=False, horse_reduce=False):
        """
        player实例化
        :param role: 身份（主公，忠臣，反贼，内奸）
        :param address:
        :param attack_distance:攻击距离
        :param arms: 武器
        :param shield: 防具
        :param horse_plus: 加1马增加防御距离
        :param horse_reduce: 减1马增加攻击距离
        """
        self.role = role
        self.address = address
        self.attack_distance = attack_distance
        self.arms = arms
        self.shield = shield
        self.horsePlus = horse_plus
        self.horseReduce = horse_reduce


class Card:
    def __init__(self, name, num, color):
        """
        卡牌属性
        :param name: 名字
        :param num: 数值（1--13）
        :param color: 花色（黑桃：spade，红桃：hart，方块：diamond，梅花：club）
        """
        self.name = name
        self.num = num
        self.color = color


class Kill(Card):
    def __init__(self, num, color, name=None):
        name = "kill" if name is None else name
        Card.__init__(self, name, num, color)


class Avoid(Card):
    def __init__(self, num, color, name=None):
        name = "avoid" if name is None else name
        Card.__init__(self, name, num, color)


class Peach(Card):
    def __init__(self, num, color, name=None):
        name = "peach" if name is None else name
        Card.__init__(self, name, num, color)


class Wine(Card):
    def __init__(self, num, color, name=None):
        name = "wine" if name is None else name
        Card.__init__(self, name, num, color)


if __name__ == '__main__':
    CARDS = [
        # 杀
        Kill(7, "spade"),
        Kill(8, "spade"),
        Kill(8, "spade"),
        Kill(9, "spade"),
        Kill(9, "spade"),
        Kill(10, "spade"),
        Kill(10, "spade"),
        Kill(4, "spade", "thunder_kill"),
        Kill(5, "spade", "thunder_kill"),
        Kill(6, "spade", "thunder_kill"),
        Kill(7, "spade", "thunder_kill"),
        Kill(8, "spade", "thunder_kill"),

        Kill(10, "hart"),
        Kill(10, "hart"),
        Kill(11, "hart"),
        Kill(3, "hart", "fire_kill"),
        Kill(7, "hart", "fire_kill"),
        Kill(10, "hart", "fire_kill"),

        Kill(2, "club"),
        Kill(3, "club"),
        Kill(4, "club"),
        Kill(5, "club"),
        Kill(6, "club"),
        Kill(7, "club"),
        Kill(8, "club"),
        Kill(8, "club"),
        Kill(9, "club"),
        Kill(9, "club"),
        Kill(10, "club"),
        Kill(10, "club"),
        Kill(11, "club"),
        Kill(11, "club"),
        Kill(5, "club", "thunder_kill"),
        Kill(6, "club", "thunder_kill"),
        Kill(7, "club", "thunder_kill"),
        Kill(8, "club", "thunder_kill"),

        Kill(6, "diamond"),
        Kill(7, "diamond"),
        Kill(8, "diamond"),
        Kill(9, "diamond"),
        Kill(10, "diamond"),
        Kill(13, "diamond"),
        Kill(4, "diamond", "fire_kill"),
        Kill(5, "diamond", "fire_kill"),
        # 闪
        Avoid(2, "hart"),
        Avoid(2, "hart"),
        Avoid(8, "hart"),
        Avoid(9, "hart"),
        Avoid(11, "hart"),
        Avoid(12, "hart"),
        Avoid(13, "hart"),

        Avoid(2, "diamond"),
        Avoid(2, "diamond"),
        Avoid(3, "diamond"),
        Avoid(4, "diamond"),
        Avoid(5, "diamond"),

        Avoid(6, "diamond"),
        Avoid(6, "diamond"),
        Avoid(7, "diamond"),
        Avoid(7, "diamond"),
        Avoid(8, "diamond"),
        Avoid(8, "diamond"),
        Avoid(9, "diamond"),
        Avoid(10, "diamond"),
        Avoid(10, "diamond"),
        Avoid(11, "diamond"),
        Avoid(11, "diamond"),
        Avoid(11, "diamond"),

        Peach(3, "hart"),
        Peach(4, "hart"),
        Peach(5, "hart"),
        Peach(6, "hart"),
        Peach(6, "hart"),
        Peach(7, "hart"),
        Peach(8, "hart"),
        Peach(9, "hart"),
        Peach(12, "hart"),

        Peach(2, "diamond"),
        Peach(3, "diamond"),
        Peach(12, "diamond"),

        Wine(3, "spade"),
        Wine(9, "spade"),
        Wine(3, "club"),
        Wine(9, "club"),
        Wine(9, "diamond"),
    ]
    # li = ['role', 'address', 'arms', 'shield', 'horsePlus', 'horseReduce']
    # for i in li:
    #     print('self.{} = {}'.format(i, i))
    n = 0
    for c in CARDS:
        if c.name == "peach":
            n += 1
    print(n)
    print(len(CARDS))
