from apps import mysql_db, Request, Result


# 用户注册
def register():
    try:
        param = Request()
        result = Result()
        if not param.param:
            result.code = 202
            result.message = "参数错误"
            return result.json()

        mobile_phone = param.param.get('mobile_phone')
        psd = param.param.get('psd')

        sql = """INSERT INTO flask_test.user (name, psd, mobile_phone) value ('{}','{}','{}')""".format(
            mobile_phone, psd, mobile_phone)
        print(sql)
        mysql_db.execute(sql)

    except Exception as e:
        result.code = 202
        result.message = "注册失败"
        print("Error:{}".format(e))
    else:
        result.code = 200
        result.message = "注册成功"
        return result.json()
        pass
    finally:
        pass
