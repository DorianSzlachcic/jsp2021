def rgb2hsv(r,g,b):
    r = r/255
    g = g/255
    b = b/255

    xmax = max(r,g,b)
    xmin = min(r,g,b)
    c = xmax-xmin
    v = xmax

    if c==0:
        h = 0
    elif v == r:
        h = 60 * (0+(g-b)/c)
    elif v == g:
        h = 60 * (2+(b-r)/c)
    elif v == b:
        h = 60 * (4+(r-g)/c)
    
    if v == 0:
        s = 0
    else:
        s = (c/v)*100
    
    v = v*100

    return h,s,v

print(rgb2hsv(31,52,29))