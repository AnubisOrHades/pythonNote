import os
import sys
import traceback

from moviepy.editor import VideoFileClip
import cv2

from tools.file import File


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
    if not os.path.exists(path):
        print("Error：{} 不存在".format(path))
        return 0
    vc = cv2.VideoCapture(path)

    if vc.isOpened():
        real, frame = vc.read()
        img_path = "{}\\{}.{}".format(img_path, video_name, img_format)
        if os.path.exists(img_path):
            print("Error：{} 已存在".format(img_path))
            return 0
        # cv2.imwrite(img_path, frame) #中文路径乱码
        cv2.imencode(".{}".format(img_format), frame)[1].tofile(img_path)
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


def get_video_attribute(filename):
    """
    获取视频属性
    :param filename: 视频时长（单位：秒/s）
    :return: 视频时长
    """
    clip = VideoFileClip(filename)
    video = {
        "duration": clip.duration,  # 时长
        "size": clip.size,  # 尺寸
        "fps": clip.fps,  # 码率（每秒帧数）
        "filename": clip.filename  # 名字
    }
    clip.close()
    # clip.reader.close()
    # clip.audio.reader.close_proc()
    return video


def de_watermark(file_path, x, y, w, h, out_path=None):
    """
    去除视频水印
    :param file_path: 文件完整地址
    :param x: 水印位置x坐标
    :param y: 水印位置y坐标
    :param w: 水印宽度
    :param h: 水印高度
    :param out_path:文件输出路径
    :return:
    """
    try:
        in_file = File(file_path)
        old_name = in_file.name
        print(old_name)
        in_file.re_name("in")
        in_path = "{}\\in{}".format(in_file.path, os.path.splitext(in_file.local_path)[1])
        if out_path is None:
            out_path = "{}\\out{}".format(in_file.path, os.path.splitext(in_file.local_path)[1])
        else:
            out_path = "{}\\out{}".format(out_path, os.path.splitext(in_file.local_path)[1])
        try:
            os.system("ffmpeg -i {} -vf delogo=x={}:y={}:w={}:h={} {}".format(in_path, x, y, w, h, out_path))
            pass
        except Exception as e:
            exc_type, exc_value, exc_traceback_obj = sys.exc_info()
            traceback.print_tb(exc_traceback_obj)
            File(in_path).re_name(old_name)
            print("Error:{}".format(e))
        else:
            File(in_path).re_name(old_name)
            File(out_path).re_name(old_name)
            pass
        finally:
            pass
        pass
    except Exception as e:
        exc_type, exc_value, exc_traceback_obj = sys.exc_info()
        traceback.print_tb(exc_traceback_obj)
        print("Error:{}".format(e))
    else:
        pass
    finally:
        pass


if __name__ == '__main__':
    pass
