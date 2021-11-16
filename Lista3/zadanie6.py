x = int(input("Podaj liczbe i: "))

for i in range(1,x+1):
    s = ""
    for j in range(1,11):
        s += str(i*j)+"\t"
    print(s)
