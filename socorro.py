'''

Seu irmão abriu uma empresa de revenda de veículos usados. Obviamente, ele pediu sua ajuda para resolver um

problema (vá se acostumando). Ele armazena seus veículos listas. Nessas listas encontra-se os seguintes dados:

  placa, nome, ano, cor, preço e número de donos anteriores.

  Ele precisa de um programa que forneça algumas informações de sua frota e você deve construir alguns relatórios

  para extrair essas informações. Abaixo os relatórios necessários:



****************Imprimir todos os veículos

Imprimir todos os veículos de uma determinada cor

Imprimir todos os veículos produzidos acima de um determinado ano

Imprimir todos os veículos abaixo de um determinado preço

Imprimir todos os veículos entre uma determinada faixa de preço

Imprimir todos os veículos entre uma determinada faixa de preço e uma faixa de ano



['Douglas', 'Bruno', 'Ademar', 'Gabriel','Emanueli']

['AAA-1A11','BBB-2B222', 'CCC-3C333', 'DDD-4D444', 'EEE-5E555']



'''
'''
placa=['AAA-1A11','BBB-2B222', 'CCC-3C333', 'DDD-4D444', 'EEE-5E555']

nome=['ONIX', 'FIAT UNO', 'CELTA', 'CORSA', 'HILUX']

ano=[2021,2020,1970,2000,2021]

cor=['CINZA','VERMELHO','ROXO ALELUIA', 'AMARELO', 'ROSA']

preco=[68000.00, 45000.00, 28000,00, 50000.00,110000.00]

nda=[1,2,2,5,1]

nome_ultimo_dono=['Douglas', 'Bruno', 'Ademar', 'Gabriel','Emanueli']



nv= int(input('Digite a quantidade de veíulos a seem inseridos'))



for i in range(nv):

  pp= input('Digite a placa do veículo')

  placa.append(pp)

  nn=input('Digite o nome do veículo')

  nome.append(nn)

  aa=int(input('Digite o ano de fabricação do veículo'))

  ano.append(aa)

  cc=input('Digite a cor do veículo')

  cor.append(cc)

  pr=float(input('Digite o valor do veículo'))

  preco.append(pr)

  ndanteriores= int(input('Digite o número de donos deste veículo'))

  nda.append(ndanteriores)

  nud=input('Digite o nome do último dono')

  nome_ultimo_dono.append(nud)





#Imprimir todos os veículos

for i in range(len(placa)):

  print ('O dono do carro', nome[i],

      ' na cor', cor[i],

      ' é o ', nome_ultimo_dono[i],

      '\nele já teve ', nda[i],' dono(s)',

      'a placa é',placa[i],

      'o ano do veículo é',ano[i],

      'está a venda por',preco[i],

      '\n******************\n')



   

#Imprimir todos os veículos de uma determinada cor?????

cor2=input('Digite uma cor para verificar em nosso estoque').upper()

for i in range(len(cor)):

  if(cor[i]==cor2):

    print ('O dono do carro', nome[i],

      ' na cor', cor[i],

      ' é o ', nome_ultimo_dono[i],

      '\nele já teve ', nda[i],' dono(s)',

      'a placa é',placa[i],

      'o ano do veículo é',ano[i],

      'está a venda por',preco[i],

      '\n******************\n')



#Imprimir todos os veículos produzidos acima de um determinado ano



ano2=int(input('Digite um ano para ser pesquisado e mostraremos as nossas ofertas'))

for i in range(len(ano)):

  if(ano[i]>=ano2):

    print ('O dono do carro', nome[i],

      ' na cor', cor[i],

      ' é o ', nome_ultimo_dono[i],

      '\nele já teve ', nda[i],' dono(s)'

'''