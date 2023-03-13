# Berechnung der harmonischen Reihe mit Hilfe der Py-Bibliothek numpy
import time
import numpy as np
import cupy as cp

k = cp.array([1])
s = cp.array([0])
s_temp = cp.array([0])
a = cp.array([1])

timeout = 10   # [seconds]

timeout_start = time.time()

while time.time() < timeout_start + timeout:
    s_temp = cp.divide(a, k)
    k = cp.add(k, a)
    s = cp.add(s, s_temp)
    print(s)