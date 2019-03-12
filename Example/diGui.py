lis = []


def calc(i, n):
    global lis
    if i < n:
        lis.append(i)
        return calc(i+1, n)
    else:
        return lis


s = calc(0, 100)
print(s)
