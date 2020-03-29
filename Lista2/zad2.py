"""Zadanie 2 lista_2"""
import sys
TAB = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'


def encode(output_name, input_name):
    """Funkcja koduje plik kodowaniem Base64"""
    file_read = open(input_name)
    file_write = open(output_name, "wb")
    bits = ""

    for line in file_read:
        for char in line:
            bits += '{0:08b}'.format(ord(char))

    chunks = [bits[index: index + 6] for index in range(0, len(bits), 6)]

    for chunk in chunks:
        file_write.write(TAB[int(chunk, 2)].encode())
    file_read.close()
    file_write.close()
    print("Zakodowano plik: ", input_name)


def decode(input_name, output_name):
    """Funkcja dekoduje plik zakodowany Base64"""
    file_read = open(input_name, "rb")
    file_write = open(output_name, "w")
    bits = ""

    letters = list(file_read.read())

    for letter in letters:
        bits += '{0:06b}'.format(TAB.index(chr(letter)))
    chunks = [bits[index: index + 8] for index in range(0, len(bits), 8)]

    for chunk in chunks:
        file_write.write(str(chr(int(chunk, 2))))

    file_read.close()
    file_write.close()
    print("Odkodowano plik:", input_name)


if sys.argv[1] == "--encode":
    encode(sys.argv[2], sys.argv[3])
elif sys.argv[1] == "--decode":
    decode(sys.argv[2], sys.argv[3])
