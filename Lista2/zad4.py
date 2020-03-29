"""Zadanie 4 lista_2"""
import hashlib
import sys
import os


def check_dir(path):
    """Funkcja zwracajaca takie same pliki"""
    files_info = []

    for root, dirs, files in os.walk(path):
        for file in files:
            files_info.append([os.path.join(root, file),
                               hashlib.md5(file.encode()).hexdigest(),
                               os.stat(os.path.join(root, file)).st_size])

    for info in range(len(files_info) - 1, -1, -1):
        k = 0
        if files_info[info] == ["", "", ""]:
            continue
        for chunk in range(info - 1, -1, -1):
            if files_info[info][1] == files_info[chunk][1]:
                if files_info[info][2] == files_info[chunk][2]:
                    if k == 0:
                        print(files_info[info][0])
                    print(files_info[chunk][0])
                    files_info[chunk] = ["", "", ""]
                    k += 1
        if k > 0:
            print("----------------------")


check_dir(sys.argv[1])
