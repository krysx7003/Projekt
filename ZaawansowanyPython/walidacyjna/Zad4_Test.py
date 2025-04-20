import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import główna.Zad4 as zad4

poly1 = zad4.Polynomial(3)
poly2 = zad4.Polynomial(5)

poly1[0] = 1
poly1[1] = 2
poly1[2] = 3

poly2[4] = 5
poly2[2] = 3

print(f"Wielomian 1: {poly1}")
print(f"Wielomian 2: {poly2}")

print( f"Współczynnik 0 {poly1[0]}" )
print( f"Współczynnik 1 {poly1[1]}" )
print( f"Współczynnik 2 {poly1[2]}" )

poly3 = poly1 + 2

print(f"Wielomian 3: {poly3}")

poly4 = poly3 + poly2
print(f"Wielomian 4(Wiel 2 + 3): {poly4}")
poly5 = poly1 + poly3
print(f"Wielomian 5(Wiel 1 + 3): {poly5}")