from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

bc = load_breast_cancer()
data = bc.data
target = bc.target
print(np.unique(target))

# separando os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.33, random_state=42)

# treinando o modelo
knn = KNeighborsClassifier(n_neighbors=8)
knn.fit(X_train, y_train)

probas = knn.predict_proba(X_test)
print(probas)
fpr, tpr, thresholds = roc_curve(y_test[:], probas[:,1])
roc_auc = auc(fpr, tpr)

plt.plot([0, 1], [0, 1], '--', color=(0.6, 0.6, 0.6), label='Aleatório')
plt.plot(fpr, tpr, lw=1, label='ROC (area = %0.2f)' % roc_auc)

plt.xlim([-0.05, 1.05])
plt.ylim([-0.05, 1.05])
plt.xlabel('Falsos Positivos')
plt.ylabel('Positivos Verdadeiros')
plt.title('ROC do KNN')
plt.legend(loc="lower right")
plt.show()
