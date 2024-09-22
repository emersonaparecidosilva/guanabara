#Exercício Python #087 - Matriz em Python - https://www.youtube.com/watch?v=EGmlFdwD4C4&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=18

print(('==*==')*20)
print('Bem vindo(a) - Matriz em Python')
print(('==*==')*20)

soma = 0
somaTerColuna = 0
numeros = []
numerosPares = []
numerosImpares = []

for e in range(0,3):
    temp = []
    paresTemp = []
    imparTemp = []
    for i in range(0,3):
        número = int(input(f'Digite um valor para [{e},{i} ]: '))
        temp.append(número)
        if número % 2 == 0:
            soma += número
            paresTemp.append(número)
        else:
            imparTemp.append(número)
        if i ==2:
            somaTerColuna += número
    numeros.append(temp)
    numerosPares.append(paresTemp)
    numerosImpares.append(imparTemp)
for p,i in enumerate(numeros):
    print(f'{numeros[p]}')

print(f'A soma dos pares são: {soma}')
print(f'A soma dos elementos da terceira coluna: {somaTerColuna}')
print(f'O maior valor da segunda linha é: {max(numeros[1])}')

