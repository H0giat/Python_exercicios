#bmenor (base menor)
#Bmaior (base maior)
import math
h=float(input("Digite a altura: "))
B=float(input("Digite a base maior: "))
b=float(input("Digite a base menor: "))
volume=h/3*(B**2+b**2+B*b)
print("O volume é: ", volume)
