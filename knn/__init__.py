import numpy as np

def getDistanceMatrix(X, p):

    N, _ = X.shape
    mDist = []

    for i in range(N):
        xc = X[i, :]
        mDist.append([np.sqrt(np.sum(xc - p)**2)])

    return np.matrix(mDist)

def getKnn(X, Y, p, k):

    dm = getDistanceMatrix(X, p)

    ord = np.argsort(dm[:, 0])
    ordY = Y[ord]

    



