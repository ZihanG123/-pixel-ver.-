from cmu_graphics import *
from player import *
from PIL import Image

def getCafeValidMovement():
        validSpaceImg = Image.open('./images/cafeValidMovementImage.PNG')
        validSpaceImg.resize((640,640))
        print(validSpaceImg.width, validSpaceImg.height)
        for x in range(validSpaceImg.width):
            for y in range(validSpaceImg.height):
                pixel = validSpaceImg.getpixel((x, y))
