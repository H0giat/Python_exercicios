nota1=float(input('Digite sua primeira nota: '))
nota2=float(input('Digite sua segunda nota: '))
percentual_frequencia=int(input('Digite seu percentual de frequência: '))
media=(nota1+nota2)/2
if media>=6:
    if percentual_frequencia>=75:
        print('Aprovado!')
    else:
        print('Reprovado!')
else:
    print('Reprovado por nota.')

