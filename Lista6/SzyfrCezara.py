klucz = 5

def szyfruj(tekst):
    s = ""
    for t in tekst:
        tInt = ord(t)
        if tInt >= 65 and tInt <= 90:
            tInt += klucz
            if tInt > 90:
                tInt -= 26
            s += chr(tInt)
        elif tInt>=97 and tInt<=122:
            tInt += klucz 
            if tInt > 122:
                tInt -= 26
            s += chr(tInt)
        else:
            s += t

    return s

def odszyfruj(tekst):
    s = ""
    for t in tekst:
        tInt = ord(t)
        if tInt >= 65 and tInt <= 90:
            tInt -= klucz
            if tInt < 65:
                tInt += 26
            s += chr(tInt)
        elif tInt>=97 and tInt<=122:
            tInt -= klucz 
            if tInt < 97:
                tInt += 26
            s += chr(tInt)
        else:
            s += t

    return s
