import math

a = int(input("Podaj czesc rzeczywista liczby: "))
b = int(input("Podaj czesc urojona liczby: "))
z = complex(a ,b)

modZ = math.sqrt(z.real**2 + z.imag**2)
print(modZ)
argZ = math.atan(z.imag/z.real)
print(argZ)
print(z.conjugate())