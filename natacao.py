#Elabore um programa que dada a idade de um nadador

#classifica-o em uma das seguintes categorias:
#infantil A = 5 - 7 anos"
#infantil B = 8-10 anos"
#juvenil A = 11-13 anos"
#juvenil B = 14-17 anos"
#adulto = maiores de 18 anos")

idade=int(input("Digite a idade do nadador: "))
if idade<=7 and idade>=5:
    print("Nadador infantil A.")
if idade<=10 and idade>=8:
    print("Nadador infantil B.")
if idade<=13 and idade>=11:
    print("Nadador juvenil A.")
if idade<=17 and idade>=14:
    print("Nadador juvenil B.")
if idade>18:
    print("Nadador adulto.")
