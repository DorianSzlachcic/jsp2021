a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))

if b > a:
    Z = b % a
else:
    Z = a % b

Z *= Z + 3

print(Z)