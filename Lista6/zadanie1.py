import trojkat as t

a = float(input("Podaj bok a: "))
b = float(input("Podaj bok b: "))
c = float(input("Podaj bok c: "))

if t.czyToTrojkat(a,b,c):
    print("Obwód trojkata = "+str(t.obwodTrojkata(a,b,c)))
    print("Pole trojkata = "+str(t.poleTrojkata(a,b,c)))
    print("Ten trojkat jest " + t.sprawdzBoki(a,b,c) + " oraz " + t.sprawdzKaty(a,b,c))
else:
    print("To nie jest trojkat")