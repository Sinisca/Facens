import pandas as pd

#Leia o arquivo csv (911.csv) como um dataframe chamado calls
#Última linha desmontra a quantidade de linhas e colunas
calls = pd.read_csv('911.csv')
print(calls)

#Quantas linhas e colunas tem o arquivo? Qual a quantidade de memória necessária para carregá-lo?
#Última linha desmontra a quantidade de memória utilzada
print('Memory usage is in bites: \n', calls.memory_usage().sum())
print(calls.info())

#Quais são os top 5 CEPs nas chamadas 911?
print(calls['zip'].value_counts().head(5))

#Quais são os 5 principais municípios nas chamadas 911?
calls_top5 = calls['twp'].value_counts().head(5)
print('\n',calls_top5)

#Quantos códigos de título únicos existem?
print('Titulos únicos: ', len(calls['title'].unique()))

#Na coluna title existem Razões / Departamentos especificados antes do código do título. Estes são "EMS"_, _"Fire" e "Traffic". Crie uma nova coluna chamada Reason que conterá esse valor em cada linha
#Por exemplo, se o valor da coluna do título for EMS: BACK PAINS / BLESSOR, o valor da coluna Reason será EMS.
calls["Reason"] = calls["title"].str.split(":").str[0]
print(calls)

#Qual é a razão mais comum para uma chamada do 911 com base nessa nova coluna?
print(calls["Reason"].value_counts().head(1))

#Qual é o tipo de dados dos objetos na coluna _timeStamp_?
print(calls['timeStamp'].dtype)

#Converta a coluna timeStamp para DateTime. Use pd.to_datetime para essa operação.
calls['timeStamp'] = pd.to_datetime(calls['timeStamp'])
print(calls)

#Crie 3 novas colunas chamadas Hour_, _Month e Day of Week. Você criará essas colunas com base na coluna timeStamp
calls['Hour'] = pd.DatetimeIndex(calls['timeStamp']).hour
calls['Month'] = pd.DatetimeIndex(calls['timeStamp']).month
calls['Day of Week'] = pd.DatetimeIndex(calls['timeStamp']).weekday
print(calls)

#Observe como o dia da semana é um número inteiro de 0-6. Mapeie os nomes das seqüências reais para o dia da semana, nessa mesma coluna:
#0 = > Mon
#1 = > Tue
#2 = > Wed
#3 = > Thu
#4 = > Fri
#5 = > Sat
#6 = > Sun
calls['Day of Week'] = calls['timeStamp'].dt.day_name().str[0:3]
print(calls)

#Qual a quantidade de chamadas de cada motivo (_Reason_) por mês?
print(calls.groupby('Month').agg({'Reason':'value_counts'}))

#Qual foi o dia com a maior quantidade de chamadas? Quantas chamadas foram executadas neste dia?
calls['Date'] = calls['timeStamp'].apply(lambda x: x.strftime("%d/%m/%y"))
calls['Date'].value_counts().sort_values(ascending=False).head(1)

#Levando-se em consideração apenas atendimentos feitos às sextas-feiras, qual a hora do dia com o maior número de chamadas?
print(calls[calls['Day of Week']=='Fri']['Hour'].value_counts().head(1).index[0])

#Levando-se em consideração os atendimentos relacionados a incêndio (Reason = _Fire_) qual a quantidade de chamados aos sábados?
print(calls[calls.Reason =='Fire']['Day of Week'].value_counts().loc['Sat'])