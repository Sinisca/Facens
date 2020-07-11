from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


breast_cancer = load_breast_cancer()
data = breast_cancer.data
target = breast_cancer.target

# separando os dados em treino e teste
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.33, random_state=42)

# separando o conjunto de treino em validação também
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.33, random_state=42)

# treinando o modelo
knn = KNeighborsClassifier(n_neighbors=3)
print(knn.fit(X_train, y_train))

y_pred = knn.predict(X_val)
print(accuracy_score(y_val, y_pred))

