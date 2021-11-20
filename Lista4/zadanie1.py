def suma(lista):
    s = 0
    for x in lista:
        s+=x
    return s

def iloczyn(lista):
    i = 1
    for x in lista:
        i *= x
    return i

a = [1,2,3,4]
print(suma(a))
print(iloczyn(a))