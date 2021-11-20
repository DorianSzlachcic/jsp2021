def silnia(n):
    if n>=0:
        if n==0 or n==1:
            return 1
        else:
            return n*silnia(n-1)
    else:
        return -1

print(silnia(2))