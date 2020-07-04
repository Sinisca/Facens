from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

iris = load_iris()
print(iris.target_names)
data = iris.data # atributos
target = iris.target # classes
print(data[0])
print(iris.target_names[target[0]])

# separando os dados
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.6, shuffle=False, random_state=42)

# treinando o modelo
knn = KNeighborsClassifier(n_neighbors=4)
print(knn.fit(X_train, y_train))

# predizendo
y_pred = knn.predict(X_test)

# comparando com gabarito
accuracy_score(y_test, y_pred)
print(confusion_matrix(y_test, y_pred))

