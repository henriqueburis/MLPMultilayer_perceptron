import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import cross_val_score


df = pd.read_csv("./dados.csv")

X_train, X_test, y_train, y_test = train_test_split(df.loc[:, df.columns != 'price'], df['price'], random_state=80)

print(X_train.head())

MLP = MLPRegressor(solver='lbfgs', alpha=1e+4,activation='relu',
                    hidden_layer_sizes=(4,2))


MLP.fit(X_train, y_train)

print("Accuracy on training set: {:.3f}".format(MLP.score(X_train, y_train)))

# Predict
y_1 = MLP.predict(X_test)

#   Validação Cruzada K-Fold
score = cross_val_score(MLP,  X_train, y_train, cv=10).mean()

print(score)

#   grafico
plt.scatter(y_test, y_1)
range = [y_test.min(), y_1.max()]
plt.plot(range, range, 'red')
plt.xlabel('Preço real')
plt.ylabel('Preço predito')
plt.show()
