from cmu_graphics import *
from player import *
from PIL import Image

def onAppStart(app):
    app.keyHeld = None

################
# start screen
################

def start_redrawAll(app):
    drawLabel('Welcome!', 200, 160, size=24, bold=True)


def start_onKeyPress(app, key):
    if key == 'space':
        setActiveScreen('game')

################
# game screen
################

def game_redrawAll(app):
    drawImage('./images/cafeImage.PNG', 0, 0, width=640, height=640)
    addCafeCustomerDesks()
    addCafeKitchenDesksBottom()
    addTrashCan()

    drawSelectionTrashCan()
    drawSelectionFood()

    # draw moving amuro
    drawImage('./images/amuroImage.PNG', amuro.playerPosX, amuro.playerPosY, width=128, height=128, align='center')

    addCafeKitchenDesksTop()
    addCafeChairs()

    drawSelectionDesk()

    print(amuro.playerPosX, amuro.playerPosY)
    # print(amuro.selection)

def game_onStep(app):
    if app.keyHeld in ['up', 'down', 'left', 'right']:
        amuro.move(app.keyHeld)

def game_onKeyPress(app, key):
    app.keyHeld = key
    if key == 'space':
        amuro.doSelectionDesk()
        amuro.doSelectionFood()
    if key == 'escape':
        setActiveScreen('start')

def game_onKeyRelease(app, key):
    if app.keyHeld == key:
        app.keyHeld = None


def addCafeCustomerDesks():
    drawImage('./images/desk1Image.PNG', 96, 544, width=64, height=64, align='center')
    drawImage('./images/desk1Image.PNG', 224, 544, width=64, height=64, align='center')
    drawImage('./images/desk1Image.PNG', 352, 544, width=64, height=64, align='center')
    drawImage('./images/desk1Image.PNG', 416, 544, width=64, height=64, align='center')

def addCafeKitchenDesksTop():
    drawImage('./images/desk2TopImage.PNG', 224, 288, width=64, height=64, align='center')
    drawImage('./images/desk2TopImage.PNG', 288, 288, width=64, height=64, align='center')
    drawImage('./images/desk2TopImage.PNG', 352, 288, width=64, height=64, align='center')
    drawImage('./images/desk2TopImage.PNG', 416, 288, width=64, height=64, align='center')

def addCafeKitchenDesksBottom():
    drawImage('./images/desk2Image.PNG', 160, 224, width=64, height=64, align='center')
    drawImage('./images/desk2Image.PNG', 160, 288, width=64, height=64, align='center')
    drawImage('./images/desk2BottomImage.PNG', 224, 288, width=64, height=64, align='center')
    drawImage('./images/desk2BottomImage.PNG', 288, 288, width=64, height=64, align='center')
    drawImage('./images/desk2BottomImage.PNG', 352, 288, width=64, height=64, align='center')
    drawImage('./images/desk2BottomImage.PNG', 416, 288, width=64, height=64, align='center')

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


def drawSelectionFood():
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


def main():
    runAppWithScreens(width=640, height=640, initialScreen='start')
    # runApp(width=640, height=640)



amuro = Player(32, 280, 'amuro')
amuro.getCafeValidMovement()



main()