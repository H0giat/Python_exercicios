nome=[]
nota=[]
curso=[]
resp='s'
while(resp=='s' or resp=='S'):
    n=input('Digite o nome do aluno: ')
    nt=float(input('Digite a nota do aluno: '))
    cr=input('Digite o curso do aluno CCP ou TADS: ')
    nome.append(n)
    nota.append(nt)
    curso.append(cr)
    resp=input(f'Digite "s" para continuar: ')

qtd=0
for i in range(len(curso)):
    if(curso[i]=='TADS'):
        qtd=qtd+1
print(f'A quantidade de alunos em TADS é: {qtd}.')

print(nome)
print(nota)
print(curso)

acum=0
for i in range(len(nota)):
    acum=acum+nota[i]

media=acum/len(nota)
print(f'A média de todos os alunos de CCP e TADS é: {media}.')

qtd2=0
for i in range(len(nota)):
    if(nota[i]>media):
        qtd2=qtd2+1
print(f'A quantidade de alunos com a média acima da turma é: {qtd2}.')