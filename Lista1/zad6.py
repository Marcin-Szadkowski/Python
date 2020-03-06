#Program generujacy 20 liczb losowych

import random

tab =[]

for i in range(20):
    x = random.randint(1, 100)
    tab.append(x)

print(tab)
print("Średnia wartosc w tablicy: ", sum(tab)/len(tab))
print("Maksymalna: ", max(tab))
print("Minimalna: ", min(tab))

mini = max(tab)
maxi = min(tab)
count =0

for i in tab:
    if i < mini and i != min(tab):
        mini = i
    if i > maxi and i != max(tab):
        maxi = i
    if i % 2 == 0:
        count +=1


print("Druga maksymalna: ", maxi)
print("Druga minimalna: ", mini)
print("Liczb parzystych: ", count)