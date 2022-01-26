import re

def znajdzWyrazy(tekst: str, literaPoczatkowa: str) -> list:
    pattern = r"\b["+literaPoczatkowa.lower() + literaPoczatkowa.upper() +r"][a-zA-Z0-9]+\b"
    return re.findall(pattern, tekst)

tekst = "Ala ma kota i elementarz"

znalezione = []
znalezione.extend(znajdzWyrazy(tekst,"a"))
znalezione.extend(znajdzWyrazy(tekst,"e"))

print(znalezione)