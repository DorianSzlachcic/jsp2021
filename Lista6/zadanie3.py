N = 10

a = "1"
print(a)

i = 2
while i<=N:
    b = {}
    for x in a:
        if x in b:
            b[x] += 1
        else:
            b[x] = 1
    
    a = ""
    for k,v in b.items():
        a += str(v) + str(k)

    print(a)
    i += 1