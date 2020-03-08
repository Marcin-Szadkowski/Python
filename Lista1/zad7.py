#Program dopasowujacy slowa z listy do wzorca

L = ['aababacaa', 'cabaabcca', 'aaabbcbacb', 'acababbaab', 'accabbbbb']
pattern = "a**a******"

def matcher(pattern, list):
    result = []
    dict = {}

    for i in range(0, len(pattern)):
        if pattern[i].isalpha():
            dict[i] = pattern[i]
            
    for word in list:
        for indeks in dict:
            if word[indeks] != pattern[indeks]:
                break
        else:
            result.append(word)
    return result
 
print(matcher(pattern, L))