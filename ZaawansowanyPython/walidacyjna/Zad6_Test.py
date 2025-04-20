import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import główna.Zad6 as zad6

car1 = zad6.Car("Toyota","Corolla",2008,500000,50000)

print(car1)

car1.drive(10000)

print(car1)

car1.calculate_depreciation(2020)

print(car1)

# car1.mileage = -100 # ValueError: Mileage cannot be negative.