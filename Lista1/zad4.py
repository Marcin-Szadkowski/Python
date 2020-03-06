#Program rozkladajace liczbe na czynniki pierwsze

n = int(input("Podaj liczbe naturalna: "))

def prime_factors(n):
    result = []

    if n ==1:
        return [1 ,1]
    for i in range(2, n+1):
        #Sprawdzamy czy i dzieli n
        if (n % i) == 0:
            k =0
            #Sprawdzamy w takim razie czy i jest pierwsze
            for j in range (2, i):
                if (i % j) == 0:
                    break
            else: #Jest pierwsza, wiec rozkladamy dalej
                k += 1
                n = n/i
                while( n % i == 0):
                    n =n/i
                    k += 1
                result.append([i, k])
    return result

print(prime_factors(n))
