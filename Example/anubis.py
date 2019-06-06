def get_password(password):
    password = bin(password)[2:]
    print(password)
    return password


if __name__ == '__main__':
    class GrayCode:
        def getGray(self, n):
            # write code here
            global maxn
            maxn = n
            return GrayCode.getGrace(self, ['0', '1'], 1)

        def getGrace(self, list_grace, n):
            global maxn
            if n >= maxn:
                return list_grace
            list_befor, list_after = [], []
            for i in range(len(list_grace)):
                list_befor.append('0' + list_grace[i])
                list_after.append('1' + list_grace[-(i + 1)])
            return GrayCode.getGrace(self, list_befor + list_after, n + 1)


    # gary = GrayCode()
    # print("脚本之家测试结果：")
    # print(gary.getGray(3))

