m = int(input("Podaj ilosc wierszy: "))
n = int(input("Podaj ilosc kolumn: "))
lista = []

for i in range(0,m+1):
    l = []
    for j in range(0,n+1):
        l.append(i*j)
    lista.append(l)

for i in range(0,m+1):
    print(lista[i])
