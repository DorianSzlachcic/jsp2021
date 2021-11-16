parzyste = []

for i in range(100,401):
    jednosci = i%10
    pom = i//10
    dziesiatki = pom%10
    pom = pom // 10
    setki = pom%10

    if jednosci%2==0 and dziesiatki%2==0 and setki%2==0:
        parzyste.append(i)

print(parzyste)