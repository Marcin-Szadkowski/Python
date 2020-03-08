#Program rysujacy wykres funkcji
import math
from math import *

tab = [[" " for x in range(0, 80)] for y in range(0, 24)]

for i in range(0, 80):
    tab[12][i] = "-"
for i in range(0, 24):
    tab[i][39] = "|"

func = input("Podaj funkcje f(x): ")
a = int(input("Podaj początek przedzialu: "))
b = int(input("Podaj koniec przedzialu: "))

#Obliczenie kroku poziomego
interval = (b-a)/80
x = a
#Obliczenie kroku pionowego
temp =[]
for i in range(0,80):
    temp.append(eval(func))
    x += interval

maxi = max(temp)
mini = min(temp)
k = max(abs(maxi), abs(mini))
step = (2 * k)/24

print(step)
#Narysowanie lewej strony wykresu
if(a < 0):
    x = 0
    for i in range(39, -1, -1):
    # print(eval(func)/step)
        j = math.ceil(eval(func)/step)  
        j = 12 - j
        if(j >23 ):
            j -= 1
        tab[j][i]= "*"
        x -= interval
#narysowanie prawej strony wykresu
x =0
for i in range(40, 80):
# print(eval(func)/step)
    j = math.ceil(eval(func)/step)  
    j = 12 - j
    if(j >23 ):
        j -= 1
    tab[j][i]= "*"
    x += interval
#Wyswietlenie tablicy jako wykres   
for i in range(0, 24):
    for j in range(0, 80):
        print(tab[i][j], end="", sep="")
    print()




