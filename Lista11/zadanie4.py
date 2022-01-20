import re

def znajdzWyrazy(tekst: str, literaPoczatkowa: str) -> list:
    pattern = "["+literaPoczatkowa.lower() + literaPoczatkowa.upper() +"][a-zA-Z0-9]+[ ,.]?"
    return re.findall(pattern, tekst)

print(znajdzWyrazy("Ala ma kota","a"))