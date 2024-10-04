'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
 Faça também um programa que importe esse módulo e use algumas dessas funções.
'''

def aumentar(valor,fator=0):
    calculo = valor * (1+(fator/100))
    novoValor = round(calculo,2)
    return novoValor

def diminuir(valor,fator=0):
    calculo = valor * (1-(fator/100))
    novoValor = round(calculo,2)
    return novoValor

def dobro(valor):
    calculo = valor * 2
    novoValor = round(calculo,2)
    return novoValor

def metade(valor):
    calculo = valor / 2
    novoValor = round(calculo,2)
    return novoValor

def moeda(valor=0,pais='R$'):
    return f'{pais}{valor:.2f}'.replace('.',',')

# print(moeda(20,'USS ')) #Exemplo Implementação Moeda