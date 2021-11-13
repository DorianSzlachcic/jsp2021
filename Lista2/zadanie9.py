import itertools as it
a = [[2,4,3],[1,5,6],[9],[7,9,0]]
a = list(it.chain.from_iterable(a))
print(a)