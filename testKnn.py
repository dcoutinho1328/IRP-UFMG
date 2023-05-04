from knn import getKnn
import numpy as np

# Define o desvio padrão
desvio = 0.3

# Define o número de pontos a serem gerados
num_pontos = 20

# Gera uma distribuição normal de pontos ao redor do ponto central
g1 = np.hstack((np.random.normal(loc=[2,2], scale=desvio, size=(num_pontos, 2)), np.matrix([-1 for _ in range(num_pontos)]).transpose()))
g2 = np.hstack((np.random.normal(loc=[4,4], scale=desvio, size=(num_pontos, 2)), np.matrix([1 for _ in range(num_pontos)]).transpose()))

data = np.vstack((g1, g2))
np.random.shuffle(data)

x_in = data[:, :2]
y_in = data[:, 2]

x_test = g1[13, :2] + np.matrix([[0.01], [0.1]])

k = 2

dm = getKnn(x_in, y_in, x_test, k)

