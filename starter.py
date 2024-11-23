from cmu_graphics import *
from PIL import Image

from player import *
from dish import *
from plate import *
from menu import *
from initializer import *

# All of the images used are drawn by me.

def onAppStart(app):
    app.keyHeld = None

################
# start screen
################

def start_redrawAll(app):
    drawImage('./images/startScreenImage.PNG', 0, 0, width=640, height=640)


def start_onKeyPress(app, key):
    if key == 'space':
        setActiveScreen('game')
    elif key == 'enter':
        setActiveScreen('instructions')

################
# instructions screen
################

def instructions_redrawAll(app):
    drawImage('./images/instructionsScreenImage.PNG', 0, 0, width=640, height=640)

def instructions_onKeyPress(app, key):
    if key == 'space':
        setActiveScreen('game')
    elif key == 'escape':
        setActiveScreen('start')

################
# game screen
################

def game_redrawAll(app):
    drawImage('./images/cafeImage.PNG', 0, 0, width=640, height=640)
    addCafeCustomerDesks()
    addCafeKitchenDesksBottom()
    addTrashCan()

    drawSelectionTrashCan()
    drawSelectionIngredient()

    # draw moving amuro
    drawImage('./images/amuroImage.PNG', amuro.playerPosX, amuro.playerPosY, width=128, height=128, align='center')

    addCafeKitchenDesksTop()
    addCafeChairs()

    drawSelectionDesk()

    # print(amuro.playerPosX, amuro.playerPosY)
    # print(amuro.selection)

    drawHoldIngredient()

def game_onStep(app):
    if app.keyHeld in ['up', 'down', 'left', 'right']:
        amuro.move(app.keyHeld)

def game_onKeyPress(app, key):
    app.keyHeld = key
    if key == 'space':
        amuro.doSelectionDesk()
        amuro.doSelectionIngredient()
        amuro.holdIngredients()

    if key == 'escape':
        setActiveScreen('start')

def game_onKeyRelease(app, key):
    if app.keyHeld == key:
        app.keyHeld = None

##########
# draw things

def addCafeCustomerDesks():
    drawImage('./images/desk1Image.PNG', 96, 544, width=64, height=64, align='center')
    drawImage('./images/desk1Image.PNG', 224, 544, width=64, height=64, align='center')
    drawImage('./images/desk1Image.PNG', 352, 544, width=64, height=64, align='center')
    drawImage('./images/desk1Image.PNG', 416, 544, width=64, height=64, align='center')

def addCafeKitchenDesksTop():
    for i in range(224, 417, 64):
        drawImage('./images/desk2TopImage.PNG', i, 288, width=64, height=64, align='center')

def addCafeKitchenDesksBottom():
    drawImage('./images/desk2Image.PNG', 160, 224, width=64, height=64, align='center')
    drawImage('./images/desk2Image.PNG', 160, 288, width=64, height=64, align='center')
    for i in range(224,417,64):
        drawImage('./images/desk2BottomImage.PNG', i, 288, width=64, height=64, align='center')

def addCafeChairs():
    drawImage('./images/chairImage.PNG', 96, 480, width=64, height=64, align='center')
    drawImage('./images/chairImage.PNG', 224, 480, width=64, height=64, align='center')
    drawImage('./images/chairImage.PNG', 352, 480, width=64, height=64, align='center')
    drawImage('./images/chairImage.PNG', 416, 480, width=64, height=64, align='center')

def addTrashCan():
    drawImage('./images/trashcanImage.PNG', 480, 160, width=64, height=64, align='center')

def drawSelectionDesk():
    if amuro.selection != (0,0) and amuro.selection in [(3,4), (4,4), (5,4), (6,4), (2,3)]:
        drawImage('./images/selectionDeskImage.PNG', amuro.selection[0]*64, amuro.selection[1]*64, width=64, height=64, opacity=40)

def drawSelectionTrashCan():
    if amuro.selection == (7,2):
        drawImage('./images/selectionDeskImage.PNG', amuro.selection[0]*64, amuro.selection[1]*64, width=64, height=64, opacity=40)


def drawSelectionIngredient():
    if amuro.selection == (3,2):
        drawImage('./images/selectionFoodImage.PNG', 204, 130, width=64, height=64, opacity=40)
    elif amuro.selection == (3.5,2):
        drawImage('./images/selectionFoodImage.PNG', 228, 130, width=64, height=64, opacity=40)
    elif amuro.selection == (4,2):
        drawImage('./images/selectionFoodImage.PNG', 260, 130, width=64, height=64, opacity=40)
    elif amuro.selection == (4.5,2):
        drawImage('./images/selectionFoodImage.PNG', 284, 130, width=64, height=64, opacity=40)
    elif amuro.selection == (5,2):
        drawImage('./images/selectionFoodImage.PNG', 332, 130, width=64, height=64, opacity=40)
    elif amuro.selection == (5.5,2):
        drawImage('./images/selectionFoodImage.PNG', 356, 130, width=64, height=64, opacity=40)
    elif amuro.selection == (6,2):
        drawImage('./images/selectionFoodImage.PNG', 390, 130, width=64, height=64, opacity=40)

def drawHoldIngredient():
    if amuro.curentHoldIngredient != None:
        drawImage('./images/hold/holdBGImage.PNG', amuro.playerPosX, amuro.playerPosY, width=64, height=64)
        drawImage(amuro.curentHoldIngredient.image, amuro.playerPosX, amuro.playerPosY, width=64, height=64)

def main():
    runAppWithScreens(width=640, height=640, initialScreen='start')

main()