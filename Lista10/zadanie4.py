import xml.etree.ElementTree as ET

class Kursy:
    def __init__(self, filePath) -> None:
        self.filePath = filePath
        try:
            tree = ET.parse(filePath)
        except Exception as e:
            print(e)
            exit()
        self.root = tree.getroot()

    def lista(self) -> list:
        lista = []
        for x in self.root:
            d = {child.tag: child.text for child in x}
            lista.append(d)
        return lista
    
    def konwertuj_na_PLN(self, kwota: float, kod_waluty: str) -> float:
        for x in self.lista():
            if x["kod_waluty"] == kod_waluty:
                return kwota * (float(x["kurs_sredni"].replace(",","."))/float(x["przelicznik"]))
    
    def konwertuj_z_PLN(self, kwota: float, kod_waluty: str) -> float:
        for x in self.lista():
            if x["kod_waluty"] == kod_waluty:
                return (kwota / float(x["kurs_sredni"].replace(",","."))) * float(x["przelicznik"])

    def konwertuj(self, kwota: float, kod_waluty1: str, kod_waluty2: str) -> float:
        return self.konwertuj_z_PLN(self.konwertuj_na_PLN(kwota, kod_waluty1), kod_waluty2)

if __name__ == "__main__":
    k = Kursy("kursy.xml")
    print(k.konwertuj_z_PLN(k.konwertuj_na_PLN(100, "EUR"),"EUR"))
    print(k.konwertuj(100, "EUR", "CZK"))
