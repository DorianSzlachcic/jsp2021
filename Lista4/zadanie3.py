from math import pi

def convert(angle, type="d2r"):
    if type == "d2r":
        return angle*(pi/180)
    elif type == "r2d":
        return angle*(180/pi)

print(convert(90))