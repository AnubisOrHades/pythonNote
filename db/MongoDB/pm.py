from pymongo import MongoClient

# 连接MongoDB
conn = MongoClient("localhost", 27017)
# 选择要使用的数据库，如果没有则创建
db = conn.MG
# 选择要使用的数据表，如果没有则创建
poetry = db.test

# 获取mongodb所有数据库名
dblist = conn.list_database_names()
# print(dblist)

# 获取数据库中的所有数据表
collist = db.list_collection_names()
# print(collist)

# 添加数据
# poetry.save({"时间":"2019/3/16"," 行为":"添加数据"})
# poetry.insert_one({"时间":"2019/3/16"," 行为":"添加数据"})

# 添加多条数据
# poetry.insert_many([{"时间": "2019/3/16", " 行为": "添加数据"}, {"时间": "2019/3/16", " 行为": "添加多条数据"}])

# 查询一条数据
# x = poetry.find_one()
# print(x)

# 查询所有数据
# for x in poetry.find():
#     print(x)

# 条件查询
# mydoc = poetry.find({" 行为": "添加数据"})
# for x in mydoc:
#     print(x)

# 返回指定条数记录
myresult = poetry.find().limit(3)
for x in myresult:
    print(x)