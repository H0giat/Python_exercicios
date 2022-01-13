# aula base para esse estudo: Python do Curso em Vídeo
lanche=['Hambuguer','Refrigerante','Batata frita']
print(lanche)
lanche.append('Milkshake')
print(lanche)
lanche.insert(0, 'Sorverte')
print(lanche)

# apagar elementos

del lanche[0]
lanche.pop(3)
lanche.remove('Refrigerante')
print(lanche)

# usando if quando não tiver um valor 
if 'Soverte' in lanche:
    lanche.remove('Sorvete')
