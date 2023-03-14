# Berechnung der Fourier Reihe
import time

k = 1
s = 0.0

timeout = input('Für wie viele Sekunden soll das Skript ausgeführt werden?')   # [seconds]

timeout_start = time.time()

while time.time() < timeout_start + timeout:
    s_temp = 1/k**2
    k += 1
    s += s_temp
    print(s)