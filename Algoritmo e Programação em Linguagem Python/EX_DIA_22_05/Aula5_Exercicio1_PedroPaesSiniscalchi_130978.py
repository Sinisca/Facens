import numpy as np
import random

#Exercicio 1
a = np.array([1, 2, 3, 4, 5])
b = np.hstack((a[:,None], np.zeros([5, 3], dtype = int))).flatten()[0:-3]
print("Exercicio 1: ", b)

#Exercicio 2
a = np.zeros((8,8), dtype = np.float64)
a[1::2, ::2] = 1
a[::2, 1::2] = 1
print("\nExercicio 2: \n", a)

#Exercicio 3
a = np.array(range(0,25)).reshape(5, 5)
a[[0, 1]] = a[[1, 0]]
print("\nExercicio 3: \n", a)

#Exercicio 4
a = np.array(range(0,25)).reshape(5, 5)
a[:,[2, 3]] = a[:,[3, 2]]
print("\nExercicio 4: \n", a)

#Exercicio 5
array = np.array([np.array([1, 2, 3])] * 4)
print("\nExercicio 5: \n", array)

#Exercicio 6
array = np.array([np.array([1, 2, 3])] * 3).transpose()
print("\nExercicio 6: \n", array)

#Exercicio 7
array = np.array([4, 95, 37, 64, 42, 19, 55, 38, 46, 83, 48, 67, 98, 21, 10, 88])
b = array[np.where(np.logical_and(array >= 35, array <= 55))]
print("\nExercicio 7: \n", b)

#Exercicio 8
array = np.arange(0, 101)
print("\nExercicio 8")
print("Matriz : \n", array)
a = np.random.uniform(0, 100)
print(f"Numero é: {a:.4f}")
print("O numero que mais se aproxima é: ", np.abs(array - a).argmin())

#Exercicio 9
np.random.seed(100)
array = np.random.uniform(1, 50, 30)
array[np.where(array < 10)] = 10
array[np.where(array > 30)] = 30
print("Vetor:", a)
print("\nExercicio 9: \n", array)

#Exercicio 10
matriz = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
def function():
    return np.linalg.det(matriz)
print("\nExercicio 10: \n", function())