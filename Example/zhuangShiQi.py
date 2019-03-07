import time


def decorator(fun):
    def warpper(*args, **kwargs):
        start = time.time()
        fun(*args, **kwargs)
        runtime = time.time() - start
        print(runtime)
    return warpper


@decorator
def do_something():
    for i in range(1000000):
        if i % 1999 == 0:
            print(i)


if __name__ == '__main__':
    do_something()
