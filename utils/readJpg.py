from PIL import Image

def getGrayscalePixels(path):
    return Image.open(path, 'r').convert('L')

def getImage(path):
    return Image.open(path, 'r')
