
#Trojkat Pascala
def pascal_triangle(n):
    tab=[]
    for i in range(n):
        tab.append([])
        tab[i].append(1)
        for j in range(1, i):
            tab[i].append(tab[i-1][j-1]+tab[i-1][j])
            
        tab[i].append(1)
    for i in range(n):
        print("   "*(n-i), end=" ")
        for j in range(0, i+1):
            print('{0:5}'.format(tab[i][j]), end=" ")
        print()

n=int(input("Enter number of rows: "))

pascal_triangle(n)