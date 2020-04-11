import time

import pygame
from mutagen.mp3 import MP3
from pymediainfo import MediaInfo


def mp3_duration(audio_path):
    """
    获取mp3文件时长
    :param audio_path: mp3文件地址
    :return: 时长（s）
    """
    try:
        audio = MP3(audio_path)
    except Exception as e:
        print("Error:{}".format(e))
    else:
        return audio.info.length
    finally:
        pass


def audio_duration(audio_path):
    """
    获取音频时长
    :param audio_path: 音频文件
    :return: 时长
    """
    try:
        media_info = MediaInfo.parse(audio_path)
        data = media_info.to_data()
        pass
    except Exception as e:
        print("Error:{}".format(e))
    else:
        return data["tracks"][0]["duration"] / 1000
    finally:
        pass


def audio_info(audio_path):
    """
    获取音频信息
    :param audio_path: 音频文件
    :return: 音频信息
    """
    try:
        media_info = MediaInfo.parse(audio_path)
        data = media_info.to_data()
        pass
    except Exception as e:
        print("Error:{}".format(e))
    else:
        return data
    finally:
        pass


def play_music(music_path):
    """
    播放音乐
    :param music_path: 音乐地址
    :return:
    """
    pygame.mixer.init()
    # 加载音乐
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play(start=0.0)
    # 播放时长，没有此设置，音乐不会播放，会一次性加载完
    time.sleep(audio_duration(music_path))
    pygame.mixer.music.stop()


if __name__ == '__main__':
    path = "../media/audio/go.mp3"
    play_music(path)
