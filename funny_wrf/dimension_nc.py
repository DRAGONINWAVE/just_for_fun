from __future__ import print_function

from netCDF4 import Dataset
from wrf import getvar

ncfile = Dataset(
    r"C:\Users\Administrator\Desktop\wrfout_d01_2016-10-06_00_00_00")

# Get the Sea Level Pressure
slp1 = getvar(ncfile, "slp")

ncfile2 = Dataset(
    r"C:\Users\Administrator\Desktop\wrfout_d01_2016-10-08_00_00_00")
slp2 = getvar(ncfile2, "slp")

print(slp1, '\n', slp2)
