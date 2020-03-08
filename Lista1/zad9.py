#Kalkulator
from math import *

formula = input("Policz: ")
formula = formula.replace('^', '**')
        
print(eval(formula))