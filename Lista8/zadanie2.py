import os
import re
import datetime
import SzyfrCezara as sc

path = input("Podaj sciezke do folderu z plikami: ")

try:
    files = [f for f in os.listdir(path) if (re.search(r"plik_zaszyfrowany(.*).txt",f) != None) and os.path.isfile(os.path.join(path, f))]

    for f in files:
        key = int(re.search(r"[1-9][0]*",f).group(0))
        writeFileName = f"plik_odszyfrowany{key}_"+str(datetime.datetime.now().year)+str(datetime.datetime.now().month)+str(datetime.datetime.now().day) + ".txt"
        
        readFileName = os.path.join(path,f)
        writeFileName = os.path.join(path,writeFileName)

        try:
            readFile = open(readFileName,"r")
            writeFile = open(writeFileName,"w")

            writeFile.write(sc.odszyfruj(readFile.read(),key))

            readFile.close()
            writeFile.close()
        except FileNotFoundError:
            print("Nie mozna otworzyc pliku")

except FileNotFoundError:
    print("Podana sciezka nie istnieje")