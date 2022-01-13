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