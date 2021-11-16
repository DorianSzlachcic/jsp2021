litera = input("Podaj litere: ")

samogloski = ['a','e','i','o','u','y']
if(len(litera)==1):
    if litera in samogloski:
        print("Litera jest samogloska")
    else:
        print("Litera jest spolgloska")
else:
    print("Wprowadziles wiecej niz jedna litere")