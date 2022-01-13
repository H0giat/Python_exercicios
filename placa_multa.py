placa=[]
multa=[]

for n in range(15):
    pp=input('Digite a placa do veículo: ')
    mm=float(input('Digite o valor total de multas: '))
    placa.append(pp)
    multa.append(mm)

acum=0
for n in range(15):
    acum=acum+multa[n]

media=acum/15
print('O valor médio de multas é:', media)
# ou
# acum/len(multa)
acum2=0
for n in range(15):
    if(multa[n]>=300):
        acum2=acum2+1

print('A quantidade de veículos com multas acima de R$300 é de:', acum2)

# a variavel acum acumula cada uma unidade verdadeira (de um em um, nesse caso)

'''
o código do professor

placa =[]
multa=[]

for n in range(15):
  pp=input('Digite a placa do veículo')
  mm= float(input('Digite o valor total de multas'))
  placa.insert(n,pp)
  multa.insert(n,mm)

  #placa.append(input('Digite a placa do veículo'))
  #multa.append(float(input('Digite a multa do veículo')))
  #placa.insert(n,(input('Digite a placa do veículo')))
  #multa.insert(n,(float(input('Digite a multa do veículo'))))

acum=0

for n in range(15):

  acum = acum+multa[n]

#media= acum/len(multa)
#ou
media=acum/15

print('o valor médio de multas é igual a:',media)

acum2=0

for n in range(15):

  if(multa[n]>=300):

    acum2=acum2+1

print ('A quantidade de veículos com',
    'multas acima de R$300,00 é de: ', acum2)

'''

