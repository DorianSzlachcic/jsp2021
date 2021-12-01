def szyfr(text,type="szyfruj"):
    klucz={"a" : "y","e" : "i","i" : "o","o" : "a","y" : "e"}
    s = ""
    
    if type == "odszyfruj":
        klucz = {v: k  for k,v in klucz.items()}

    for t in text:
        if t in klucz.keys():
            s += klucz[t]
        else:
            s += t
    
    return s

print(szyfr("ta jist maj tikst", "odszyfruj"))
