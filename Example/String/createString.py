import random


# 生成邀请码
def random_username(n=10):
    username = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789-_'
    length = len(chars) - 1
    for index in range(n):
        username += chars[random.randint(0, length)]
    return username


if __name__ == '__main__':
    s = random_username(8)
    print(s)
