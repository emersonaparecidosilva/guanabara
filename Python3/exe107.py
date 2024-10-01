#exercicio 107 - Tema XYZ

import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'modulos'))) # Adiciona a pasta 'modulos' ao sys.path

from moedas import aumentar,diminuir,dobro,metade
from helpers import título

título('Treinamento de Módulos',2)
num = int(input('Digite o preço: R$ '))

print(f'A metade de R$ {num} é R$ {metade(num)}.')
print(f'O dobro de R$ {num} é R$ {dobro(num)}.')
print(f'Aumentando 10% de R$ {num} é R$ {aumentar(num,10)}.')
print(f'Diminuindo 10% de R$ {num} é R$ {diminuir(num,10)}.')

