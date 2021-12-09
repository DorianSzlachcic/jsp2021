import math

def obwodTrojkata(a: float, b: float, c: float) -> float:
    return a + b + c

def poleTrojkata(a: float, b: float, c: float) -> float:
    p = obwodTrojkata(a,b,c) / 2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))

def sprawdzBoki(a: float, b: float, c: float) -> str:
    if a == b and b == c and c == a:
        return "Rownoboczny"
    elif a == b or b == c or c == a:
        return "Rownoramienny"
    else:
        return "Roznoboczny"

def sprawdzKaty(a: float, b: float, c: float) -> str:
    ab = math.sqrt(a**2 + b**2)
    bc = math.sqrt(b**2 + c**2)
    ca = math.sqrt(c**2 + a**2)

    if ab==c or bc==a or ca==b:
        return "Prostokatny"
    elif ab>c and bc>a and ca>b:
        return "Ostrokatny"
    else:
        return "Rozwartokatny"

def czyToTrojkat(a: float, b: float, c: float) -> bool:
    return (a + b > c) and (b + c > a) and (c + a > b)
