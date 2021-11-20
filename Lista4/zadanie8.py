def sumaSzereguHarmonicznego(ileWyrazow):
    suma = 0
    for i in range(1, ileWyrazow):
        suma += 1/i
    return suma

print(sumaSzereguHarmonicznego(30))