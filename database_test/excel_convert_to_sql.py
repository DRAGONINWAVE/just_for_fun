import pymongo
import pandas as pd
# import bson
# from bson.raw_bson import RawBSONDocument
# from sqlalchemy import create_engine

# 连接数据库

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["national_weather_station"]
mycol = mydb["national_weather_station"]
# engine = create_engine("mongodb://localhost:27017/")
# 读取数据和对数据变量赋名
data = pd.read_fwf(
    r"D:\piles\SURF_CLI_CHN_MUL_DAY-EVP-13240-201701.TXT", header=None, index=None)
data.columns = ['站点', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'ET', 'H', 'I']

print(data)
# data = data.dropna()
data = data.to_dict(orient="index")
print(len(data))
# data = list(data)
x = mycol.insert_one(data)
print(x)
