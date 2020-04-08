import numpy as np
import pandas as pd
import statistics as st
from collections import defaultdict

class Object:
    def __init__(self, lista, media, moda, mediana, varAmo, desAmo, coeAmo):
        self.__lista = lista
        self.__media = media
        self.__moda = moda
        self.__mediana = mediana
        self.__varAmo = varAmo
        self.__desAmo = desAmo
        self.__coeAmo = coeAmo

    @property
    def media(self):
        print('A média dos índices é: {:.4f} '.format(np.mean(self.__lista)))

    @property
    def moda(self):
        print('A moda é: {:.4f} '.format(st.mode(self.__lista)))

    @property
    def mediana(self):
        print('A Mediana é: {:.4f} '.format(st.median(self.__lista)))

    @property
    def varAmo(self):
        print('A variância amostral é: {:.4f}'.format(st.pvariance(self.__lista)))

    @property
    def desAmo(self):
        print('O desvio padrão amostral é: {:.4f}'.format(st.stdev(self.__lista)))

    @property
    def coeAmo(self):
        print('O coeficiente de variação é: {:.4f}'.format(st.variance(self.__lista)))

class lista(Object):
    def __init__(self, lista):
        print('\nREGRAS NA FORMAÇÃO DA LISTA:\n'
              '1.Um dos valores tem que estar repetido\n'
              '2.O conjunto de dados deve apresentar, pelo menos, 6 valores únicos.\n'
              '3.NÃO É PERMITIDO escolher todos os números iguais.\n'
              '4.A LISTA POSSUI APENAS 12 ELEMENTOS\n')

        lista = []

        for i in range(0, 12):
            elementos = int(input('Elemento inserido no índice {}: '.format(i)))
            self.__lista.append(elementos)
        return (self.__lista)