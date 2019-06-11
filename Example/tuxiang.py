import cv2


def look_photo():
    # 接收两个参数，一个是文件名，一个值，如果值为1，接收的是彩色图片，如果值为零，接受的是灰度图片。会有一个返回值，表示返回的图片内容
    img = cv2.imread('img/l.jpg', 1)

    # 接收两个参数，一个是窗体名称，另一个是要显示的内容
    cv2.imshow('mashiro', img)

    # 将程序暂停，只有这样，才能看到图片,否则图片会一闪而过因为程序结束了，如果time.sleep()的话，会卡住
    cv2.waitKey(0)


def make_photo(path=""):
    """
    控制摄像头拍照
    :return:
    """
    # 打开默认摄像头
    cap = cv2.VideoCapture(0)
    while 1:
        ret, fram = cap.read()
        if ret:
            # 弹出摄像头窗口
            cv2.imshow("photo", fram)
            # 当按“q”键时退出窗口并拍照
            if cv2.waitKey(1) & 0xFF == ord("q"):
                # 保存相片
                cv2.imwrite(path+"photo.jpg", fram)
                break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    make_photo()
