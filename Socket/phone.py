from socketBase import Client
from database.myDB import MysqlClients


class Tel(Client):
    # def deviceOperation(self, cl):
    #     if self.message.notificationHolder:
    #         online = []
    #         deviceId = self.message.data["id"]
    #         # 创建数据库连接
    #         tags = MysqlClients(db=DATABASE, p=PASSWORD)
    #         # 获取设备房间Id
    #         roomId = tags.select("product_shanlaidevice", "deviceId", deviceId, key2="deviceRoom_id")
    #         # 获取房间的所有用户Id
    #         result = tags.select("user_user_room", "room_id", roomId, key2="user_id")
    #         for user in result:
    #             userId = tags.select("user_user", "id", user[0], key2="userName")[0][0]
    #             print(userId)
    #             # 获取用户的socket对象
    #             online.append(cl.get(userId))
    #         print(online)
    #         if len(online) == 1:
    #             self.message.responseResult = "NO"
    #             self.message.resultCode = "11000"
    #         else:
    #             for shoujiSocket in online:
    #                 if shoujiSocket is not None:
    #                     shoujiSocket.socketObj.send(self.message.result(shoujiSocket.id, d=self.message.data))
    #     elif self.message.notificationHolder == "False":
    #         self.socketObj.send(self.message.result())
    #     else:
    #         deviceId = self.message.notificationHolder
    #         d = cl.get(deviceId)
    #         if d is None:
    #             self.message.responseResult = "NO"
    #             self.message.resultCode = "11000"
    #         else:
    #             d.socketObj.send(self.message.result(deviceId, d=self.message.data))
    #
    #     pass

    def deviceOperation(self, cl):
        sbId=self.message.data.get("id")
        d = cl.get(sbId)
        if d is None:
            self.message.responseResult = "NO"
            self.message.resultCode = "11000"
        else:
            d.socketObj.send(self.message.result(sbId, d=self.message.data))
            print("手机发硬件已完成")
        self.socketObj.send(self.message.result())
        pass
