def NWD(a,b):
    if a!=b:
        if a>b:
            return NWD(a-b,b)
        else:
            return NWD(a,b-a)
    else:
        return a

print(NWD(144,64))