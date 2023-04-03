from numpy import matrix

def initializeDiscriminator(nd, p, n):

    mList = []

    for _ in range(nd):
        m1 = matrix([[0 for _ in range(p)] for _ in range(2**n)])
        m2 = matrix([[0 for _ in range(p)] for _ in range(n)])
        mList.append([m1,m2])

    return mList
