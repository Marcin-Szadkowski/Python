"""Zadanie 5 lista_2"""
import random
import math
import re
import sys

PUBLIC_KEY = "key.pub"
PRIVATE_KEY = "key.prv"


def is_prime(n):
    """Implementacja Miller-Rabin Test"""
    if n == 2 or n == 3:
        return True
    elif n <= 1 or n % 2 == 0:
        return False
    k = 100  # liczba prob
    d = n - 1
    r = 0
    while d & 1 == 0:
        d //= 2
        r += 1
    for i in range(0, k):
        random_number = random.randrange(2, n - 2)
        x = pow(random_number, d, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < r and x != n - 1:
                x = pow (x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n -1:
                return False
    return True


def generate_prime(keysize):
    """Funkcja generujaca liczbe pierwsza o podanej liczbie bitow"""
    while True:
        num = random.getrandbits(keysize)
        if is_prime(num):
            return num


def mod_inverse(a, m):
    m0 = m
    y = 0
    x = 1

    if m == 1:
        return 0

    while a > 1:
        q = a // m

        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t

    if x < 0:
        x = x + m0

    return x


def generate_keys(keysize):
    # Generujemy dwie duze liczby pierwsze p i q
    p = generate_prime(keysize)
    q = generate_prime(keysize)
    # Obliczamy n
    n = p * q

    # Generujemy wykladnik kodujacy
    minimum = 2 ** 16 + 1
    fi = (p - 1) * (q - 1)
    if minimum >= fi:
        minimum = 2 ** (keysize - 1)
    while True:
        e = random.randrange(minimum, fi)
        if math.gcd(e, fi) == 1:
            break

    # Obliczamy wykladnik dekodujacy
    d = mod_inverse(e, fi)

    file_public = open(PUBLIC_KEY, "w+")
    file_private = open(PRIVATE_KEY, "w+")

    file_public.write(str(n) + "\n")
    file_public.write(str(e))
    file_private.write(str(n) + "\n")
    file_private.write(str(d))

    file_private.close()
    file_public.close()


def encrypt(msg):
    """Funkcja kodujaca"""
    file = open(PUBLIC_KEY)
    public_key = file.read()
    public_key = public_key.split()

    n = int(public_key[0])
    e = int(public_key[1])
    for char in msg:
        print(pow(ord(char), e, n), sep="", end=" ")
    print()
    file.close()


def decrypt(msg):
    """Funkcja dekodujaca"""
    file = open(PRIVATE_KEY)
    private_key = file.read()
    private_key = private_key.split()

    n = int(private_key[0])
    d = int(private_key[1])
    msg = msg.split()

    if len(msg) == 1:
        print(chr(pow(int(msg[0]), d, n)))
    else:
        for number in msg:
            print(chr(pow(int(number), d, n)), sep='', end='')
    print()
    file.close()


try:
    if sys.argv[1] == "--encrypt":
        encrypt(sys.argv[2])
    elif sys.argv[1] == "--decrypt":
        decrypt(sys.argv[2])
    elif sys.argv[1] == "--gen-keys":
        generate_keys(int(sys.argv[2]))
except IOError:
    pass

