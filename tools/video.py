import os

from moviepy.editor import VideoFileClip
import cv2


def preview(video_name, video_path, img_path, video_format="mp4", img_format="jpg"):
    """
    生成视频预览图
    :param video_name: 视频名
    :param video_path: 视频路径
    :param img_path: 图片路径
    :param video_format: 视频格式
    :param img_format: 图片格式
    :return: 是否成功（1：成功；0：失败）
    """
    path = '{}\\{}.{}'.format(video_path, video_name, video_format)
    vc = cv2.VideoCapture(path)

    if vc.isOpened():
        real, frame = vc.read()
        cv2.imwrite("{}\\{}.{}".format(img_path, video_name, img_format), frame)
        cv2.waitKey(1)
        vc.release()
        return 1
    else:
        return 0


def compress_video(input_path=None, out_path=None, bitrate=500, ffmpeg_path=None):
    """
    视频压缩
    :param input_path:输入文件地址
    :param out_path:输出文件地址
    :param bitrate: 码率
    :param ffmpeg_path:ffmpeg所在地址
    :return:
    """
    try:
        if input_path is None and out_path is None:
            return False
        if not ffmpeg_path:
            ffmpeg_path = r"E:\WU\server\ffmpeg\bin"
        code = r"{}\ffmpeg -i {} -b:v {}k -bufsize {}k {}".format(ffmpeg_path, input_path, bitrate, bitrate, out_path)
        os.system(code)
    except Exception as e:
        print("Error:{}".format(e))
        return False
    else:
        return True
        pass


def get_video_times(filename):
    """
    获取视频时长
    :param filename: 视频时长（单位：秒/s）
    :return: 视频时长
    """
    clip = VideoFileClip(filename)
    video_time = clip.duration
    clip.close()
    # clip.reader.close()
    # clip.audio.reader.close_proc()
    return video_time
