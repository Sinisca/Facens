import numpy as np
import pandas as pd
import statistics as st

lista = []

def vetor(lista):

    print('\nREGRAS NA FORMAÇÃO DA LISTA:\n'
          '1.Um dos valores tem que estar repetido\n'
          '2.O conjunto de dados deve apresentar, pelo menos, 6 valores únicos.\n'
          '3.NÃO É PERMITIDO escolher todos os números iguais.\n'
          '4.A LISTA POSSUI APENAS 12 ELEMENTOS\n')

    for i in range(0, 12):
        elementos = int(input('Elemento inserido no índice {}: '.format(i)))    #Inserção dos elementos e mostrando qual índice
        lista.append(elementos)                                                #Adiciona um elemento na ultima posição da lista
    return(lista)

print('A sua lista é: ', vetor(lista))
print('A média dos índices é: {:.4f} '.format(np.mean(vetor(lista))))
print('A moda é: {:.4f} '.format(st.mode(lista)))
print('A Mediana é: {:.4f} '.format(st.median(vetor(lista))))
print('A variância amostral é: {:.4f}'.format(st.pvariance(vetor(lista))))
print('O desvio padrão amostral é: {:.4f}'.format(st.stdev(vetor(lista))))
print('O coeficiente de variação é: {:.4f}'.format(st.variance(vetor(lista))))


