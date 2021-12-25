import random

def generujPesel() -> str:
    d30 = [4,6,9,11]

    rok = random.randrange(1800,2300)
    miesiac = random.randrange(1,13)

    if miesiac == 2:
        if rok % 4 == 0:
            dzien = random.randrange(1,30)
        else:
            dzien = random.randrange(1,29)
    elif miesiac in d30:
        dzien = random.randrange(1,31)
    else:
        dzien = random.randrange(1,32)

    if rok//100 == 18:
        miesiac += 80
    elif rok//100 == 20:
        miesiac += 20
    elif rok//100 == 21:
        miesiac += 40
    elif rok//100 == 22:
        miesiac += 60
    
    if len(str(dzien))==1 and len(str(miesiac))==1:
        pesel = str(rok)[2:4] + "0" + str(miesiac) + "0" + str(dzien)
    elif len(str(dzien))==1:
        pesel = str(rok)[2:4] + str(miesiac) + "0" + str(dzien)
    elif len(str(miesiac))==1:
        pesel = str(rok)[2:4] + "0" + str(miesiac) + str(dzien)
    else:
        pesel = str(rok)[2:4] + str(miesiac) + str(dzien)
    
    pppp = str(random.randrange(10000))
    
    while len(pppp) < 4:
        pppp = "0" + pppp
    
    pesel += pppp

    wagi = [1,3,7,9,1,3,7,9,1,3]

    k = 0
    for i in range(10):
        k += int(pesel[i]) * wagi[i]
    
    k = str(10 - (k%10))

    pesel += k[len(k)-1]

    return pesel



try:
    file = open("PESEL.txt","w")

    toSave = ""
    for i in range(10):
        toSave += generujPesel() + "\n"
    
    file.write(toSave)
    file.close()
except:
    print("Blad zapisu do pliku")