#Program wypisujacy liczby pierwsze nie wieksze od n
n = int(input("Podaj n:"))

def primes(n):
    tab=[]
    for i in range (2, n+1):
        for j in range (2, i):
            if (i % j) == 0:
                break
        else:
            tab.append(i)

    return tab

print(primes(n))

