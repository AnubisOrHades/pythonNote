import pymysql


class MysqlClients:
    def __init__(self, db="flask_test", host="127.0.0.1", user="root", password="111111", port=3306):
        """
        初始化MySQL连接
        :param db: 数据库名字
        :param host: 数据库地址
        :param user: 数据库用户名
        :param password: 数据库用户密码
        :param port: 数据库端口
        """
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.port = port

    def client(self):
        db = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            db=self.db,
            port=self.port,
            charset='utf8'
        )
        return db

    def select(self, tableName, key=None, value=None, key2="*"):
        """

        :param tableName: 数据库表名
        :param key: 查找依据的字段名
        :param value: 字段的值
        :param key2: 返回的字段
        :return:
        """
        db = self.client()
        cursor = db.cursor()
        try:
            if key is None and value is None:
                sql = "SELECT {} FROM {}.{}".format(key2, self.db, tableName)
            else:
                if type(value) == int:
                    pass
                else:
                    if value.isdigit():
                        pass
                    else:
                        value = "\'%s\'" % value

                sql = "SELECT {} FROM {}.{} WHERE {}={}".format(key2, self.db, tableName, key, value)
            print("查询：", sql)
            cursor.execute(sql)  # 执行sql语句
            results = cursor.fetchall()  # 获取查询的所有记录
            return results
        except Exception as e:
            raise e
        finally:
            db.close()

    def updata(self, tableName, key, value, key2, value2):
        db = self.client()
        cursor = db.cursor()
        try:
            if type(value) == int:
                pass
            else:
                if value.isdigit():
                    pass
                else:
                    value = "\'%s\'" % value
            if type(value2) == int:
                pass
            else:
                if value2.isdigit():
                    pass
                else:
                    value2 = "\'%s\'" % value2

            sql = "UPDATE {}.{} SET {}={} WHERE {}={}".format(self.db, tableName, key, value, key2, value2)
            print("更新：", sql)
            cursor.execute(sql)  # 执行sql语句
            db.commit()
        except Exception as e:
            db.rollback()
            raise e
        finally:
            db.close()

    def insert(self, tableName, **kwargs):
        db = self.client()
        cursor = db.cursor()
        try:
            keys = []
            values = []
            for k, v in kwargs.items():
                keys.append(k)
                values.append(v)
            if len(keys) > 1:
                keyLis = "("
                for k in keys:
                    keyLis += k
                    keyLis += ","
                keyLis = keyLis[:-1]

                keyLis += ")"
                print(keyLis)
                keys = keyLis
                values = tuple(values)
            else:
                keys = "(%s)" % keys[0]
                values = "(\'%s\')" % values[0]

            sql = "INSERT INTO {}.{} {}  VALUES {}".format(self.db, tableName, keys, values)
            # sql="INSERT INTO testdb.product_shanlaiedition (editionName)  VALUES ('1.2.34')"
            print("插入：", sql)
            cursor.execute(sql)  # 执行sql语句
            db.commit()
        except Exception as e:
            db.rollback()
            raise e
        finally:
            db.close()

    def execute(self, sql):
        """
        执行SQL语句
        :param sql: SQL语句
        :return: 结果
        """
        db = self.client()
        try:
            results = None
            cursor = db.cursor()
            cursor.execute(sql)  # 执行sql语句
            if "INSERT" in sql or "UPDATE" in sql or "insert" in sql or "update" in sql:
                db.commit()
            else:
                results = cursor.fetchall()
            pass
        except Exception as e:
            print("Error:{}".format(e))
        else:
            return results
            pass
        finally:
            db.close()
            pass
