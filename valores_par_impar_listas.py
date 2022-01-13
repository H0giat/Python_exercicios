valores=[]
par=[]
impar=[]

resp='s'
while(resp=='s' or resp=='S'):
    xx=int(input('Digite um número: '))
    valores.append(xx)
    resp=input('Digite s ou S para continuar: ')

for n in range(len(valores)):
    if((valores[n]%2)==0):
        par.append(valores[n])
    else:
        impar.append(valores[n])

print(valores)
print(par)
print(impar)
