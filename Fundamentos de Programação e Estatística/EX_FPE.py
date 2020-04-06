import numpy as np

lista = []

def list(lista):
    x = int(input('Insira a quantidade de elementos da lista 1: '))                     #Inserção dos elementos das lista 1 pelo usuário

    for i in range(0, x):                                                               #Especificando a quantidade de elementos da lista começando pelo índice 0
        elementos = int(input('Elemento inserido no índice {}: '.format(i)))            #Inserção dos elementos e mostrando qual índice
        lista.append(elementos)                                                         #Adiciona um elemento na ultima posição da lista
    return ('A lista criada é {} '.format(lista))

print('A média dos elementos é: ', np.mean(lista))                                      #Média dos Elementos
