from utils.readJpg import getGrayscalePixels
import numpy as np
from math import floor
from PIL import ImageDraw

def findItem(target, source):

    targetImg = getGrayscalePixels(target)

    tWidth, tHeight = targetImg.size

    sourceImg = getGrayscalePixels(source)

    sWidth, sHeight = sourceImg.size

    location = (-1, -1)

    t = np.asarray(targetImg)
    s = np.asarray(sourceImg)

    allValues = []

    searchLimits = (sWidth - tWidth, sHeight - tHeight)

    for i in range(searchLimits[1]):
        for j in range(searchLimits[0]):
            partial = s[i:i+tHeight, j:j+tWidth]
            allValues.append(np.sum(np.abs(t - partial)))

    idx = allValues.index(min(*allValues))

    line = floor(idx/searchLimits[0])

    location = (line + 1, idx - (line * searchLimits[0]))

    return location, (tWidth, tHeight)

def drawBounds(source, location, w, h, color='red'):

    img = source.convert("RGB")

    draw = ImageDraw.Draw(img)

    draw.line((location[1], location[0], location[1] + w, location[0]), fill=color, width=3)
    draw.line((location[1], location[0], location[1], location[0] + h), fill=color, width=3)
    draw.line((location[1] + w, location[0] + h, location[1] + w, location[0]), fill=color, width=3)
    draw.line((location[1] + w, location[0] + h, location[1], location[0] + h), fill=color, width=3)

    return img

