import time

# 获取当前时间 返回时间戳
t = time.time()
print(t)
# 获取元组形式的时间戳
time_tuple = time.localtime(t)
print(time_tuple)
# 格式化时间戳
now_time=time.asctime(time_tuple)
print(now_time)
# 格式化时间戳
now_time = time.strftime('%Y-%m-%d %H:%M:%S', time_tuple)
print(now_time)

t = "2017-11-24 17:30:00"
#将其转换为时间数组
timeStruct = time.strptime(t, "%Y-%m-%d %H:%M:%S")
print(timeStruct)
#转换为时间戳:
timeStamp = time.mktime(timeStruct)
print(timeStamp)