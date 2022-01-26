

from unittest import result


class CiagArytmetyczny:
    def __init__(self, a1: float, r: float, n: int) -> None:
        self.a1 = a1
        self.r = r
        self.n = n
    
    def zapisz_do_pliku(self, nazwa_pliku: str) -> None:
        with open(nazwa_pliku, "a") as file:
            for i in self:
                file.write(str(i)+"\n")

    def __iter__(self):
        self.i = 0
        return self
    
    def __next__(self):
        if self.i < self.n:
            res = self.a1 + self.i * self.r
            self.i += 1
            return res
        else:
            raise StopIteration
    
    def __len__(self):
        return self.n


if __name__ == "__main__":
    c = CiagArytmetyczny(1,1,10)
    c.zapisz_do_pliku("ciag.txt")
    print("Zapisano do pliku!")

    print("Iterowanie w petli for: ")
    for i in c:
        print(i)
    
    print("Dlugosc obiektu: ")
    print(len(c))