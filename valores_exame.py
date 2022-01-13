a=155.50
b=95.50
c=387.75
d=79.99
tipo=input('Qual tipo de exame?')
if tipo=='a':
    print(f'Angiografia R${a}.')
elif tipo=='b':
    print(f'Venografia R${b}.')
elif tipo=='c':
    print(f'Urografia R${c}.')
elif tipo=='d':
    print(f'Ultrassom R${d}.')
else:
    print(f'Não realizamos este exame.')
'''
tipo=str(input('Qual tipo de exame?')).lower
no lugar do tipo que eu fiz
'''
# não esquecer de como usar o 'tipo' ali em cima
#  