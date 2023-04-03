from os.path import dirname
from utils.readJpg import getImage, getGrayscalePixels
from templateMatching import findItem, drawBounds

placas = dirname(__file__) + "/assets/templateMatching/placas.jpg"

p1 = dirname(__file__) + "/assets/templateMatching/placa_1.jpg"

p2 = dirname(__file__) + "/assets/templateMatching/placa_2.jpg"

p3 = dirname(__file__) + "/assets/templateMatching/placa_3.jpg"

resultsFolder = dirname(__file__) + "/results"

loc1, size1 = findItem(p1, placas)
loc2, size2 = findItem(p2, placas)
loc3, size3 = findItem(p3, placas)

srcImg = getImage(placas)
srcGrayscale = getGrayscalePixels(placas)

output = drawBounds(srcImg, loc1, *size1, color='red')
output = drawBounds(output, loc2, *size2, color='blue')
output = drawBounds(output, loc3, *size3, color='green')

outputGs = drawBounds(srcGrayscale, loc1, *size1, color='red')
outputGs = drawBounds(outputGs, loc2, *size2, color='blue')
outputGs = drawBounds(outputGs, loc3, *size3, color='green')

output.save(resultsFolder + "/resultado.jpg")
outputGs.save(resultsFolder + "/resultado_grayscale.jpg")



