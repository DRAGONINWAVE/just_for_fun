import numpy as np


def thornthwaite(T, P):
    # T: average monthly temperature (°C)
    # P: average monthly precipitation (mm)
    T = T + 273.15
    n = len(T)
    ET = np.zeros(n)
    for i in range(n):
        if T[i] <= 273.15:
            ET[i] = 0.0
        else:
            ET[i] = 16 * ((10 * T[i] / I[i]) - T[i] / 5 - 17)
    return ET


def calc_evaporation(T, P):
    # T: average monthly temperature (°C)
    # P: average monthly precipitation (mm)
    I = calc_heat_index(T)
    ET = thornthwaite(T, P)
    return np.sum(ET) / 12.0


def calc_heat_index(T):
    # T: average monthly temperature (°C)
    I = np.zeros(len(T))
    for i in range(len(T)):
        I[i] = T[i] * T[i] * T[i] * T[i]
    return np.sum(I) / 12.0


# Example
T = [5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0]
P = [100.0, 90.0, 80.0, 70.0, 60.0, 50.0, 40.0, 30.0, 20.0, 10.0, 5.0, 0.0]

evaporation = calc_evaporation(T, P)
print("Annual Evaporation: {:.2f} mm".format(evaporation))
