#Skript zum Berechnen der geometrischen Reihe

#Import der mathematischen Bibliothek
import time

q = 0.5
k = 0.0
s = 0.0

timeout = 0.0049   # [seconds] Dauer in der 20. erreicht wird

timeout_start = time.time()

while time.time() < timeout_start + timeout:
    s_temp = q**k
    k = k + 1
    s = s + s_temp
    print(s)