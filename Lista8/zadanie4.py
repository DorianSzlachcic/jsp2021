from os import execle


def walidacjaPESEL(pesel: str) -> bool:
    if len(pesel) == 11:
        wagi = [1,3,7,9,1,3,7,9,1,3]
        
        k = pesel[10]
        pesel = pesel[0:10]

        suma = 0
        for i in range(10):
            suma += int(pesel[i]) * wagi[i]
        
        suma = str(10 - (suma%10))

        return k == suma[len(suma)-1]
    else:
        return False

def dataUrodzenia(pesel: str) -> str:
    dzien = pesel[4:6]
    miesiac = int(pesel[2:4])

    if miesiac > 80:
        miesiac -= 80
        rok = "18" + pesel[0:2]
    elif miesiac > 60:
        miesiac -= 60
        rok = "22" + pesel[0:2]
    elif miesiac > 40:
        miesiac -= 40
        rok = "21" + pesel[0:2]
    elif miesiac > 20:
        miesiac -= 20
        rok = "20" + pesel[0:2]
    else:
        rok = "19" + pesel[0:2]
    
    return rok + "-" + str(miesiac) + "-" + dzien

def plec(pesel: str) -> str:
    p = ["kobieta", "mezczyzna"]
    return p[int(pesel[9])%2]

try:
    readFile = open("PESEL.txt","r")
    pesele = readFile.read().split("\n")
    readFile.close()

    toSave = ""
    for pesel in pesele:
        if walidacjaPESEL(pesel):
            toSave += "nr "+pesel+":\n data urodzenia "+ dataUrodzenia(pesel) + "\t plec: " + plec(pesel) + "\n"
        else:
            toSave += "nr "+pesel+":\n Nieprawidlowy PESEL\n"
    
    try:
        saveFile = open("PESEL.txt","w")
        saveFile.write(toSave)
        saveFile.close()
    except:
        print("Blad zapisu do pliku")
except FileNotFoundError:
    print("Plik nie istanieje")
except:
    print("Nie można otworzyc pliku")