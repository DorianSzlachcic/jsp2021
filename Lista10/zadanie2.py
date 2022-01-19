import itertools as it

class A:
    def __init__(self, l: list) -> None:
        self.l = l
    
    def podlisty(self) -> list:
        p = [[]]
        for i in range(1,len(self.l)+1):
            p.extend([list(x) for x in it.combinations(self.l,i)])

        return p


if __name__ == "__main__":
    a = A([1,2,3])
    print(a.podlisty())