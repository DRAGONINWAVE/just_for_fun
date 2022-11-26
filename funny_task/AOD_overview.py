import xarray as xr
import pandas as pd
from pandas import HDFStore
# import h5py
# import xarray

# data = xr.open_dataset(r"E:\AOD_MYDIS\MYD04_3K.A2003001.0440.061.2018005041406.hdf")
# print(data['w3'])
# data = xr.open_dataset(r"E:\AOD_MYDIS\MYD04_3K.A2003001.0440.061.2018005041406.hdf")
# print(data)
file = HDFStore(
    r"E:\AOD_MYDIS\MYD04_3K.A2003001.0440.061.2018005041406.h5")
print(file)
# file = xr.open_dataset(
#     r"E:\AOD_MYDIS\MYD04_3K.A2003001.0440.061.2018005041406.hdf")
# print(file)

# h5py.run_tests()
