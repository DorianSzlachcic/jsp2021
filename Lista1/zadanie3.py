import math

a = int(input("Podaj liczbe a: "))
b = int(input("Podaj liczbe b: "))
alpha = int(input("Podaj kat w stopniach: "))

pole = a*b*math.sin(math.radians(alpha))
print(pole)
