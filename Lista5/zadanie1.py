import re

jednosci = ["jeden","dwa","trzy","cztery","piec","szesc","siedem","osiem","dziewiec"]
dziesiatki = ["dwadziescia","trzydziesci","czterdziesci","piecdziesiat"]
nastki = ["dziesiec","jedenascie","dwanascie","trzynascie","czternascie","pietnascie","szesnascie","siedemnascie","osiemnascie","dziewietnascie"]

slownie = input("Podaj liczbe z przedzialu (1-59) słownie: ")
liczba = ""

if re.search(r" ",slownie)==None:
    if slownie in jednosci:
        print(jednosci.index(slownie)+1)
    elif slownie in nastki:
        print(nastki.index(slownie)+10)
else:
    for d in dziesiatki:
        for j in jednosci:
            if re.search(d+" "+j, slownie):
                print((dziesiatki.index(d)+2)*10+(jednosci.index(j)+1))
