from pymongo import MongoClient

conn = MongoClient("localhost", 27017)

# db = conn.wulianwang
db = conn.mzitu

# sockLis = db.socketClient
sockLis = db.students
sockLis.update({"name": "伏尔泰"}, {"$set": {"age": "50"}})
for s in sockLis.find():
    for k, v in s.items():
        print(k, ":\t", v)

# sockLis.insert(
#     [
#         {
#             "id": "13699998888",
#             "name": "泰戈尔",
#             "age": "99",
#             "gender": ""
#         },
#     {
#             "id": "13677778888",
#             "name": "伏尔泰",
#             "age": "99",
#             "gender": ""
#         },
#     ]
# )

# sockLis.save(
#     {
#         "id": "1111",
#         "name": "aobama",
#         "age": 12,
#     }
# )

# sockLis.remove({"name": "aobama"})
