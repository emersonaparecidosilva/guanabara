#exercicio 107 - Tema XYZ

import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'modulos'))) # Adiciona a pasta 'modulos' ao sys.path

import helpers

helpers.título('Aprendendo sobre módulos',1)

# Testa a função fatorial
print(helpers.fatorial(5))
print(helpers.triplo(2))

