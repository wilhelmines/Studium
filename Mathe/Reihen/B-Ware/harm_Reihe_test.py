# Berechnung der harmonischen Reihe
import time
import numpy as np

k = np.dtype(np.float128)
k = 1
s = np.dtype('float128')
s = 0
s_temp = np.dtype('float128')

timeout = 50   # [seconds]

timeout_start = time.time()

while time.time() < timeout_start + timeout:
    s_temp = 1/k
    k = k + 1
    s = s + s_temp
    print(s)