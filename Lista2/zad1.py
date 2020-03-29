"""Zadanie 1 lista_2"""
import sys
import os
import re


def file_info(name):
    """Funkcja wyswietlajaca informacje o pliku"""
    words = 0
    lines = 0
    max_line = 0

    stat_info = os.stat(name)
    file = open(name)
    for line in file:
        data = re.sub('[,\'\".!?]', '', line)
        data = data.split()
        if len(line) > max_line:
            max_line = len(line)
        words += len(data)
        lines += 1

    print("liczba bajtów:", stat_info.st_size)
    print("liczba słów:", words)
    print("liczba linii:", lines)
    print("maksymalna długość linii:", max_line)


file_info(sys.argv[1])
