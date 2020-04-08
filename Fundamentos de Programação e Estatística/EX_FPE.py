import numpy as np
import statistics as st

def insert_data():
    lista = []
    print('\nREGRAS NA FORMAÇÃO DA LISTA:\n'
          '1.Um dos valores tem que estar repetido\n'
          '2.O conjunto de dados deve apresentar, pelo menos, 6 valores únicos.\n'
          '3.NÃO É PERMITIDO escolher todos os números iguais.\n'
          '4.A LISTA POSSUI APENAS 12 ELEMENTOS\n')

    for i in range(0, 12):
        elemento = int(input('Elemento inserido no índice {}: '.format(i)))
        lista.append(elemento)
    return lista

lista = insert_data()
print('A sua lista é: ', lista)
print('A média dos índices é: {:.4f} '.format(np.mean(lista)))
print('A moda é: {:.4f} '.format(st.mode(lista)))
print('A Mediana é: {:.4f} '.format(st.median(lista)))
print('A variância amostral é: {:.4f}'.format(st.pvariance(lista)))
print('O desvio padrão amostral é: {:.4f}'.format(st.stdev(lista)))
print('O coeficiente de variação é: {:.4f}'.format(st.variance(lista)))
