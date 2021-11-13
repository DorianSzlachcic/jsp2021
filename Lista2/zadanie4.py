a = input("Podaj napis: ")

a = a[0]+a[1:len(a)].replace(a[0],'$')
print(a)