from celery import shared_task
import time


@shared_task
def add():
    print("hello")
    with open(r"C:\Users\武晓涛\Desktop\celery.txt", "w")as f:
        f.write("celery")
    time.sleep(10)
    print("end")
    with open(r"C:\Users\武晓涛\Desktop\celery10.txt", "w")as f:
        f.write("celery")
    return 90


'celery worker -A drfc -l debug'
'celery worker -A demo -l debug'
'celery worker -A celerydemo -l debug'
