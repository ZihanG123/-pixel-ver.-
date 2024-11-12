from cmu_graphics import *
from player import *
from PIL import Image

def onAppStart(app):
    # app.cafeURL = 'cmu://872707/34739461/cafeImage.PNG'
    # app.amuroURL = 'cmu://872707/34739463/amuroImage.png'
    print('hello')

def redrawAll(app):
    drawImage('./images/cafeImage.PNG', 0, 0, width=640, height=640)
    drawImage('./images/amuroImage.PNG', amuro.playerPosX, amuro.playerPosY, width=128, height=128, align='center')
    
    addCafeCustomerDesks()
    addCafeKitchenDesks()
    addCafeChairs()
    
def onKeyPress(app, key):
    amuro.playerKeyPress(key)
    amuro.move()

def onKeyHold(app, key):
    amuro.playerKeyPress(key)
    amuro.move()

def addCafeCustomerDesks():
    drawImage('./images/desk1Image.PNG', 96, 544, width=64, height=64, align='center')
    drawImage('./images/desk1Image.PNG', 224, 544, width=64, height=64, align='center')
    drawImage('./images/desk1Image.PNG', 352, 544, width=64, height=64, align='center')
    drawImage('./images/desk1Image.PNG', 416, 544, width=64, height=64, align='center')

def addCafeKitchenDesks():
    drawImage('./images/desk2Image.PNG', 160, 224, width=64, height=64, align='center')
    drawImage('./images/desk2Image.PNG', 160, 288, width=64, height=64, align='center')
    drawImage('./images/desk2Image.PNG', 224, 288, width=64, height=64, align='center')
    drawImage('./images/desk2Image.PNG', 288, 288, width=64, height=64, align='center')
    drawImage('./images/desk2Image.PNG', 352, 288, width=64, height=64, align='center')
    drawImage('./images/desk2Image.PNG', 416, 288, width=64, height=64, align='center')

def addCafeChairs():
    drawImage('./images/chairImage.PNG', 96, 480, width=64, height=64, align='center')
    drawImage('./images/chairImage.PNG', 224, 480, width=64, height=64, align='center')
    drawImage('./images/chairImage.PNG', 352, 480, width=64, height=64, align='center')
    drawImage('./images/chairImage.PNG', 416, 480, width=64, height=64, align='center')

def main():
    runApp(width=640, height=640)



amuro = Player(320, 320, 'amuro')
amuro.getCafeValidMovement()


main()