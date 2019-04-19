from socketBase import Client
from database.myDB import MysqlClients


class Device(Client):
    # def __init__(self):
    #     Client.__init__()
    #     self.dbid = self.get_id()

    def get_id(self):
        tags = MysqlClients(db="testdb", p="111111")
        # 获取设备ID
        d = tags.select("product_shanLaidevice", "deviceId", self.id)
        return d

    def linkageOperation(self, cl):
        # 创建数据库连接
        tags = MysqlClients()
        # 获取设备ID
        d = tags.select("product_shanLaidevice", "deviceId", self.id)
        if len(d) == 0:
            self.message.responseResult = "NO"
            self.message.resultCode = "10005"
        else:
            # 获取触发码id
            data = ""
            if self.message.data.get("linkPara") is not None:
                cfmId = tags.select("device_operation_opterationtrigger", "triggerName",
                                    self.message.data.get("linkPara"), "id")[0][0]
                # 获取联动操作
                print("触发码id:", cfmId)
                cz = tags.select("device_operation_concern", "device_id", d[0][0])
                for c in cz:
                    if c[4] == cfmId:
                        caozuo = tags.select("device_operation_deviceOpteration",
                                             "id", c[3], "opterationName")
                        if len(caozuo) != 0:
                            data = caozuo[0][0]
                            self.socketObj.send(self.message.result(d={"opterationName": data}))
                            break
                else:
                    self.message.responseResult = "NO"
                    self.message.resultCode = "10005"
                    self.socketObj.send(self.message.result())

    def zhuanfa(self, cl):
        """
        设备转发手机
        :param cl:
        :return:
        """

        tags = MysqlClients()
        # 获取设备详情
        d = tags.select("product_shanLaidevice", "deviceId", self.id)[0]
        print("fangjianxiangqing\n",d)
        # 获取房间的所有拥有者
        db = tags.client()
        cursor = db.cursor()
        try:
            sql = "SELECT userName FROM user_user WHERE id IN " \
                  "(SELECT user_id FROM user_user_room WHERE room_id=%d)"%d[6]
            print(sql)
            cursor.execute(sql)  # 执行sql语句
            results = cursor.fetchall()
            for u in results:
                d = cl.get(u[0])
                if d is None:
                    self.message.responseResult = "NO"
                    self.message.resultCode = "11000"
                else:
                    d.socketObj.send(self.message.result(u[0], d=self.message.obj))
                    print("硬件发手机已完成")
                self.socketObj.send(self.message.result())
        except Exception as e:
            raise e
