# Berechnung der Fourier Reihe
import time

k = 1
s = 0

timeout = 60   # [seconds]

timeout_start = time.time()

while time.time() < timeout_start + timeout:
    s_temp = 1/k**2
    k = k + 1
    s = s + s_temp
    print(s)