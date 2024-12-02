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
    app.stepsPerSecond = 10

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

    drawSelectionCustomerDesk()

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

    drawCustomersWalkingIn()

    drawSelectionCookFood()

    drawCookingIngredient(chopping)
    drawCookingIngredient(pan)
    drawCookingIngredient(fryer)

    # chopping.drawCookingIngredient()
    # pan.drawCookingIngredient()
    # fryer.drawCookingIngredient()

    drawTakeCustomerOrder()

    checkCurrDishOnDesk()

    drawCustomerLeaving()


def game_onStep(app):
    if app.keyHeld in ['up', 'down', 'left', 'right']:
        amuro.move(app.keyHeld)
        # amuro.loadSpritePilImages()
        amuro.isMoving = True
    else:
        amuro.isMoving = False

    poirotCafe.cafeTime += 1
    # print(poirotCafe.cafeTime)
        
    for i in range(len(poirotCafe.availableSeats)):
        poirotCafe.letCustomerIn()
    # print(poirotCafe.nextCustomers)

    if len(poirotCafe.nextCustomers) > 0:
        poirotCafe.currWalkingInCustomer = poirotCafe.nextCustomers[-1]
    
    # print(poirotCafe.currWalkingInCustomer)
    # if poirotCafe.currWalkingInCustomer != None:
        # print(poirotCafe.currWalkingInCustomer.isSeated)

    customerControll()

    # delay 2 seconds to let the customer go into the cafe

    if poirotCafe.cafeTime >= 20:
        customer = poirotCafe.currWalkingInCustomer
        if customer.currentStep < len(customer.pixelPath) - 1:
            if poirotCafe.customerTimeStamps == []:
                customer.currentStep += 1
            else:
                prevCustomerStamp = poirotCafe.customerTimeStamps[-1]
                if poirotCafe.cafeTime >= prevCustomerStamp + customer.nextCustomerDelay:
                    customer.currentStep += 1

    if poirotCafe.currLeavingCustomer != None:
        customer = poirotCafe.currLeavingCustomer
        if customer.currentStepLeaving < len(customer.pixelPath) - 1:
            customer.currentStepLeaving += 1

    # print(poirotCafe.customerTimeStamps)       

    # if app.counterCustomer >= 60:
    #     if app.currentCustomerStep < len(currentCustomer.pixelPath) - 1:
    #         app.currentCustomerStep += 1

    # app.counterCustomer += 1

    if app.counterSprite % 2 == 0:
        app.spriteIndex = (app.spriteIndex + 1) % len(amuro.spriteAnimatedImages)
    app.counterSprite += 1


    for customer in poirotCafe.insideCustomers:

        poirotCafe.recordTimeStep(customer)

        if customer.ordered == False:
            customer.startToOrder(cafeMenu)
        
        poirotCafe.letCustomerLeave(customer)

    customerControllLeaving()

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
        amuro.doSelectCustomerDesk()

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
        if (amuro.currentPlate.currentIngredients != [] and 
            amuro.selection in [(3,4), (1,8), (3,8), (5,8), (6,8)] and 
            amuro.currentHoldPlate.currentIngredients == []):
            # amuro.updateDish()
            amuro.pickUpDish()
        
        elif (amuro.currentHoldPlate.currentIngredients != [] and 
            amuro.selection in [(3,4), (1,8), (3,8), (5,8), (6,8)] and
            amuro.currentPlate.currentIngredients == []):
            # amuro.updateDish()
            amuro.putBackDish()

    if key == 'a':
        amuro.holdFood()

    if key == 'l':
        amuro.doCookFoodSelection()
        amuro.cookFood()
        amuro.pickUpCookedIng()
        amuro.startDialogue()

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

def drawSelectionCustomerDesk():
    if amuro.selection != (0,0) and amuro.selection in [(1,8), (3,8), (5,8), (6,8)]:
        drawImage('./images/selectionDeskImage.PNG', amuro.selection[0]*64, amuro.selection[1]*64, width=64, height=64, opacity=40)

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
            drawImage(f'./images/cooked/{item.name}CookedImage.PNG', amuro.currentPlate.posX*64, amuro.currentPlate.posY*64, width=64, height=64)


# draw the plate when picked up
def drawHoldPlate():
    if len(amuro.currentHoldPlate.currentIngredients) != 0:
        for item in amuro.currentHoldPlate.currentIngredients:
            drawImage(f'./images/cooked/{item.name}CookedImage.PNG', amuro.playerPosX, amuro.playerPosY, width=64, height=64)

def drawCustomersWalkingIn():

    customer = poirotCafe.currWalkingInCustomer
    if customer != None:
        if not customer.isSeated:
            if poirotCafe.customerTimeStamps != []:
                prevCustomerStamp = poirotCafe.customerTimeStamps[-1]
                if poirotCafe.cafeTime >= prevCustomerStamp + customer.nextCustomerDelay:
                    posX, posY = customer.pixelPath[customer.currentStep]
                    drawImage(customer.image, posX+35, posY+21, width=128, height=128, align='center')
            else:
                posX, posY = customer.pixelPath[customer.currentStep]
                drawImage(customer.image, posX+35, posY+21, width=128, height=128, align='center')


    for insideSeatedCustomer in poirotCafe.insideCustomers:
        posX, posY = insideSeatedCustomer.pixelPath[-1]
        drawImage(insideSeatedCustomer.image, posX+35, posY+21, width=128, height=128, align='center')

def drawCustomerLeaving():

    customer = poirotCafe.currLeavingCustomer
    if customer != None:
        # print(f'{customer.name} is leaving')
        # print('............', len(customer.pixelPathLeave))
        # print('currentStepLeaving', customer.currentStepLeaving)
        if customer.currentStepLeaving > 0:
            posX, posY = customer.pixelPathLeave[customer.currentStepLeaving]
            drawImage(customer.image, posX+35, posY+21, width=128, height=128, align='center')


def drawCustomersEating(app):
    pass


def customerControll():
    # posX, posY = currentCustomer.pixelPath[app.currentCustomerStep]
    # if (posX, posY) == (currentCustomer.targetX*64, (currentCustomer.targetY+1)*64):
    #     currentCustomer.isSeated = True
    customer = poirotCafe.currWalkingInCustomer
    posX, posY = customer.pixelPath[customer.currentStep]
    if (posX, posY) == (customer.targetX*64, (customer.targetY+1)*64):
        customer.isSeated = True
        poirotCafe.insideCustomers.append(customer)
        poirotCafe.walkInOneByOne()

def customerControllLeaving():
    customer = poirotCafe.currLeavingCustomer
    if customer != None:
        if customer in poirotCafe.insideCustomers:
            poirotCafe.insideCustomers.remove(customer)
        # print('len customer.pixelPathLeave', len(customer.pixelPathLeave))
        # print('customer.currentStepLeaving', customer.currentStepLeaving)
        posX, posY = customer.pixelPathLeave[customer.currentStepLeaving]
        if (posX, posY) == (customer.pixelPathLeave[-1][0], customer.pixelPathLeave[-1][1]):
            customer.hasLeft = True
            customer.isSeated = False
            print('customer has left?', customer.hasLeft)

            if customer in poirotCafe.nextCustomers:
                poirotCafe.nextCustomers.remove(customer)

            if customer not in poirotCafe.queue:
                poirotCafe.queue.append(customer)
            if customer.seat in poirotCafe.occupiedSeats:
                poirotCafe.occupiedSeats.remove(customer.seat)
            print('occupied seats:????', poirotCafe.occupiedSeats)

            if customer.seat not in poirotCafe.availableSeats:
                poirotCafe.availableSeats.append(customer.seat)
            if customer.hasLeft:
                poirotCafe.currLeavingCustomer = None

            customer.resetCustomer()



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

def drawTakeCustomerOrder():
    if (poirotCafe.insideCustomers != [] and 
        amuro.selection in [(1,8), (3,8), (5,8), (6,8)] and 
        amuro.startCustomerDialogue):
        for customer in poirotCafe.insideCustomers:
            if amuro.selection[0] == customer.seat[0] and amuro.selection[1]-1 == customer.seat[1]:
                drawImage('./images/dialogueImage.PNG', 0, 0, width=640, height=640)
                drawLabel('I would like ', 8, 576+10, size=16, font='monospace', align='left', bold=True)
                i = 14
                for dish in customer.orderDishes:
                    drawLabel(f' - {str(dish)}', 8, 576+8+i, size=16, font='monospace', align='left', bold=True)
                    i += 14

def checkCurrDishOnDesk():
    for customer in poirotCafe.insideCustomers:
        if (customer.currDishOnDesk != Plate()):
            if customer.eatingTimeStamps != None:
                if poirotCafe.cafeTime <= customer.eatingTimeStamps + customer.eatingTime*10:
                    for item in customer.currDishOnDesk.currentIngredients:
                        drawImage(f'./images/cooked/{item.name}CookedImage.PNG', customer.currDishOnDesk.posX*64, customer.currDishOnDesk.posY*64, width=64, height=64)
                else:
                    customer.eatingTimeStamps = None
                    for dish in customer.orderDishes:
                        if customer.currDishOnDesk == dish:
                            customer.orderDishes.remove(dish)
                    customer.eaten += 1
                    print(f'{customer.name} ate {customer.eaten} dish(es)')
                    customer.currDishOnDesk = Plate()


def drawCookingIngredient(utensil):
        # print(f'{self.name}', self.ingredientInside)
        if utensil.ingredientInside != None:
            currCookingIng = utensil.ingredientInside
            drawImage(currCookingIng.image, utensil.selectionCoor[0]*64, utensil.selectionCoor[1]*64, width=64, height=64)
            if not currCookingIng.cookedOnce:
                if currCookingIng.cookTime-utensil.cookingCounterSeconds > 0:
                    drawLabel(str(currCookingIng.cookTime-utensil.cookingCounterSeconds), 
                        utensil.selectionCoor[0]*64+8, utensil.selectionCoor[1]*64+8, 
                        size=20, align='center', font='monospace', bold=True, fill='white')



###################
def main():
    runAppWithScreens(width=640, height=640, initialScreen='start')

main()