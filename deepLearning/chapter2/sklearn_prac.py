from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
import mglearn
import matplotlib.pylab as plt
import numpy as np
 # pip install mglear
 
X,y=make_moons(n_samples=100, noise=0.25, random_state=3)
X_train, X_test, y_train, y_test= train_test_split(X,y,stratify=y, random_state=42)

mlp=MLPClassifier(solver='lbfgs', random_state=0).fit(X_train, y_train)
mglearn.plots.plot_2d_separator(mlp, X_train, fill=True, alpha=.3)
mglearn.discrete_scatter(X_train[:,0], X_train[:, 1], y_train)

plt.xlabel("feature0")
plt.ylabel("feature1")

plt.show()
