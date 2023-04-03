from dataStructure import initializeDiscriminator
from math import ceil
from random import shuffle, randint

inpSize = 12
classes = 2
n = 2

p = ceil(inpSize / n)

def getRel():

    out = []

    indexes = list(range(0, inpSize))

    while len(out) < n * p:
        out.append(randint(0,inpSize - 1))

    shuffle(out)

    for i in range(n):
        out.append(indexes[i*p: (i+1)*p])

    return out

correspondence = getRel()
rams = initializeDiscriminator(classes, p, n)

def convertBinary(values):
    pos = 0
    for e, i in values:
        pos += (2**i * int(e))

    return pos


def train(data, c, rams, corresp):

    for e, i in corresp:
        for f, j in e:
            rams[c][1][i, j] = data[f]

    for i in range(p):
        row = convertBinary(rams[c][1][:,i])
        rams[c][0][row,i] = rams[c][0][row,i] + 1

    return rams

if __name__ == "__main__":

    trainData = input("Insert data: \n")
    trainData = list(map(lambda x: int(x), trainData.split()))
    c = int(input("Insert class: \n")) - 1

    rams = train(trainData, c, rams, correspondence)



        







