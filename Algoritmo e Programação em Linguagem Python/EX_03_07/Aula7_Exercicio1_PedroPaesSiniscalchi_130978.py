import pandas as pd
import numpy as np

#1 - Efetuar a leitura do dataset através do Pandas, gerando um DataFrame de nome tit,
#levando-se em consideração que o arquivo encontra-se na mesma pasta do notebook.
tit = pd.read_csv('titanic_data.csv')

#2 - Quantas linhas e colunas tem o dataset? Quais os tipos das colunas?
print(tit)

#3 - Mostre os dados dos dez primeiros e 8 últimos registros do dataset.
print(tit.head(10))
print(tit.tail(8))

#4 - Cálculos envolvendo colunas numéricas com dados faltantes podem sofrer impacto.
#É possível afirmar se há dados faltantes no dataset? Caso positivo, quais e quantos seriam esses dados?
#Preencha os dados faltantes de forma que não influenciem em operações futuras.
print(tit.dropna(axis = 1))

#ADEQUANDO O DataSet
#4 - Uma vez que algumas colunas não serão utilizadas, eventualmente é melhor excluí-las para que não interfiram na análise.
#Assim, exclua do dataset as colunas Sibsp, Parch e Ticket.
print(tit.drop(['SibSp', 'Ticket', 'Parch'], axis = 1))

#5 - Renomear as colunas restantes para a lingua portuguesa, utilizando os seguintes nomes de colunas: IdPassageiro, Sobreviveu, Classe, Nome, Sexo, Idade, Tarifa, Cabine e Embarque
print(tit.rename(columns = {'PassengerId': 'IdPassageiro', 'Survived': 'Sobreviveu', 'Pclass': 'Classe', 'Name': 'Nome', 'Sex': 'Sexo', 'Age': 'Idade', 'Fare': 'Tarifa', 'Cabin': 'Cabine', 'Embarked': 'Embarque'}))

#6 - Alterar o conteudo da coluna Sobreviveu para:
#0 => Não
#1 => Sim
print(tit['Sobreviveu'].apply(lambda x: x.replace('0', 'Não')))
print(tit['Sobreviveu'].apply(lambda x: x.replace('1', 'Sim')))

#7 - Alterar o conteudo da coluna Sexo para:
#female => Mulher
#male => Homem
print(tit['Sexo'].apply(lambda x: x.replace('female', 'Mulher')))
print(tit['Sexo'].apply(lambda x: x.replace('Male', 'Homem')))

#ALGUNS NÚMEROS
#8 - Quantas mulheres e quantos homems estavam à bordo, de acordo com o dataset?
soma_male = tit['male'].sum()
soma_female = tit['female'].sum()
print(soma_male)
print(soma_female)

#9 - Quantos passageiros sobreviveram e quantos não sobreviveram?

#10 - Quantas mulheres não sobreviveram?

#11 - Proporcionalmente, sobreviveram mais homens ou mais mulheres? Cite as proporções.

#12 - Levando-se em consideração a idade dos passageiros, qual a idade e quantidade de pessoas com o maior número de mortos?

#13 - Qual a média de idade dos homens sobreviventes?

#14 - Levando-se em consideração passageiros prioritários (mulheres e crianças de até 15 anos independente do sexo) qual a proporção de sobreviventes por sexo?

#15 - Qual a quantidade de passageiros por classe?

#16 - Qual o percentual de sobreviventes por classe?

#17 - Crie um dataframe que demonstre a quantidade de sobreviventes e não sobreviventes, agrupados por sexo e classe.

#18 - Dos homens com idade entre 24 e 30 anos quantos da classe 3 sobreviveram? Quantos da classe 2 não sobreviveram?

#19 - Calcule a probabilidade condicional de uma pessoa sobreviver, dado seu sexo e a classe em que estava viajando:
#P(S= true | G=female,C=1)
#P(S= true | G=female,C=2)
#P(S= true | G=female,C=3)
#P(S= true | G=male,C=1)
#P(S= true | G=male,C=2)
#P(S= true | G=male,C=3)