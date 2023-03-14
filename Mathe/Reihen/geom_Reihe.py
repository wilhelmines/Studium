#Skript zum Berechnen der geometrischen Reihe

import time

q = input('Welcher Wert soll für q verwendet werden?')
k = 0.0
s = 0.0

timeout = input('Für wie viele Sekunden soll das Skript ausgeführt werden?')  # [seconds] Dauer in der 2.0 erreicht wird: 0.0049

timeout_start = time.time()

while time.time() < timeout_start + timeout:
    s_temp = q**k
    k += 1
    s += s_temp
    print(s)