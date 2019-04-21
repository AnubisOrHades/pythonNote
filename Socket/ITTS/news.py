import json

from Socket.ITTS.settings import STOPWORD


class Message:
    def __init__(self, obj):
        self.obj = obj
        self.id = obj.get("id")
        self.action = obj.get("action")
        self.messageId = obj.get("messageId")
        self.data = obj.get("data")

        self.uniqueId = obj.get("uniqueId")
        self.notificationHolder = obj.get("notificationHolder")

        self.type = "tel" if self.uniqueId is not None else "device"

        self.responseResult = "OK"
        self.resultCode = "20000"

    def result(self, id=None, act=None, d=None):
        data = {
            "id": self.id if id is None else id,
            "action": self.action + "Response" if act is None else act + "Response",
            "uniqueId": self.uniqueId,
            "notificationHolder": self.notificationHolder,
            "responseResult": self.responseResult,
            "resultCode": self.resultCode,
            "return": [] if d is None else d
        }
        if self.type == "tel":
            pass
        elif self.type == "device":
            del data["uniqueId"]
            del data["notificationHolder"]

        return (json.dumps(data) + STOPWORD).encode('utf8')
