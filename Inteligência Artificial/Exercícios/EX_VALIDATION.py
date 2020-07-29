from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
import pandas as pd

#Loag Breast Cancer Database
breast_cancer = load_breast_cancer()
X = breast_cancer.data
y = breast_cancer.target

#Test Accuracy With Holdout
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=True, random_state=42)
grid_params = {
    'n_neighbors':[3,5,6,7,8,9,10,11,12,20,30,50],
    'weights':['uniform', 'distance'],
    'metric': ['euclidean', 'manhattan', 'chebyshev'],
    'algorithm':['ball_tree', "kd_tree"],
    'leaf_size':[10,20,30,40,50,60,70,80,90,100],
}

knn = KNeighborsClassifier(n_neighbors=3)

gs = GridSearchCV(knn, grid_params,n_jobs=1)

gs_results = gs.fit(X_train, y_train)
print(gs_results.best_score_)
print(gs_results.best_estimator_)
print(gs_results.best_params_)

y_pred = gs.predict(X_test)
print(accuracy_score(y_test, y_pred))

#Test Accuracy with Cross validation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=True, random_state=42)
grid_params = {
    'n_neighbors':[3,5,6,7,8,9,10,11,12,20,30,50],
    'weights':['uniform', 'distance'],
    'metric': ['euclidean', 'manhattan', 'chebyshev'],
    'algorithm':['ball_tree', "kd_tree"],
    'leaf_size':[10,20,30,40,50,60,70,80,90,100],
}

knn = KNeighborsClassifier(n_neighbors=3)

gs = GridSearchCV(knn, grid_params, cv=3, n_jobs=1)

gs_results = gs.fit(X_train, y_train)
print(gs_results.best_score_)
print(gs_results.best_estimator_)
print(gs_results.best_params_)

y_pred = gs.predict(X_test)
print(accuracy_score(y_test, y_pred))

#Check Data Distribution
df = pd.DataFrame(X)
print(df.describe())
print(df.describe())

#Standardize Data
pipeline = Pipeline([('scaler', StandardScaler()), ('KNN', KNeighborsClassifier())])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=True, random_state=42)
grid_params = {
    'KNN__n_neighbors':[3,5,6,7,8,9,10,11,12,20,30,50],
    'KNN__weights':['uniform', 'distance'],
    'KNN__metric': ['euclidean', 'manhattan', 'chebyshev'],
    'KNN__algorithm':['ball_tree', "kd_tree"],
    'KNN__leaf_size':[10,20,30,40,50,60,70,80,90,100],
}

gs = GridSearchCV(pipeline, grid_params, cv=3, n_jobs=1)

gs_results = gs.fit(X_train, y_train)
print(gs_results.best_score_)
print(gs_results.best_estimator_)
print(gs_results.best_params_)

y_pred = gs.predict(X_test)
print(accuracy_score(y_test, y_pred))
scores = cross_val_score(gs_results.best_estimator_, X_test, y_test, cv=3)
print('Acurácia - %.2f +- %.2f' % (scores.mean() * 100, scores.std() * 100))

