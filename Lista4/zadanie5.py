import itertools as it

def permutacje(lista):
    return list(it.permutations(lista))

print(permutacje([1,2,3]))