import math
valorprestacao=float(input("Digite o valor da prestação: "))
valormulta=float(input("Digite a porcentagem da multa devido atraso: "))
valordias=int(input("Digite a quantidade de dias atrasados: "))
Prestacao=valorprestacao+(valorprestacao*(valormulta/100)*valordias)
print("Seu débito é: ", Prestacao)
