#Program konwertujacy liczby rzymskie na arabskie


def converter(num):
    symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V','IV','I']
    values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    result = 0
    i =0
    s =0
    while s < len(num):
        if num[s] == symbols[i]:
            result += values[i]
            s += 1
        elif (len(num) - s >= 2) and (num[s] + num[s+1]) == symbols[i+1]:
                i +=1
                result += values[i]
                i +=1
                s += 2
        else:
            i += 2
    return result     

number = input("Podaj liczbe rzymska: ")
print(converter(number))