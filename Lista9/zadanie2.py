from os import sep
import sys, os, stat
import numpy as np

mode = os.fstat(sys.stdin.fileno()).st_mode
if stat.S_ISREG(mode):

    data = [float(x) for x in sys.stdin.read().split(sep="\n") if x.isdecimal()]
    
    print("Average: " + str(np.average(data)))
    print("Variance: " + str(np.var(data)))
    print("Standard Deviation: " + str(np.std(data)))

elif len(sys.argv) > 1:
    arg = sys.argv
    arg.pop(0)

    for a in arg:
        data = [float(x) for x in a.split(sep=",")]

        print("Average: " + str(np.average(data)))
        print("Variance: " + str(np.var(data)))
        print("Standard Deviation: " + str(np.std(data)))
else:
    print("Missing arguments")