import random
import numpy as np

#6 zufallszahlen
def lotto():
    i = 0
    a = np.arange(1,46)
    zz = []
    while i < 6:
        randomz = random.randint(a[0], a[44-i])
        a[randomz-1], a[44 - i] = a[44 - i], a[randomz-1]
        zz.append(a[44-i])

        i = i + 1

    return zz


#statistik mit dicts
def dict_lotto():
    dict = {}
    for i in range(1,46):
        dict[i]=0
    for i in range(0,1000):
        dict[int(random.random()*45+1)]+=1

    return dict


print("Lottoziehung: " + str(lotto()) + "\nStatistik: "+ str(dict_lotto()))
