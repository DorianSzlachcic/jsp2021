a = input("Podaj napis: ")
a = a[0:(len(a)//2)] + "Python" + a[(len(a)//2):len(a)]
print(a)