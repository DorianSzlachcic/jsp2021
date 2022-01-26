import re

def dodajSpacje(tekst: str) -> str:
    pattern = r"\b[A-Z][a-z]+[A-Z][a-z]+[ ,.]?"
    s = tekst
    while re.search(pattern, s):
        x = re.search(pattern, s).group(0)
        s = s.replace(x, x[:re.search(r"[a-z][A-Z]",x).span()[0]+1]+" "+re.search(r"[a-z][A-Z][a-z]+[ ,.]?",x).group(0)[1:])
    return s

print(dodajSpacje("AlaMa kota BardzoFajnego"))