dia=[]
volume=[]

for n in range(3):
    nn=input('Digite o dia da semana: ')
    dia.append(nn)
    vv=float(input('Digite o volume do dia da semana: '))
    volume.append(vv)

acum=0
qtd=0

for n in range(3):
    if(dia[n]=='Quarta-feira'):
        acum=acum+volume[n]
        qtd=qtd+1
media=acum/qtd
print('A média de chuvas as quartas é de %.3f'%media)

acum2=0
for n in range(3):
    acum2=acum2+volume[n]
print('O valor total dos dias cadastrados é de:', acum2)



'''
for n in range(10):
    dia.append(input('Digite o dia da semana: '))
    volume.append(float(input('Digite o volume do dia da semana: ')))


print(dia)
print(volume)

acum=0
qtd=0
for n in range(3):
    if(dia[n]=='quarta-feira'):
        acum=acum+volume[n]
        qtd=qtd+1
media=acum/qtd 
'''

'''
o código do professor

dia=[]
volume=[]

for n in range(3):
  nn= input('Digite o dia da semana')
  dia.append(nn)
  vv= float(input('Digite o volume do dia da semana'))
  volume.append(vv)

acum=0
qtd=0

for n in range(3):
  if(dia[n]=='Quarta-feira'):
    acum=acum+volume[n]
    qtd= qtd+1
media= acum/qtd
print('A média de chuvas as quartas é de %.3f'%media)
acum2=0
for n in range(3):
  acum2=acum2+volume[n]
print('O volume total dos dias cadastradados é de:', acum2)
'''
