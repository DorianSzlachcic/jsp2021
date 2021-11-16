import math

a = float(input("Podaj liczbe a: "))
b = float(input("Podaj liczbe b: "))
c = float(input("Podaj liczbe c: "))

if a != 0:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Rownanie nie ma rozwiazan rzeczywistych")
    elif delta == 0:
        x = (-b)/(2*a)
        print("Rownanie ma jedno rozwiazanie: x = " + str(x))
    else:
        x1 = (-b-math.sqrt(delta))/(2*a)
        x2 = (-b+math.sqrt(delta))/(2*a)
        print("Rozwiazania: x1 = " + str(x1) + "\nx2 = " + str(x2))
else:
    print("Rownanie nie jest kwadratowe")