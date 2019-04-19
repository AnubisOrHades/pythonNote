from Socket.database.myDB import MysqlClients

from Socket.ITTS.settings import *


class Client:
    def __init__(self, sobj, m):
        self.id = m.id
        self.type = m.type
        self.socketObj = sobj
        self.message = m

    tags = MysqlClients(db=DATABASE, p=PASSWORD)

    def heartbeat(self, cl):
        """
        处理心跳反应
        :param m: 客户端发送的数据
        :return:
        """
        if self.type == "device":
            online = []
            deviceId = self.id

            # 获取设备详情
            d = self.tags.select("product_shanlaidevice", "deviceId", deviceId)[0]
            print(d)
            # 获取设备版本号
            vId = d[4]
            # 设备版本号为空添加设备版本号
            if vId is None:
                # 查询版本号是否存在
                eId = self.tags.select("product_shanlaiedition", "editionName", self.message.data.get("version"),
                                       "id")  # [0][0]

                # 版本号存在
                if len(eId) != 0:
                    pass
                else:
                    # 版本号不存在，创建新的版本号
                    self.tags.insert(tableName="product_shanlaiedition", editionName=self.message.data.get("version"))

                # 获取创建版本号id
                eId = self.tags.select("product_shanlaiedition", "editionName", self.message.data.get("version"))[0][0]
                print("版本id：", eId)
                # 将版本号添加到设备
                self.tags.updata("product_shanlaidevice", "deviceEdition_id", eId, "id", d[0])


            # 修改设备版本号
            else:
                # 查询版本号是否存在
                eId = self.tags.select("product_shanlaiedition", "editionName", self.message.data.get("version"),
                                       "id")  # [0][0]

                # 版本号存在
                if len(eId) != 0:
                    if eId[0][0] == d[4]:
                        pass
                    else:
                        self.tags.updata("product_shanlaidevice", "deviceEdition_id", eId[0][0], "id", d[0])

                else:
                    # 版本号不存在，创建新的版本号
                    self.tags.insert(tableName="product_shanlaiedition", editionName=self.message.data.get("version"))
                    # 获取创建版本号id
                    eId = \
                        self.tags.select("product_shanlaiedition", "editionName", self.message.data.get("version"))[0][
                            0]
                    print("版本id：", eId)
                    # 将版本号添加到设备
                    self.tags.updata("product_shanlaidevice", "deviceEdition_id", eId, "id", d[0])
            # 修改设备状态
            self.tags.updata("product_shanlaidetails", "deviceState", self.message.data.get("state"), "deviceInfo_id",
                             d[0])
            # 获取设备房间Id
            roomId = d[6]
            # 获取房间的所有用户Id
            # result = tags.select("SELECT user_id FROM testdb.user_user_room WHERE room_id=%s" % roomId)

            result = self.tags.select("user_user_room", "room_id", roomId, key2="user_id", )
            for user in result:
                # 获取用户的userId
                # userId = tags.select("SELECT userName FROM testdb.user_user WHERE id=%s" % user[0])[0][0]

                userId = self.tags.select("user_user", "id", user[0], key2="userName")[0][0]
                print(userId)
                # 获取用户的socket对象
                if cl.get(userId) is None:
                    pass
                else:
                    online.append(cl.get(userId))
            print(online)
            if len(online) == 0:
                self.message.responseResult = "NO"
                self.message.resultCode = "11000"
            else:
                for shoujiSocket in online:
                    if shoujiSocket is not None:
                        shoujiSocket.socketObj.send(self.message.result(shoujiSocket.id, d=self.message.data))
        elif self.type == "tel":
            if self.message.notificationHolder:
                pass

        self.socketObj.send(self.message.result())
        print("心跳已处理")
