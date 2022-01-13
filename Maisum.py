import math
c=int(input("Digite o consumo médio mensal: "))
tr=int(input("Digite o tempo de reposição: "))
estoque_min=math.sqrt(c*tr)
estoque_total=c+estoque_min
print("O estoque mínimo deve ser de: ", estoque_min)
print("O estoque total deve ser de: ", estoque_total)
