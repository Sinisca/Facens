import pandas as pd
import random

traindata = pd.read_csv('ex1_train_data.csv', delimiter=';')

def mse(Y, Y_pred):
    result = 1/len(Y) * sum((Y - Y_pred) ** 2)
    return result

a = random.randrange(1, 100)
b = random.randrange(1, 100)
L = 0.0001
epochs = 10000

for i in range(epochs):
        Y_pred = traindata['x'] * a + b

        n = len(Y_pred)

        a = a - L * (-2/n) * sum(traindata['x'] * (traindata['y'] - Y_pred))
        b = b - L * (-2/n) * sum(traindata['y'] - Y_pred)

Y_pred = traindata['x'] * a + b
final_mse = mse(traindata['y'], Y_pred)
print('mse = %.3f, learned a = %3.f, learned b = %.3f')