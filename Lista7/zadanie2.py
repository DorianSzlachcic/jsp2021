import random
import time

def sortowanieWstawianie(a: list) -> list:
    l = a
    for i in range(len(l)):
        pom = l[i]
        j = i-1
        
        while j>=0 and l[j]>pom :
                l[j+1] = l[j]
                j -= 1
        l[j+1] = pom
    return l

#100 elementow
l100 = []
for i in range(100):
    l100.append(random.randint(0,20))

start = time.time()

print(sortowanieWstawianie(l100))

stop = time.time()
print("Czas trwania: "+str(stop-start) + "s")

#200 elementow
l200 = []
for i in range(200):
    l200.append(random.randint(0,20))

start = time.time()

print(sortowanieWstawianie(l200))

stop = time.time()
print("Czas trwania: "+str(stop-start) + "s")

#300 elementow
l300 = []
for i in range(300):
    l300.append(random.randint(0,20))

start = time.time()

print(sortowanieWstawianie(l300))

stop = time.time()
print("Czas trwania: "+str(stop-start) + "s")