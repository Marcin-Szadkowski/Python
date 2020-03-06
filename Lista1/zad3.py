#Program usuwajacy powtarzajace sie elementy z listy

list = [1,1,2,2,2,3,3,5,5,5,4,4,4,0]
print(list)

def reduce(list):
    for i in range(len(list)-1, -1, -1):
        for j in range(i-1, -1, -1):
            if list[i] == list[j]:
                del list[j]

reduce(list)
print(list)
    
