import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import główna.Zad1 as zad1

time1 = zad1.Time(22,33)
time2 = zad1.Time(11,11)
time3 = zad1.Time(9,50)
time4 = zad1.Time(25,00)
time5 = zad1.Time(21,70)

time_list = [time1,time2,time1]

print(time_list)

time_list.sort()

print(time_list)

time_list.append(time4)
time_list.append(time5)

for time in time_list:
    if time.isValid():
        print(f"Czas {time} jest poprawny")
    else:
        print(f"Czas {time} jest niepoprawny")

time6 = time1 + time2
print(f"{time1} + {time2} = {time6}")

time7 = time2 + time3
print(f"{time2} + {time3} = {time7}")
