import redis


class RedisClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = redis.Redis(host=host, port=port)


if __name__ == '__main__':
    host = "localhost"
    port = 6379
    r = redis.Redis(host=host, port=port)

    for i in range(100):
        r.set(i+1000, i+1)
        # name = r"D:\service\APP\test\{}.txt".format(int(r.get(i)) * 10+10)
        # with open(name, "w")as f:
        #     f.write(str(i))
        #
        # print(r.get(i))
