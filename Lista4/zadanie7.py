import math

def dwumianNewtona(n,k):
    if n==k or k==0:
        return 1
    else:
        return int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))

def trojkatPascala(n):
    trojkat = []
    for i in range(n+1):
        row = []
        for j in range(i+1):
            row.append(dwumianNewtona(i,j))
        trojkat.append(row)
    return trojkat


print(trojkatPascala(10))