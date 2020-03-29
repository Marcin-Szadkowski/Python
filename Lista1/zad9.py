#Kalkulator
from math import *

formula = input("Policz: ")
formula = formula.replace('^', '**')
try:        
    print(eval(formula))
except SyntaxError:
    print("Podano zły argument funkcji")
except NameError:
    print("Nieznany parametr funkcji")