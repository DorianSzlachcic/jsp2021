import cmath

a = int(input("Podaj czesc rzeczywista liczby: "))
b = int(input("Podaj czesc urojona liczby: "))
z = complex(a ,b)

modZ = abs(z)
print(modZ)
argZ = cmath.phase(z)
print(argZ)
print(z.conjugate())
