from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import numpy as np
from sklearn.metrics import confusion_matrix

bc = load_breast_cancer()

data = bc.data
target = bc.target
print(data.shape)
print(np.unique(target))

# separando os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.33, random_state=42)

# treinando o modelo
knn = KNeighborsClassifier(n_neighbors=1)
print(knn.fit(X_train, y_train))
# predizendo os rótulos com o modelo
y_pred = knn.predict(X_test)

# calculando a acurácia sem scikit-learn
certos = 0

for idx, rotulo in enumerate(y_pred):
    if rotulo == y_test[idx]:
        certos += 1
print('Acurácia:', certos/y_pred.shape[0])

# calculando a acurácia de forma vetorizada
certos = np.sum(y_test == y_pred)
print('Acurácia:', certos/y_pred.shape[0])

# avaliando o modelo com o scikit-learn
print('Acurácia:', accuracy_score(y_test, y_pred))

# predizendo os rótulos a partir do modelo
y_pred = knn.predict(X_test)

# vp = verdadeiros positivos
# vn = verdadeiros negativos
# fp = falsos positivos
# fn = falsos negativos

vp = 0
vn = 0
fp = 0
fn = 0

for pred, true in zip(y_pred, y_test):
    if pred == 1:
        if pred == true:
            vp += 1
        else:
            fp += 1
    else:
        if pred == true:
            vn += 1
        else:
            fn += 1

print('VP:', vp)
print('FP:', fp)
print('VN:', vn)
print('FN:', fn)
print('---')

# calculando a matriz utilizando scikit-learn
print(confusion_matrix(y_test, y_pred))
print('---')

# obtendo os resultados com scikit-learn
vn, fp, fn, vp = confusion_matrix(y_test, y_pred).ravel()
print('VP:', vp)
print('FP:', fp)
print('VN:', vn)
print('FN:', fn)

#Precisão
p = vp / (vp+ fp)
print('Precisão: ', p)

#Revocação
r = vp / (vp +fn)
print('Revocação: ', r)

#F-medida
f = 2 * (p * r / (p + r))
print('F-medida: ', f)


