# 引用 requests文件
import requests
# 下载地址
Download_addres = 'https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2/M2I3NXGAS.5.12.4/1980/01/MERRA2_100.inst3_2d_gas_Nx.19800101.nc4'
# 把下载地址发送给requests模块
f = requests.get(Download_addres)
# 下载文件
print(f)
