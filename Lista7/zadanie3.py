import random
import time

def sortowanieBabelkowe(a: list) -> list:
    l = a
    
    for i in range(len(l)):
        for j in range(1,len(l)-i):
            if l[j-1] > l[j]:
                l[j-1],l[j] = l[j], l[j-1]

    return l


#100 elementow
l100 = []
for i in range(100):
    l100.append(random.randint(0,20))

start = time.time()
print(sortowanieBabelkowe(l100))
stop = time.time()
print("Czas trwania: "+str(stop-start) + "s")

#200 elementow
l200 = []
for i in range(200):
    l200.append(random.randint(0,20))

start = time.time()
print(sortowanieBabelkowe(l200))
stop = time.time()
print("Czas trwania: "+str(stop-start) + "s")

#300 elementow
l300 = []
for i in range(300):
    l300.append(random.randint(0,20))

start = time.time()
print(sortowanieBabelkowe(l300))
stop = time.time()
print("Czas trwania: "+str(stop-start) + "s")