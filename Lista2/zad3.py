"""Zadanie 3 lista_2"""
import os
import sys


def change_names(path):
    """Funkcja zmieniajaca nazwy plikow na nazwy z malymi literami"""
    for root, dirs, files in os.walk(path):
        for f in files:
            os.rename(os.path.join(root, f), os.path.join(root, f.lower()))


try:
    change_names(sys.argv[1])
except OSError:
    print("Nie udalo sie wykonac operacji")
