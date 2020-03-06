# funkcja fraczero(n) liczącą silnie n! dla n od 0 do 10000 oraz jako wynik wraca liczbę zer na końcu n!
n = int(input("Podaj liczbe naturalna: "))

def fraczero(n):
    factorial =1
    result = 0
    for i in range(1, n+1):
        factorial *= i
    
    while(factorial%10 == 0):
        result += 1
        factorial = factorial // 10

    return result

print(fraczero(n))