import json
from flask import request


class Request(object):
    def __init__(self):
        self._request = request
        form = dict(request.form)
        data = json.loads(request.data)
        if len(form) != 0:
            param = form
        elif len(data) != 0:
            param = data
        else:
            param = None
        self.param = param
        self.headers = dict(request.headers)
        print(self.headers)

    def header(self):
        try:
            if self.headers.get("host") != "127.0.0.1:5000":
                return "host error!"
            pass
        except Exception as e:
            print("Error:{}".format(e))
        else:
            pass
        finally:
            pass

    def __str__(self):
        return ""

    pass


class Result(object):
    def __init__(self):
        self.code = 400
        self.message = None
        self.data = []
        pass

    def json(self):
        return json.dumps({"code": self.code, "message": self.message, "data": self.data})

    def __str__(self):
        return ""

# param = Param()
