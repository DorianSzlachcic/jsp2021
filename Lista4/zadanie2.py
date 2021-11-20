def usunDuplikaty(lista):
    for x in lista:
        i = 0
        for y in lista:
            if x == y:
                i+=1
        
        if i > 1:
            for j in range(i-1):
                lista.remove(x)

a = [1,1,1,2,2,2,3,33,3,3,4,5,4,6,6]
usunDuplikaty(a)
print(a)