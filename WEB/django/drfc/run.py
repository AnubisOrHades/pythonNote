import os


def runDjango(host='127.0.0.1', port="8000"):
    path = os.getcwd()  # 获取当前目录
    os.chdir(path)  # 切换到当前目录
    os.system("python manage.py runserver {}:{}".format(host, port))  # 命令行启动当前项目

"""cd WEB/django/drfc"""
"""python manage.py celery worker --loglevel=info"""
if __name__ == '__main__':
    runDjango()
