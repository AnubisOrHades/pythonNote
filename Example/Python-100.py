import time, datetime
from math import sqrt
from sys import stdout

def_dict = [
    {
        "1-10": [
            {"谁是小偷": "find_thief"},
            {"1、2、3、4、组成的三位数": "num_san"},
            {}

        ]
    },
    {
        "11-20": [
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
        ]
    },
    {
        "21-30": [
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
        ]
    },
    {
        "31-40": [
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
        ]
    },
    {
        "41-50": [
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
        ]
    },
    {
        "51-60": [
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
        ]
    },
    {
        "16-70": [
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
        ]
    },
    {
        "71-80": [
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
        ]
    },
    {
        "81-90": [
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
        ]
    },
    {
        "91-100": [
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
            {"": ""},
        ]
    },
]


def find_thief():
    for thief in ['a', 'b', 'c', 'd']:
        sum = (thief != 'a') + (thief == 'c') + (thief == 'd') + (thief != 'd')
        if sum == 3:
            print("小偷是：%s" % thief)


"""
Python 100例
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。

程序源代码
"""


def num_san():
    """
    打印[1,2,3,4]组成不同的三位数
    :return:
    """
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if (i != k) and (i != j) and (j != k):
                    print(i * 100 + j * 10 + k)


"""
题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，
从键盘输入当月利润I，求应发放奖金总数？

程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。

程序源代码：
"""


def bonus():
    i = int(input('净利润:'))
    arr = [1000000, 600000, 400000, 200000, 100000, 0]
    rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    r = 0
    for idx in range(0, 6):
        if i > arr[idx]:
            r += (i - arr[idx]) * rat[idx]
            print((i - arr[idx]) * rat[idx])
            i = arr[idx]
    print(r)


"""
题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
程序分析：
假设该数为 x。
1、则：x + 100 = n2, x + 100 + 168 = m2
2、计算等式：m2 - n2 = (m + n)(m - n) = 168
3、设置： m + n = i，m - n = j，i * j =168，i 和 j 至少一个是偶数
4、可得： m = (i + j) / 2， n = (i - j) / 2，i 和 j 要么都是偶数，要么都是奇数。
5、从 3 和 4 推导可知道，i 与 j 均是大于等于 2 的偶数。
6、由于 i * j = 168， j>=2，则 1 < i < 168 / 2 + 1。
7、接下来将 i 的所有数字循环计算即可。
程序源代码：
"""


def anwer():
    for i in range(1, 85):
        if 168 % i == 0:
            j = 168 / i
            if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
                m = (i + j) / 2
                n = (i - j) / 2
                x = n * n - 100
                print(x)


"""
题目：输入某年某月某日，判断这一天是这一年的第几天？
程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，
特殊情况，闰年且输入月份大于2时需考虑多加一天：
程序源代码：
"""


def nowDate():
    year = int(input('year:\n'))
    month = int(input('month:\n'))
    day = int(input('day:\n'))

    months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
    if 0 < month <= 12:
        sum = months[month - 1]
    else:
        print('data error')
    sum += day
    leap = 0
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        leap = 1
    if (leap == 1) and (month > 2):
        sum += 1
    print('it is the %dth day.' % sum)


"""
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，
然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。
程序源代码：
"""


def num_sort():
    l = []
    for i in range(3):
        x = int(input('integer:\n'))
        l.append(x)
    l.sort()
    print(l)


"""
题目：斐波那契数列。
程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：
0、1、1、2、3、5、8、13、21、34、……。
在数学上，费波那契数列是以递归的方法来定义：
"""


def fib_one(n):
    """

    :param n:
    :return: 第N个裴波那契数字
    """
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


def fib_two(n):
    if n == 1 or n == 2:
        return 1
    return fib_two(n - 1) + fib_two(n - 2)


def fib_three(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


"""
题目：将一个列表的数据复制到另一个列表中。
程序分析：使用列表[:]。
程序源代码：
"""


def copy_list():
    a = [1, 2, 3]
    b = a[:]
    print(b)


"""
题目：输出 9*9 乘法口诀表。
程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
程序源代码：
"""


def multiplication_table():
    for i in range(1, 10):
        print()
        for j in range(1, i + 1):
            print("%d*%d=%d" % (i, j, i * j), end="\t")


"""
题目：暂停一秒输出。
程序分析：使用 time 模块的 sleep() 函数。
程序源代码：
"""


def delay(n):
    myD = {1: 'a', 2: 'b'}
    for key, value in dict.items(myD):
        print(key, value)
        time.sleep(n)


"""
题目：暂停一秒输出，并格式化当前时间。
程序分析：无。
程序源代码：
"""


def delay_now(n):
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    time.sleep(n)

    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


"""
题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
程序分析：兔子的规律为数列1,1,2,3,5,8,13,21....
程序源代码：
"""


def rubbit():
    f1 = 1
    f2 = 1
    for i in range(1, 22):
        print('%12ld %12ld' % (f1, f2))

        if (i % 3) == 0:
            print()
            ''
        f1 = f1 + f2
        f2 = f1 + f2


"""
题目：判断101-200之间有多少个素数，并输出所有素数。
程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，
如果能被整除，则表明此数不是素数，反之是素数。 　　　　　
程序源代码：
"""


def prime_number(start, end):
    h = 0
    leap = 1
    for m in range(start, end):
        k = int(sqrt(m + 1))
        for i in range(2, k + 1):
            if m % i == 0:
                leap = 0
                break
        if leap == 1:
            print('%-4d' % m)
            h += 1
            if h % 10 == 0:
                print()
        leap = 1
    print('The total is %d' % h)


"""
题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。
程序源代码：
"""


def narcissistic_number():
    n = int(input("请输入最大范围"))
    while 1:
        if n <= 0:
            n = int(input("请输入正整数"))
        else:
            break
    for n in range(n):
        power = len(str(n))
        numList = []
        m = n
        for s in range(power):
            num = m % 10
            numList.append(num)
            if m == num:
                break
            m = m // 10

        sun = 0
        for num in numList:
            sun += num ** power
        if n == sun:
            print(n)


"""
题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
(1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
(2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
(3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。

程序源代码：
"""


def reduceNum(n):
    print('{} = '.format(n), )
    if not isinstance(n, int) or n <= 0:
        print('请输入一个正确的数字 !')
        exit(0)
    elif n in [1]:
        print('{}'.format(n))
    while n != 1:  # 循环保证递归
        for index in range(2, n + 1):
            if n % index == 0:
                n /= index  # n 等于 n/index
                n = int(n)
                if n == 1:
                    print(index)
                else:  # index 一定是素数
                    print('{} *'.format(index), )
                    break


"""
题目：利用条件运算符的嵌套来完成此题：
学习成绩>=90分的同学用A表示，
60-89分之间的用B表示，
60分以下的用C表示。

程序分析：程序分析：(a>b)?a:b这是条件运算符的基本例子。
程序源代码：
"""


def classification():
    score = int(input('输入分数:\n'))
    if score >= 90:
        grade = 'A'
    elif score >= 60:
        grade = 'B'
    else:
        grade = 'C'

    print('%d 属于 %s' % (score, grade))


"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""


def one():
    for i, v in enumerate(def_dict):
        print(i + 1, "\t\t", list(v.keys())[0])
    num = int(input("请输入选项>>>>>>>>"))
    return num


def two(num):
    value_second = def_dict[num - 1]["{}-{}".format(10 * (num - 1) + 1, 10 * num)]
    for i, v in enumerate(value_second):
        for index, value in v.items():
            print(i + 1, "\t\t", index, "\t\t", value)
    num2 = int(input("请输入选项>>>>>>>>"))
    value_third = list(value_second[num2 - 1].values())[0]
    eval('{}()'.format(value_third))
    print(value_third)
    exit = input("e:返回上一级\nee:返回主页\nb:终止程序")
    return exit


def run():
    num1 = one()
    exit = two(num1)
    while 1:
        if exit == "e":
            exit = two(num1)
        elif exit == "ee":
            num1 = one()
            exit = two(num1)
        elif exit == "b":
            break


if __name__ == '__main__':
    # run()
    narcissistic_number()
