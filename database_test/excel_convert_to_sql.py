import pymongo
import pandas as pd

# 连接数据库
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["national_weather_station"]
mycol = mydb["national_weather_station"]

# 读取数据和对数据变量赋名
data = pd.read_fwf(r"D:\piles\evp.txt", header=None)
data.columns = ['站点', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'ET', 'H', 'I']
data = data.set_index("站点")

# 输入数据

x = mycol.insert_many(data)
