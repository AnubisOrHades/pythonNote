import json

from Example.Android.command import *
from Example.Android.nikki.devices_info import devices_set


def import_data(path='../nikki.json'):
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


class Nikki:
    def __init__(self, android):
        self.android = android
        pass

    def free(self):
        try:
            click(self.android["free"][0], self.android["free"][1])
            time.sleep(1)
        except Exception as e:
            print(e)
        else:
            pass
        finally:
            pass

    def _click(self, fun, spot):
        """
        获取点的坐标
        :param fun: 模块
        :param spot: 点
        :return: 点的坐标
        """
        click(self.android[fun][spot][0], self.android[fun][spot][1])
        pass

    def go_break(self):
        try:
            click(self.android["break"][0], self.android["break"][1])
        except Exception as e:
            print(e)
        else:
            pass
        finally:
            pass

    def house_of_mystery(self):
        try:
            self._click("house_of_mystery", "door")
            self._click("house_of_mystery", "magical")
            self.free()
            self.free()
            time.sleep(2)
            self._click("house_of_mystery", "cancel")
            self._click("house_of_mystery", "right")
            for i in range(4):
                self._click("house_of_mystery", "mystery")
                # time.sleep(1.5)
                self.free()
                self.free()
                self.free()
                self.free()
                self.free()

        except Exception as e:
            print(e)
        else:
            pass
        finally:
            self.go_break()

    def union(self):
        try:
            self._click("union", "door")
            self._click("union", "library")
            for i in range(3):
                self._click("union", "cleared")
                self.free()
            else:
                self.go_break()

        except Exception as e:
            print(e)
        else:
            pass
        finally:
            self.go_break()

    def dream(self):
        try:
            self._click("dream", "door")

            self._click("dream", "go_tasks")

            for t in self.android["dream"]["tasks"]:
                click(t[0], t[1])
                self._click("dream", "enter")
                self._click("dream", "free")
                self._click("dream", "free")

            self._click("dream", "break")

            self._click("dream", "islands")
            self._click("dream", "explore")
            time.sleep(2)
            self.free()
            self.free()
            self.go_break()

        except Exception as e:
            print(e)
        else:
            pass
        finally:
            self.go_break()

    def garden(self):
        for palace in self.android["garden"]["palace"]:
            try:
                slide(800, 1100, 200, 1100, 300)
                self._click("garden", "door")

                click(palace[0], palace[1])

                self._click("garden", "task1")
                self._click("garden", "third")
                self.free()
                self.free()
                self._click("garden", "free")
                self._click("garden", "task2")
                self._click("garden", "third")
                self.free()
                self.free()
                self._click("garden", "free")

                self._click("garden", "change")
                self._click("garden", "go_one")

                self._click("garden", "task1")
                self._click("garden", "third")
                self.free()
                self.free()
                self._click("garden", "free")
                self._click("garden", "task2")
                self._click("garden", "third")
                self.free()
                self.free()
                self._click("garden", "free")
            except Exception as e:
                print(e)
            else:
                pass
            finally:
                self.go_break()

    def sports(self):
        try:
            self._click("sports", "door")

            for i in range(5):
                self._click("sports", "stage")
                time.sleep(1.5)
                self._click("sports", "quick")
                time.sleep(1)
                self.free()
                self.free()

        except Exception as e:
            print(e)
        else:
            pass
        finally:
            self.go_break()

    def cabana(self):
        try:
            self._click("cabana", "door")

            time_start = "2020-04-11 01:12:12"
            start = time.mktime(time.strptime(time_start, "%Y-%m-%d %H:%M:%S"))
            s = (time.time() - start) // 60 // 60 // 24
            if s % 2 == 0:
                self._click("cabana", "wish")
                self._click("cabana", "long")

                for i in self.android["cabana"]["task"]:
                    click(i[0], i[1])
                    self._click("cabana", "wishing")
                    self.free()
                    self.free()
                    self._click("cabana", "cancel")
                    self.go_break()
                else:
                    self.go_break()

            for i in self.android["cabana"]["stroll"]:
                click(i[0], i[1])
            for i in range(6):
                self._click("cabana", "visit")
                time.sleep(1)
            else:
                self.go_break()
        except Exception as e:
            print(e)
        else:
            pass
        finally:
            self.go_break()

    def furniture(self):
        try:
            self._click("furniture", "door")
        except Exception as e:
            print(e)
        else:
            pass
        finally:
            pass

    def shopping(self):
        try:
            self._click("shopping", "door")
            self._click("shopping", "clothe")
            self._click("shopping", "buy")
            for i in range(3):
                self._click("shopping", "add")

            self._click("shopping", "buy_enter")
        except Exception as e:
            print(e)
        else:
            pass
        finally:
            self.go_break()

    def design_center(self):
        try:
            self._click("design_center", "door")
            self._click("design_center", "decompose_door")
            for i in range(4):
                self._click("design_center", "clothe")
            self._click("design_center", "decompose")
            self._click("design_center", "decompose_enter")
            for i in range(6):
                time.sleep(0.5)
                self.free()
        except Exception as e:
            print(e)
        else:
            pass
        finally:
            self.go_break()

    def judges(self):
        try:
            self._click("judges", "door")
            self._click("judges", "vote_door")
            for i in range(35):
                self._click("judges", "vote")
                self.free()
            else:
                self.go_break()
        except Exception as e:
            print(e)
        else:
            pass
        finally:
            self.go_break()

    def open_judges_box(self, num=10):
        """
        打来评选赛盒子
        :param num: 盒子数量
        :return:
        """
        for i in range(num):
            self._click("judges", "box")

    def change_clothe(self, clothe):
        """
        换衣服(单件)
        :param clothe: 衣服名字
        :return:
        """
        # 搜索
        self._click("change_clothes", "search")
        # 获取焦点
        self._click("change_clothes", "focus")
        # 输入衣服名
        input_abd(clothe)
        # 完成输入enter
        self._click("change_clothes", "enter")
        self._click("change_clothes", "choice")

    def change_clothes(self, clothe):
        """
        换衣服，可以是单件，也可以是多件
        :param clothe: 衣服名字：单件类型str，多件类型tuple或list
        :return:
        """
        if isinstance(clothe, str):
            self.change_clothe(clothe)
        elif isinstance(clothe, tuple) or isinstance(clothe, list):
            for c in clothe:
                self.change_clothe(c)

    def change_suit(self, suit):
        """
        更换套装
        :param suit: 套装，tuple或list
        :return:
        """
        self._click("change_clothes", "door")
        self._click("change_clothes", "clear")
        self.change_clothes(suit)
        self._click("change_clothes", "save")

    def main(self):
        # 迷之屋
        self.house_of_mystery()
        print("迷之屋	完成！！！".center(100, "="))
        # 搭配师联盟
        self.union()
        print("搭配师联盟	完成！！！".center(100, "="))
        # 织梦人学会
        self.dream()
        print("织梦人学会	完成！！！".center(100, "="))
        # 御苑琼芳
        self.garden()
        print("御苑琼芳	完成！！！".center(100, "="))
        # 搭配竞技场
        self.sports()
        print("搭配竞技场	完成！！！".center(100, "="))
        # 小屋
        self.cabana()
        print("小屋	完成！！！".center(100, "="))
        # 服装店
        self.shopping()
        print("服装店	完成！！！".center(100, "="))
        # 设计工坊
        self.design_center()
        print("设计工坊	完成！！！".center(100, "="))
        # 搭配评选赛
        self.judges()
        print("搭配评选赛	完成！！！".center(100, "="))


if __name__ == '__main__':
    n = Nikki(devices_set["magic_20"])
    n.main()
