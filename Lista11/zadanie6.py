

class CiagArytmetyczny:
    def __init__(self, a1: float, r: float, n: int) -> None:
        self.a1 = a1
        self.r = r
        self.n = n
    
    def zapisz_do_pliku(self, nazwa_pliku: str) -> None:
        with open(nazwa_pliku, "a") as file:
            for i in range(self.n):
                file.write(str(self.a1 + (self.r*i))+"\n")


if __name__ == "__main__":
    c = CiagArytmetyczny(1,1,10)
    c.zapisz_do_pliku("ciag")