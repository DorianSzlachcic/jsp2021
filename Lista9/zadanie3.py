from statistics import multimode
import matplotlib.pyplot as plt
import numpy as np
import math

def odlegloscXPoCzasie(predkoscPoczatkowa: float, czas: float, kat: float) -> float:
    return predkoscPoczatkowa*czas*math.cos(np.deg2rad(kat))

def czasLotu(predkoscPoczatkowa: float, kat: float) -> float:
    return (2*predkoscPoczatkowa*math.sin(np.deg2rad(kat)))/9.81

def maxWysokosc(predkoscPoczatkowa: float, kat: float) -> float:
    return (predkoscPoczatkowa**2 * math.sin(np.deg2rad(kat))**2)/(2*9.81)

if __name__ == "__main__":
    V0 = float(input("Podaj predkosc poczatkowa: "))
    alpha = float(input("Podaj kat rzutu (w stopniach): "))

    print("Czas lotu: "+str(czasLotu(V0,alpha))+"s")
    print("Zasieg rzutu: "+str(odlegloscXPoCzasie(V0, czasLotu(V0, alpha),alpha))+"m")
    print("Maksymalna wysokosc: "+str(maxWysokosc(V0,alpha))+"m")

    t = np.linspace(0,czasLotu(V0,alpha))

    #Obliczamy skladowe predkosci od czasu
    Vx = np.linspace(V0*math.cos(np.deg2rad(alpha)),V0*math.cos(np.deg2rad(alpha)))
    Vy = V0*math.sin(np.deg2rad(alpha)) - np.multiply(9.81,t)

    #Tworzenie wykresu predkosci od czasu
    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('time [s]')
    ax1.set_ylabel('Vx [m/s]', color=color)
    ax1.plot(t,Vx, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()

    color = 'tab:blue'
    ax2.set_ylabel('Vy [m/s]', color=color)
    ax2.plot(t, Vy, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()

    #Obliczamy polozenia od czasu
    Sx = np.multiply(V0*math.cos(np.deg2rad(alpha)),t)
    Sy = np.multiply(V0*math.sin(np.deg2rad(alpha)),t) + np.multiply(-9.81/2,np.power(t,2))

    #Tworzenie wykresu polozenia od czasu
    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('time [s]')
    ax1.set_ylabel('Sx [m]', color=color)
    ax1.plot(t,Sx, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()

    color = 'tab:blue'
    ax2.set_ylabel('Sy [m]', color=color)
    ax2.plot(t, Sy, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()


    #Tworzenie wykresu toru ruchu
    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('Sx [s]')
    ax1.set_ylabel('Sy [m]', color=color)
    ax1.plot(Sx,Sy, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
    plt.show()