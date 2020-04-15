import numpy as np
import statistics as st
import random

def lista_random():
    lista = []
    for i in range(0,12):
        lista.append(random.randint(1,50))
    lista.sort()
    return lista

lista = lista_random()
print(f'A sua lista é: {lista}')
print(f'A média dos índices é: {np.mean(lista):.4f} ')
print(f'A moda é: {st.mode(lista):.4f} ')
print(f'A Mediana é: {st.median(lista):.4f} ')
print(f'A variância amostral é: {st.pvariance(lista):.4f}')
print(f'O desvio padrão amostral é: {st.stdev(lista):.4f}')
print(f'O coeficiente de variação é: {st.variance(lista):.4f}')
