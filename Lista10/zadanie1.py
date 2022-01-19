import math

class Kolo:
    def __init__(self, promien: float):
        self.r = promien
    
    def pole(self) -> float:
        return math.pi * self.r**2
    
    def obwod(self) -> float:
        return 2 * math.pi * self.r

if __name__ == "__main__":
    k = Kolo(5)
    print(k.obwod())
    print(k.pole())