from pymongo import MongoClient


class MongodbClient:
    def __init__(self, db=None, table=None, host="localhost", port=27017):
        """
        MongodbClient初始化函数
        :param db: 数据库名
        :param table: 数据库表名
        :param host: 数据库地址（ip），默认为 localhost
        :param port: 数据库端口，默认为 27017
        """
        self.host = host
        self.port = port
        self.db = db
        self.table = table
        self.content = self.get_content()

    def get_content(self):
        """
        获取连接对象
        :return: 获取连接对象
        """
        conn = MongoClient(self.host, self.port)
        db = conn[self.db]
        table = db[self.table]
        return table

    def select(self, n=None, **kwargs):
        """
        查询数据库
        :param n: 要返回数据的数量
        :param kwargs: 查询条件
        :return: 查询结果
        """
        if n == None:
            return self.content.find(kwargs)
        else:
            return self.content.find(kwargs).limit(n)

    def save(self, *args, **kwargs):
        """
        存储数据
        :param args: 多条数据
        :param kwargs: 一条数据
        :return:
        """
        print(list(args))
        if len(args) != 0 and len(kwargs.keys()) != 0:
            self.content.insert_many(list(args))
            self.content.save(kwargs)

        elif len(args) == 0:
            self.content.save(kwargs)
        elif len(kwargs.keys()) == 0:
            self.content.insert_many(list(args))
        else:
            print("没有要存入的数据")
        print(list(args))

    def delete(self, **kwargs):
        if self.select(**kwargs).count() > 0:
            data = self.select(**kwargs)[0]
            self.content.delete_one(data)
        else:
            print("没有数据")


if __name__ == '__main__':
    m = MongodbClient(db="MG", table="test")
    # for i in m.select(时间="2019/4/16", 行为="添加数据"):
    #     print(i)
    # m.save(时间="2019/4/16", 行为="添加数据")
    # m.save({"时间": "2019/4/16", "行为": "添加数据"}, {"时间": "2019/4/16", "行为": "添加多条数据"})

    m.delete(行为="添加数据")
