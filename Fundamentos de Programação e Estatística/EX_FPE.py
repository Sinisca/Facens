import numpy as np
import statistics as st
import random

def lista_random():
    lista = random.sample(range(0, 50), 12)
    lista.sort()
    return lista

# def insert_data():
#     lista = []
#     for i in range(0, 12):
#         elemento = int(input('Elemento inserido no índice {}: '.format(i)))
#         lista.append(elemento)
#     return lista

lista = lista_random()
print('A sua lista é: ', lista)
print('A média dos índices é: {:.4f} '.format(np.mean(lista)))
print('A moda é: {:.4f} '.format(st.mode(lista)))
print('A Mediana é: {:.4f} '.format(st.median(lista)))
print('A variância amostral é: {:.4f}'.format(st.pvariance(lista)))
print('O desvio padrão amostral é: {:.4f}'.format(st.stdev(lista)))
print('O coeficiente de variação é: {:.4f}'.format(st.variance(lista)))
