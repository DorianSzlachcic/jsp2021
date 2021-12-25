import os
import datetime
import SzyfrCezara as sc

pathToFile = input("Podaj sciezke do pliku: ")

try:
    file = open(pathToFile,"r")

    key = int(input("Podaj klucz szyfrowania (1-10): "))
    assert(key in range(1,11))

    pathToSave = input("Podaj sciezke do zapisu pliku: ")
    saveFileName = f"plik_zaszyfrowany{key}_"+str(datetime.datetime.now().year)+str(datetime.datetime.now().month)+str(datetime.datetime.now().day) + ".txt"
    
    if os.path.exists(pathToSave) == False:
        os.makedirs(pathToSave, exist_ok=True)
    
    pathToSave = os.path.join(pathToSave,saveFileName)

    fileSave = open(pathToSave,"w")
    fileSave.write(sc.szyfruj(file.read(),key))

    fileSave.close()
    file.close()

except AssertionError:
    print("Podano zly klucz")
except FileNotFoundError:
    print("Nie mozna otworzyc pliku")
except:
    print("Cos poszlo nie tak, sprobuj ponownie")