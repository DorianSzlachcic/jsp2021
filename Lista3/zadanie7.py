def fib(numerWyrazu):
    if numerWyrazu == 0:
        return 0
    elif numerWyrazu == 1 or numerWyrazu == 2:
        return 1
    else:
        return fib(numerWyrazu-1)+fib(numerWyrazu-2)

N = int(input("Podaj N: "))

for x in range(0,N+1):
    print(str(fib(x)))