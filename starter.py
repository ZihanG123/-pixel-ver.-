from cmu_graphics import *
from PIL import Image
from urllib.request import urlopen

from player import *
from dish import *
from plate import *
from menu import *
from ingredient import *
from customer import *
from kitchen import *

# All of the images used are drawn by me.
# The images are based on Detective Conan by Gosho Aoyama.

def onAppStart(app):
    app.keyHeld = None

    app.chairs = [(1, 7), (3, 7), (5, 7), (6, 7)]
    app.desks = [(1, 8), (3, 8), (5, 8), (6, 8)]
    app.availableSeating = [(1, 7), (1, 9), (3, 7), (3, 9), (5, 7), (5, 9), (6, 7), (6, 9)]

    # app.currentCustomerStep = 0

    # app.counterCustomer = 0

    app.spriteIndex = 0
    app.counterSprite = 0

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
    addCafeCustomerDesks(app)
    addCafeKitchenDesksBottom()
    addKitchenWareBottom()
    addTrashCan()

    drawSelectionTrashCan()
    drawSelectionIngredient()

    # draw moving amuro
    drawMovingAmuro(app)    

    addCafeKitchenDesksTop()
    addKitchenWareTop()
    addCafeChairs(app)

    drawSelectionDesk()

    #########################
    # print(amuro.playerPosX, amuro.playerPosY)
    # print(amuro.selection)
    # print(amuro.currentHoldIngredient)
    # for utensil in [chopping, pan, fryer]:
    #     print(f'{utensil.name}', utensil.ingredientInside)


    drawHoldIngredient()

    drawPlate()

    drawHoldPlate()

    drawCustomers(app)

    drawSelectionCookFood()

    chopping.drawCookingIngredient()
    pan.drawCookingIngredient()
    fryer.drawCookingIngredient()


def game_onStep(app):
    if app.keyHeld in ['up', 'down', 'left', 'right']:
        amuro.move(app.keyHeld)
        # amuro.loadSpritePilImages()
        amuro.isMoving = True
    else:
        amuro.isMoving = False

    poirotCafe.cafeTime += 1
    print(poirotCafe.cafeTime)
        
    customerControll()

    for i in range(len(poirotCafe.availableSeats)):
        poirotCafe.letCustomerIn()


    # delay 2 seconds to let the customer go into the cafe

    if poirotCafe.cafeTime >= 60:
        for customer in poirotCafe.insideCustomers:
            poirotCafe.recordTimeStep(customer)
            if customer.currentStep < len(customer.pixelPath) - 1:
                customer.currentStep += 1     

    print(poirotCafe.customerTimeStamps)       

    # if app.counterCustomer >= 60:
    #     if app.currentCustomerStep < len(currentCustomer.pixelPath) - 1:
    #         app.currentCustomerStep += 1

    # app.counterCustomer += 1

    if app.counterSprite % 5 == 0:
        app.spriteIndex = (app.spriteIndex + 1) % len(amuro.spriteAnimatedImages)
    app.counterSprite += 1


    for customer in poirotCafe.insideCustomers:
        if customer.ordered == False:
            customer.startToOrder(cafeMenu)

    chopping.cookFood()
    pan.cookFood()
    fryer.cookFood()


def game_onKeyPress(app, key):
    app.keyHeld = key
    if key == 'space':
        amuro.doSelectionDesk()
        amuro.doSelectionIngredient()
        amuro.holdIngredients()
        amuro.makeSandwich()
        amuro.throwAwayPlate()
        amuro.putDownIngredients()

    if key == 'escape':
        setActiveScreen('start')

    if key == 's' or key == 'w':
        if amuro.selection == (5,4):
            amuro.select1selection = (5, amuro.select1selection[1] + 1)
            if amuro.select1selection[1] >= 6:
                amuro.select1selection = (5, 4)
        if amuro.selection == (6,4):
            amuro.select2selection = (6, amuro.select2selection[1] + 1)
            if amuro.select2selection[1] >= 7:
                amuro.select2selection = (6, 4)


    if key == 'enter':
        if (amuro.currentPlate.currentIngredients != [] and amuro.selection == (3,4) and 
            amuro.currentHoldPlate.currentIngredients == []):
            amuro.pickUpDish()
        
        elif (amuro.currentHoldPlate.currentIngredients != [] and amuro.selection == (3,4) and
            amuro.currentPlate.currentIngredients == []):
            amuro.putBackDish()

    if key == 'a':
        amuro.holdFood()

    if key == 'l':
        amuro.doCookFoodSelection()
        amuro.cookFood()
        amuro.pickUpCookedIng()

def game_onKeyRelease(app, key):
    if app.keyHeld == key:
        app.keyHeld = None

##########
# draw things

def addCafeCustomerDesks(app):
    for i in app.desks:
         drawImage('./images/desk1Image.PNG', i[0]*64, i[1]*64, width=64, height=64)

def addCafeKitchenDesksTop():
    for i in range(224, 417, 64):
        drawImage('./images/desk2TopImage.PNG', i, 288, width=64, height=64, align='center')

def addCafeKitchenDesksBottom():
    drawImage('./images/desk2Image.PNG', 160, 224, width=64, height=64, align='center')
    drawImage('./images/desk2Image.PNG', 160, 288, width=64, height=64, align='center')
    for i in range(224,417,64):
        drawImage('./images/desk2BottomImage.PNG', i, 288, width=64, height=64, align='center')

def addCafeChairs(app):
    for i in app.chairs:
        drawImage('./images/chairImage.PNG', i[0]*64, i[1]*64, width=64, height=64)

def addTrashCan():
    drawImage('./images/trashcanImage.PNG', 480, 160, width=64, height=64, align='center')

def addKitchenWareTop():
    drawImage('./images/fryerTopImage.PNG', 6*64, 4*64, width=64, height=64)
    drawImage('./images/panTopImage.PNG', 5*64, 4*64, width=64, height=64)
    drawImage('./images/choppingTopImage.PNG', 4*64, 4*64, width=64, height=64)

def addKitchenWareBottom():
    drawImage('./images/fryerBottomImage.PNG', 6*64, 4*64, width=64, height=64)
    drawImage('./images/panBottomImage.PNG', 5*64, 4*64, width=64, height=64)
    drawImage('./images/choppingBottomImage.PNG', 4*64, 4*64, width=64, height=64)


def drawSelectionDesk():
    if amuro.selection != (0,0) and amuro.selection in [(3,4), (4,4), (5,4), (6,4), (2,3)]:
        drawImage('./images/selectionDeskImage.PNG', amuro.selection[0]*64, amuro.selection[1]*64, width=64, height=64, opacity=40)

    if amuro.selection == (5,4):
        utensil = amuro.selectionToUtensil[(5,4,0)]
        if utensil.ingredientInside == None:
            drawImage('./images/select1Image.PNG', amuro.selection[0]*64, amuro.selection[1]*64, width=64, height=128)
            drawImage('./images/selectionDeskImage.PNG', amuro.select1selection[0]*64, amuro.select1selection[1]*64, width=64, height=64, opacity=40)

    if amuro.selection == (6,4):
        utensil = amuro.selectionToUtensil[(6,4,0)]
        if utensil.ingredientInside == None:
            drawImage('./images/select2Image.PNG', amuro.selection[0]*64, amuro.selection[1]*64, width=64, height=192)
            drawImage('./images/selectionDeskImage.PNG', amuro.select2selection[0]*64, amuro.select2selection[1]*64, width=64, height=64, opacity=40)

def drawSelectionCookFood():
    if amuro.selection != (0,0) and amuro.selection in [(4,4,0), (5,4,0), (6,4,0)]:
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

# draw the ingredient that the player is currently holding
def drawHoldIngredient():
    if (amuro.currentHoldIngredient != None):
        drawImage('./images/hold/holdBGImage.PNG', amuro.playerPosX, amuro.playerPosY, width=64, height=64)
        drawImage(amuro.currentHoldIngredient.image, amuro.playerPosX, amuro.playerPosY, width=64, height=64)

# draw the plate at position (3,4)
def drawPlate():
    if len(amuro.currentPlate.currentIngredients) != 0:
        for item in amuro.currentPlate.currentIngredients:
            drawImage(f'./images/cooked/{item.name}CookedImage.PNG', 3*64, 4*64, width=64, height=64)


# draw the plate when picked up
def drawHoldPlate():
    if len(amuro.currentHoldPlate.currentIngredients) != 0:
        for item in amuro.currentHoldPlate.currentIngredients:
            drawImage(f'./images/cooked/{item.name}CookedImage.PNG', amuro.playerPosX, amuro.playerPosY, width=64, height=64)

def drawCustomers(app):
    # posX, posY = currentCustomer.pixelPath[app.currentCustomerStep]
    # drawImage(currentCustomer.image, posX+35, posY+21, width=128, height=128, align='center')

    for customer in poirotCafe.insideCustomers:

        if poirotCafe.customerTimeStamps != []:
            prevCustomerStamp = poirotCafe.customerTimeStamps[-1]
            if poirotCafe.cafeTime >= prevCustomerStamp + customer.nextCustomerDelay:
                posX, posY = customer.pixelPath[customer.currentStep]
                drawImage(customer.image, posX+35, posY+21, width=128, height=128, align='center')
        else:
            posX, posY = customer.pixelPath[customer.currentStep]
            drawImage(customer.image, posX+35, posY+21, width=128, height=128, align='center')



def customerControll():
    # posX, posY = currentCustomer.pixelPath[app.currentCustomerStep]
    # if (posX, posY) == (currentCustomer.targetX*64, (currentCustomer.targetY+1)*64):
    #     currentCustomer.isSeated = True
    for customer in poirotCafe.insideCustomers:
        posX, posY = customer.pixelPath[customer.currentStep]
        if (posX, posY) == (customer.targetX*64, (customer.targetY+1)*64):
            customer.isSeated = True
            

def drawMovingAmuro(app):
    if amuro.isMoving:
        amuro.loadSpritePilImages()
        amuro.spriteAnimatedImages = [CMUImage(pilImage) for pilImage in amuro.spritePilImages]
        drawImage(amuro.spriteAnimatedImages[app.spriteIndex], amuro.playerPosX, amuro.playerPosY, width=128, height=128, align='center')
    else:
        if amuro.playerDirX == 0 and amuro.playerDirY == 1:
            drawImage('./images/amuroFrontImage.PNG', amuro.playerPosX, amuro.playerPosY-8, width=128, height=128, align='center')
        elif amuro.playerDirX == 0 and amuro.playerDirY == -1:
            drawImage('./images/amuroBackImage.PNG', amuro.playerPosX, amuro.playerPosY, width=128, height=128, align='center')
        elif amuro.playerDirX == 1 and amuro.playerDirY == 0:
            drawImage('./images/amuroRightImage.PNG', amuro.playerPosX, amuro.playerPosY, width=128, height=128, align='center')
        elif amuro.playerDirX == -1 and amuro.playerDirY == 0:
            drawImage('./images/amuroLeftImage.PNG', amuro.playerPosX, amuro.playerPosY, width=128, height=128, align='center')
        elif amuro.playerDirX == 0 and amuro.playerDirY == 0:
            drawImage('./images/amuroFrontImage.PNG', amuro.playerPosX, amuro.playerPosY-8, width=128, height=128, align='center')


###################
def main():
    runAppWithScreens(width=640, height=640, initialScreen='start')

main()