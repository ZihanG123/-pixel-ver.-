from cmu_graphics import *
from player import *
from PIL import Image

def onAppStart(app):
    # app.cafeURL = 'cmu://872707/34739461/cafeImage.PNG'
    # app.amuroURL = 'cmu://872707/34739463/amuroImage.png'
    pass

def redrawAll(app):
    drawImage('./images/cafeEntireImage.PNG', 0, 0, width=640, height=640)
    
    drawImage('./images/amuroImage.PNG', amuro.playerPosX, amuro.playerPosY, width=128, height=128, align='center')
    
def onKeyPress(app, key):
    amuro.playerKeyPress(key)
    amuro.move()

def onKeyHold(app, key):
    amuro.playerKeyPress(key)
    amuro.move()

def main():
    runApp(width=640, height=640)



amuro = Player(320, 320, 'amuro')
amuro.getCafeValidMovement()


main()