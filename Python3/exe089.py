#Exercício Python #089 - Boletim com listas compostas -> https://www.youtube.com/watch?v=7xrCJnniqMw&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=21

print(('==*==')*20)
print('Bem vindo(a) - Boletim com listas compostas')
print(('==*==')*20)

alunos = []
while True:
    alunosTemp = []
    while True:
        nome = input('Nome: ')
        nota1 = float(input('Nota 1: '))
        nota2 = float(input('Nota 2: '))
        alunoMedia = (nota1+nota2)/2
        alunosTemp.append([nome,nota1,nota2,alunoMedia])
        continuar = input('Deseja continuar? [S/N]: ').strip().upper()
        while continuar not in 'SN':
            continuar = input('Deseja continuar? [S/N]: ').strip().upper()
        if continuar == 'N':
            break
    alunos.append(alunosTemp)
    break
for p,i in enumerate(alunos):
    print(f'No {[p+1]}: Nome: {alunos[0][p][0]} Média: {alunos[0][p][3]:.2f}')


print(('====')*15)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print(('====')*15)

for pos in range(0,len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')