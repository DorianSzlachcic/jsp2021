import itertools as it

class A:
    def __init__(self, l: list) -> None:
        self.l = l
    
    def podlisty(self) -> list:
        p = []

        for x in it.combinations(self.l,3):
            if sum(x) == 0:
                p.append(list(x))

        return p

if __name__ == "__main__":
    a = A([1,2,3,-3,-2,-1])
    print(a.podlisty())