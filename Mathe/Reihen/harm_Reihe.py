# Berechnung der harmonischen Reihe
import time

k = 1
s = 0.0

timeout = 1000   # [seconds]

timeout_start = time.time()

while time.time() < timeout_start + timeout:
    s_temp = 1/k
    k = k + 1
    s = s + s_temp
    print(s)