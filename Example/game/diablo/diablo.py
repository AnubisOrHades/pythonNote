"""
暗黑3自动脚本
1.开局进入第二营地
2.开启小秘境
"""
import os
import threading

import keyboard

from Example.win.winInput import *
from tools.audio import play_music
from Example.game.diablo.settings import *

MIX_X = 1535
MIX_Y = 863

START = False


class Skills:
    def __init__(self, skills_type=None, skills_key=None, skill_sleep=None):
        self.skills_type = skills_type
        self.skills_key = skills_key
        self.skill_sleep = skill_sleep
        self.time_stare = False

    def auto_skills(self):
        while True:
            try:
                if self.skills_type == "mouse_click":
                    mouse_click()
                elif self.skills_type == "key":
                    key_input(self.skills_key)
                for i in range(self.skill_sleep):
                    if self.time_stare:
                        self.time_stare = False
                        break
                    else:
                        time.sleep(1)
                if not START:
                    break
            except Exception as e:
                print("Error:{}".format(e))
            else:
                pass
            finally:
                pass

    def clear_time(self):
        self.time_stare = True


class Role:
    LEFT_TOP = LEFT_TOP
    RIGHT_BOTTOM = RIGHT_BOTTOM
    path = os.getcwd()

    def __init__(self, *args):
        self.skills = args
        pass

    @classmethod
    def goto_caldeum(cls):
        """
        进入卡尔蒂姆
        :return:
        """
        # 打开大地图
        key_input("m")
        # 切换世界地图
        mouse_click((715, 99))
        # 选择卡尔蒂姆地图
        mouse_click((817, 415))
        # 选择秘密营地
        mouse_click((830, 630))
        print("角色已进入卡尔蒂姆秘密营地！")

    @classmethod
    def decompose(cls):
        box_x = int((cls.RIGHT_BOTTOM[0] - cls.LEFT_TOP[0]) / 9)
        box_y = int((cls.RIGHT_BOTTOM[1] - cls.LEFT_TOP[1]) / 6)
        start_xy = [int(cls.LEFT_TOP[0] + box_x / 2), int(cls.LEFT_TOP[1] + box_y / 2)]
        # print("({},{})\n{}".format(box_x, box_y, start_xy))
        print("decompose_start".center(100, "="))
        time.sleep(0.1)
        mouse_click(DECOMPOSE)
        time.sleep(0.1)
        for i in range(9):
            for j in range(6):
                mouse_click(start_xy)
                time.sleep(0.01)
                key_input("enter")
                time.sleep(0.01)
                key_input("enter")
                start_xy[1] += box_y
            start_xy[1] -= box_y * 6
            start_xy[0] += box_x
        else:
            print("decompose_end".center(100, "="))

    def auto_sate(self):
        for t in self.skills:
            threading.Thread(target=t.auto_skills).start()
            # keyboard.add_hotkey(t.skills_key, t.clear_time)

    def skills_run(self):
        global START
        START = False if START else True
        if START:
            threading.Thread(target=play_music, args=(r"../../../media/audio/go.mp3",)).start()
            self.auto_sate()
        else:
            threading.Thread(target=play_music, args=(r"../../../media/audio/stop.mp3",)).start()
            pass

    @classmethod
    def skill_stop(cls):
        global START
        START = False


def open_secret():
    """
    在卡尔蒂姆开启小秘境
    :return:
    """
    # 选择奈非天尖方碑
    mouse_click((100, 400))
    time.sleep(3)
    # 选择小秘境
    mouse_click((212, 230))
    # 打开小秘境
    mouse_click((218, 670))
    time.sleep(3)
    # 进入小秘境
    mouse_click((MIX_X // 2 - 150, MIX_Y // 2))
    # time.sleep(1)
    # mouse_click()
    print("小秘境已开启！")


if __name__ == '__main__':
    role = DIABLO_ROLE
    cyclone = Role(
        Skills("key", "1", role["one"]),
        Skills("key", "2", role["two"]),
        Skills("key", "3", role["three"]),
        Skills("key", "4", role["four"]),
        # Skills("mouse_click", None, 1)
    )
    keyboard.add_hotkey("0", Role.goto_caldeum)
    keyboard.add_hotkey("f8", cyclone.skills_run)
    keyboard.add_hotkey("f7", Role.decompose)
    keyboard.add_hotkey("t", cyclone.skill_stop)
    print("\n\n\n", "暗黑破坏神3自动脚本启动".center(100, "#"))

    keyboard.wait()
