import time

def fibonacciIter(N: int) -> int:
    poprzedni = 1
    f = 1
    for i in range(2,N):
        f, poprzedni = poprzedni, f
        f += poprzedni
    return f

def fibonacciRek(N: int) -> int:
    if N <= 2:
        return 1
    else:
        return fibonacciRek(N-1) + fibonacciRek(N-2)

N = int(input("Podaj liczbe wyrazow: "))

start = time.time()

for i in range(1,N+1):
    print(fibonacciIter(i))

stop = time.time()
print("Czas trwania: "+str(stop-start) + "s")

start = time.time()

for i in range(1,N+1):
    print(fibonacciRek(i))

stop = time.time()
print("Czas trwania: "+str(stop-start) + "s")