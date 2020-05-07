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
            click(self.android["house_of_mystery"]["door"][0], self.android["house_of_mystery"]["door"][1])
            click(self.android["house_of_mystery"]["magical"][0], self.android["house_of_mystery"]["magical"][1])
            self.free()
            self.free()
            time.sleep(2)
            click(self.android["house_of_mystery"]["cancel"][0], self.android["house_of_mystery"]["cancel"][1])
            click(self.android["house_of_mystery"]["right"][0], self.android["house_of_mystery"]["right"][1])
            for i in range(4):
                click(self.android["house_of_mystery"]["mystery"][0], self.android["house_of_mystery"]["mystery"][1])
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
            click(self.android["union"]["door"][0], self.android["union"]["door"][1])
            click(self.android["union"]["library"][0], self.android["union"]["library"][1])
            for i in range(3):
                click(self.android["union"]["cleared"][0], self.android["union"]["cleared"][1])
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
            click(self.android["dream"]["door"][0], self.android["dream"]["door"][1])

            click(self.android["dream"]["go_tasks"][0], self.android["dream"]["go_tasks"][1])

            for t in self.android["dream"]["tasks"]:
                click(t[0], t[1])
                click(self.android["dream"]["enter"][0], self.android["dream"]["enter"][1])
                click(self.android["dream"]["free"][0], self.android["dream"]["free"][1])
                click(self.android["dream"]["free"][0], self.android["dream"]["free"][1])

            click(self.android["dream"]["break"][0], self.android["dream"]["break"][1])

            click(self.android["dream"]["islands"][0], self.android["dream"]["islands"][1])
            click(self.android["dream"]["explore"][0], self.android["dream"]["explore"][1])
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
        try:
            slide(800, 1100, 200, 1100, 300)
            click(self.android["garden"]["door"][0], self.android["garden"]["door"][1])

            click(self.android["garden"]["task1"][0], self.android["garden"]["task1"][1])
            click(self.android["garden"]["third"][0], self.android["garden"]["third"][1])
            self.free()
            self.free()
            click(self.android["garden"]["free"][0], self.android["garden"]["free"][1])
            click(self.android["garden"]["task2"][0], self.android["garden"]["task2"][1])
            click(self.android["garden"]["third"][0], self.android["garden"]["third"][1])
            self.free()
            self.free()
            click(self.android["garden"]["free"][0], self.android["garden"]["free"][1])

            click(self.android["garden"]["change"][0], self.android["garden"]["change"][1])
            click(self.android["garden"]["go_one"][0], self.android["garden"]["go_one"][1])

            click(self.android["garden"]["task1"][0], self.android["garden"]["task1"][1])
            click(self.android["garden"]["third"][0], self.android["garden"]["third"][1])
            self.free()
            self.free()
            click(self.android["garden"]["free"][0], self.android["garden"]["free"][1])
            click(self.android["garden"]["task2"][0], self.android["garden"]["task2"][1])
            click(self.android["garden"]["third"][0], self.android["garden"]["third"][1])
            self.free()
            self.free()
            click(self.android["garden"]["free"][0], self.android["garden"]["free"][1])
        except Exception as e:
            print(e)
        else:
            pass
        finally:
            self.go_break()

    def sports(self):
        try:
            click(self.android["sports"]["door"][0], self.android["sports"]["door"][1])

            for i in range(5):
                click(self.android["sports"]["stage"][0], self.android["sports"]["stage"][1])
                time.sleep(1.5)
                click(self.android["sports"]["quick"][0], self.android["sports"]["quick"][1])
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
            click(self.android["cabana"]["door"][0], self.android["cabana"]["door"][1])

            time_start = "2020-04-11 01:12:12"
            start = time.mktime(time.strptime(time_start, "%Y-%m-%d %H:%M:%S"))
            s = (time.time() - start) // 60 // 60 // 24
            if s % 2 == 0:
                click(self.android["cabana"]["wish"][0], self.android["cabana"]["wish"][1])
                click(self.android["cabana"]["long"][0], self.android["cabana"]["long"][1])

                for i in self.android["cabana"]["task"]:
                    click(i[0], i[1])
                    click(self.android["cabana"]["wishing"][0], self.android["cabana"]["wishing"][1])
                    self.free()
                    self.free()
                    click(self.android["cabana"]["cancel"][0], self.android["cabana"]["cancel"][1])
                    self.go_break()
                else:
                    self.go_break()

            for i in self.android["cabana"]["stroll"]:
                click(i[0], i[1])
            for i in range(5):
                click(self.android["cabana"]["visit"][0], self.android["cabana"]["visit"][1])
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
            click(self.android["furniture"]["door"][0], self.android["furniture"]["door"][1])
        except Exception as e:
            print(e)
        else:
            pass
        finally:
            pass

    def shopping(self):
        try:
            click(self.android["shopping"]["door"][0], self.android["shopping"]["door"][1])
            # time.sleep(0.5)
            click(self.android["shopping"]["clothe"][0], self.android["shopping"]["clothe"][1])
            # time.sleep(0.5)
            click(self.android["shopping"]["buy"][0], self.android["shopping"]["buy"][1])
            # time.sleep(0.5)
            for i in range(3):
                click(self.android["shopping"]["add"][0], self.android["shopping"]["add"][1])

            click(self.android["shopping"]["buy_enter"][0], self.android["shopping"]["buy_enter"][1])
        except Exception as e:
            print(e)
        else:
            pass
        finally:
            self.go_break()

    def design_center(self):
        try:
            click(self.android["design_center"]["door"][0], self.android["design_center"]["door"][1])
            click(self.android["design_center"]["decompose_door"][0],
                  self.android["design_center"]["decompose_door"][1])
            for i in range(4):
                click(self.android["design_center"]["clothe"][0], self.android["design_center"]["clothe"][1])
            click(self.android["design_center"]["decompose"][0], self.android["design_center"]["decompose"][1])
            click(self.android["design_center"]["decompose_enter"][0],
                  self.android["design_center"]["decompose_enter"][1])
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
            click(self.android["judges"]["door"][0], self.android["judges"]["door"][1])
            click(self.android["judges"]["vote_door"][0], self.android["judges"]["vote_door"][1])
            for i in range(35):
                click(self.android["judges"]["vote"][0], self.android["judges"]["vote"][1], 0.5)
                self.free()
            else:
                self.go_break()
        except Exception as e:
            print(e)
        else:
            pass
        finally:
            self.go_break()

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
