from cmu_graphics import *
from PIL import Image
from plate import *
from dish import *
from ingredient import *
from kitchen import *
from customer import *

from cmu_graphics import *
from PIL import Image


# class for the character the player is controlling
class Player():

    # initialize player
    def __init__(self, playerPosX, playerPosY, name):
        self.playerDirX, self.playerDirY = 0, 0
        self.playerPosX = playerPosX
        self.playerPosY = playerPosY
        self.name = name
        self.speed = 8
        self.isMoving = False
        self.validSpaceImage = CMUImage(Image.open('./images/cafeValidMovementImage.PNG'))
        self.validBoard = [[1]*640 for row in range(640)]
        self.selection = (0,0)

        self.select1selection = (5,4)
        self.select2selection = (6,4)

        # the plate on the table
        self.currentPlate = Plate()
        self.currentHoldPlate = Plate()

        self.currentHoldIngredient = None


        self.validIngredientSelection = [(3,2), (3.5,2), (4,2), (4.5,2), (5,2), (5.5,2), (6,2)]
        self.ingredientToSelection = {ketchup:(3,2), curry:(3.5,2), bread:(4,2), mayonnaise:(4.5,2), 
                                      ham:(5,2), lettuce:(5.5,2), plate:(6,2), rice:(5,4), 
                                      spaghetti:(5,5), tonkatsu:(6,4), chicken:(6,5), tempura:(6,6)}
        self.selectionToIngredient = {(3,2):ketchup, (3.5,2):curry, (4,2):bread, (4.5,2):mayonnaise, 
                                      (5,2):ham, (5.5,2):lettuce, (6,2):plate, (5,4):rice, (5,5):spaghetti, 
                                      (6,4):tonkatsu, (6,5):chicken, (6,6):tempura}
        
        self.validDeskSelection = [(3,4), (4,4), (5,4), (6,4)]
        
        self.deskSelections = [
        {'posX':(216,256), 'posY':(224,240), 'dirX':0, 'dirY':1, 'selection':(3,4)},
        {'posX':(264,320), 'posY':(224,240), 'dirX':0, 'dirY':1, 'selection':(4,4)},
        {'posX':(328,384), 'posY':(224,240), 'dirX':0, 'dirY':1, 'selection':(5,4)},
        {'posX':(392,448), 'posY':(224,240), 'dirX':0, 'dirY':1, 'selection':(6,4)},
        {'posX':(216,232), 'posY':(192,240), 'dirX':-1, 'dirY':0, 'selection':(2,3)},
        {'posX':(464,512), 'posY':(184,224), 'dirX':0, 'dirY':-1, 'selection':(7,2)},
        {'posX':(528,536), 'posY':(120,176), 'dirX':-1, 'dirY':0, 'selection':(7,2)},]

        self.ingredientSelections = [
        {'posX':(216,224), 'posY':(184,216), 'dirX':0, 'dirY':-1, 'selection':(3,2)},
        {'posX':(232,256), 'posY':(184,216), 'dirX':0, 'dirY':-1, 'selection':(3.5,2)},
        {'posX':(264,288), 'posY':(184,216), 'dirX':0, 'dirY':-1, 'selection':(4,2)},
        {'posX':(296,320), 'posY':(184,216), 'dirX':0, 'dirY':-1, 'selection':(4.5,2)},
        {'posX':(328,352), 'posY':(184,216), 'dirX':0, 'dirY':-1, 'selection':(5,2)},
        {'posX':(360,384), 'posY':(184,216), 'dirX':0, 'dirY':-1, 'selection':(5.5,2)},
        {'posX':(392,416), 'posY':(184,216), 'dirX':0, 'dirY':-1, 'selection':(6,2)},]

        self.spritePilImages = []
        self.spriteAnimatedImages = []
        self.loadSpritePilImages()
        self.spriteAnimatedImages = [CMUImage(pilImage) for pilImage in self.spritePilImages]

        self.customerDeskSelections = [
        {'posX':(464,472), 'posY':(504,568), 'dirX':-1, 'dirY':0, 'selection':(6,8)},
        {'posX':(392,456), 'posY':(560,568), 'dirX':0, 'dirY':-1, 'selection':(6,8)},
        {'posX':(320,384), 'posY':(560,568), 'dirX':0, 'dirY':-1, 'selection':(5,8)},
        {'posX':(296,304), 'posY':(504,568), 'dirX':1, 'dirY':0, 'selection':(5,8)},
        {'posX':(192,264), 'posY':(560,568), 'dirX':0, 'dirY':-1, 'selection':(3,8)},
        {'posX':(272,288), 'posY':(504,568), 'dirX':-1, 'dirY':0, 'selection':(3,8)},
        {'posX':(160,176), 'posY':(504,568), 'dirX':1, 'dirY':0, 'selection':(3,8)},
        {'posX':(64,136), 'posY':(560,568), 'dirX':0, 'dirY':-1, 'selection':(1,8)},
        {'posX':(144,160), 'posY':(504,568), 'dirX':-1, 'dirY':0, 'selection':(1,8)},
        {'posX':(32,48), 'posY':(504,568), 'dirX':1, 'dirY':0, 'selection':(1,8)},]

        self.cookFoodSelections = [
        {'posX':(264,320), 'posY':(224,240), 'dirX':0, 'dirY':1, 'selection':(4,4,0)},
        {'posX':(328,384), 'posY':(224,240), 'dirX':0, 'dirY':1, 'selection':(5,4,0)},
        {'posX':(392,448), 'posY':(224,240), 'dirX':0, 'dirY':1, 'selection':(6,4,0)},]

        self.utensilToSelection = {chopping:(4,4,0), pan:(5,4,0), fryer:(6,4,0)}
        self.selectionToUtensil = {(4,4,0):chopping, (5,4,0):pan, (6,4,0):fryer}
        self.nameToUtensil = {'chopping':chopping, 'pan':pan, 'fryer':fryer}

        self.servedCustomerNum = 0

        self.startCustomerDialogue = False

    
    # move the player
    def move(self,key):
        if key not in ['up','down','left','right']:
            pass
        if key == 'up':
            self.playerDirX, self.playerDirY = 0, -1
        elif key == 'down':
            self.playerDirX, self.playerDirY = 0, 1
        elif key == 'left':
            self.playerDirX, self.playerDirY = -1, 0
        elif key == 'right':
            self.playerDirX, self.playerDirY = 1, 0

        newPosX = self.playerPosX + self.playerDirX * self.speed
        newPosY = self.playerPosY + self.playerDirY * self.speed
        if 0 <= newPosX < len(self.validBoard) and 0 <= newPosY < len(self.validBoard[0]):
            if self.validBoard[newPosX][newPosY] == 1:
                self.playerPosX = newPosX
                self.playerPosY = newPosY

    # this part of the code referenced the TP-related demos in the course notes
    def loadSpritePilImages(self):
        spritestrip = Image.open('./images/amuroAnimationFrontImage.PNG')
        self.spritePilImages = []
        if self.playerDirX == 0 and self.playerDirY == 1:
            spritestrip = Image.open('./images/amuroAnimationFrontImage.PNG')
        elif self.playerDirX == 0 and self.playerDirY == -1:
            spritestrip = Image.open('./images/amuroAnimationBackImage.PNG')
        elif self.playerDirX == 1 and self.playerDirY == 0:
            spritestrip = Image.open('./images/amuroAnimationRightImage.PNG')
        elif self.playerDirX == -1 and self.playerDirY == 0:
            spritestrip = Image.open('./images/amuroAnimationLeftImage.PNG')
        
                
        spritestrip = spritestrip.resize((512,128))
        for i in range(4):
            spriteImage = spritestrip.crop((0+128*i, 0, 128+128*i, 128))
            self.spritePilImages.append(spriteImage)
        return self.spritePilImages


    # get the valid coordinates that the player can move
    def getCafeValidMovement(self):
        validSpaceImg = Image.open('./images/cafeValidMovementImage.PNG')
        # print(validSpaceImg.width, validSpaceImg.height)
        validSpaceImg = validSpaceImg.resize((640,640))
        # print(validSpaceImg.width, validSpaceImg.height)
        for x in range(validSpaceImg.width):
            for y in range(validSpaceImg.height):
                pixel = validSpaceImg.getpixel((x, y))
                if pixel == (0,0,0,0):
                    self.validBoard[x][y] = 0

    # select the desk
    def doSelectionDesk(self):
        for desk in self.deskSelections:
            if (desk['posX'][0] <= self.playerPosX <= desk['posX'][1] and
                desk["posY"][0] <= self.playerPosY <= desk["posY"][1] and
                self.playerDirX == desk['dirX'] and self.playerDirY == desk['dirY']):
                
                if self.selection == (0, 0):
                    self.selection = desk['selection']
                else:
                    self.selection = (0, 0)
                break

    # select the ingredient 
    def doSelectionIngredient(self):
        for ingredient in self.ingredientSelections:
            if self.playerDirX == 0 and self.playerDirY == -1:
                if (ingredient['posX'][0] <= self.playerPosX <= ingredient['posX'][1] and
                    ingredient['posY'][0] <= self.playerPosY <= ingredient['posY'][1]):
                    if self.selection == (0, 0):
                        self.selection = ingredient['selection']
                    else:
                        self.selection = (0, 0)
                    break

    def doSelectCustomerDesk(self):
        for desk in self.customerDeskSelections:
            if (desk['posX'][0] <= self.playerPosX <= desk['posX'][1] and
                desk["posY"][0] <= self.playerPosY <= desk["posY"][1] and
                self.playerDirX == desk['dirX'] and self.playerDirY == desk['dirY']):
                
                if self.selection == (0, 0):
                    self.selection = desk['selection']
                else:
                    self.selection = (0, 0)
                break


    # throw away the current plate
    def throwAwayPlate(self):
        if self.selection == (7,2):
            self.currentHoldPlate.throwAway()
            if self.currentHoldIngredient != None:
                self.currentHoldIngredient.isCooking = False
                self.currentHoldIngredient.inUtensil = False
                self.currentHoldIngredient.cookedOnce = False
                if self.currentHoldIngredient.name in ['ketchup', 'curry', 'mayonnaise', 'plate']:
                    self.currentHoldIngredient.cooked =  True
                else:
                    self.currentHoldIngredient.cooked = False
                self.currentHoldIngredient = None


    # pick up ingredients
    # only one ingredient can be held at a time
    def holdIngredients(self):
        if self.selection in self.validIngredientSelection:
            if self.currentHoldIngredient == None:

                # ingredient1 will output the ingredient
                ingredient1 = self.selectionToIngredient[self.selection]
                self.currentHoldIngredient = ingredient1

            
            else:
                # get the selection of the ingredient the player currently has
                # temp2 will output the selection of this ingredient
                selection1 = self.ingredientToSelection[self.currentHoldIngredient]
                if self.selection == selection1 and self.validUnselection():
                    # self.selection = (0,0)
                    self.currentHoldIngredient = None
        
    # check to see if the unselection is valid
    def validUnselection(self):
        if self.selection in self.validIngredientSelection:
            for ingredient in self.ingredientSelections:
                if (ingredient['posX'][0] <= self.playerPosX <= ingredient['posX'][1] and
                    ingredient['posY'][0] <= self.playerPosY <= ingredient['posY'][1] and
                    self.playerDirX == ingredient['dirX'] and self.playerDirY == ingredient['dirY']):

                    if self.selection == ingredient['selection']:
                        return True
                    
            return False
        elif self.selection in self.validDeskSelection:
            for desk in self.deskSelections:
                if (desk['posX'][0] <= self.playerPosX <= desk['posX'][1] and
                    desk['posY'][0] <= self.playerPosY <= desk['posY'][1] and
                    self.playerDirX == desk['dirX'] and self.playerDirY == desk['dirY']):
                    if self.selection == (5,4):
                        if self.currentHoldIngredient == self.selectionToIngredient[self.select1selection]:
                            return True
                    elif self.selection == (6,4):
                        if self.currentHoldIngredient == self.selectionToIngredient[self.select2selection]:
                            return True
            return False
        return False


    # put the ingredient currently have to the table (3,4)
    # needs to have a plate
    def makeSandwich(self):
        if self.selection == (0,0):
            pass

        # make sandwich
        # ingredients have to be put in order
        if self.currentHoldIngredient != None and self.selection == (3,4):
            nextIndex = len(self.currentPlate.currentIngredients)
            if nextIndex < len(sandwich.ingredientsNeeded):
                requiredIngredient = sandwich.ingredientsNeeded[nextIndex]
                if self.currentHoldIngredient == requiredIngredient:
                    self.currentPlate.addIngredients(self.currentHoldIngredient)
                    self.currentHoldIngredient = None

    # pick up the dish currently have to the table (3,4)
    def pickUpDish(self):
        if (self.currentPlate.currentIngredients != [] and self.selection in [(3,4), (1,8), (3,8), (5,8), (6,8)] and 
            self.currentHoldPlate.currentIngredients == []):

            self.currentHoldPlate = self.currentPlate
            self.currentPlate = Plate()

    # put back the dish to the table (3,4)
    def putBackDish(self):
        if (self.currentHoldPlate.currentIngredients != []):
            if self.selection == (3,4) and self.currentPlate.currentIngredients == []:

                self.currentPlate = self.currentHoldPlate
                self.currentHoldPlate = Plate()
                self.currentPlate.posX = self.selection[0]
                self.currentPlate.posY = self.selection[1]
            elif self.selection in [(1,8), (3,8), (5,8), (6,8)]:
                for customer in poirotCafe.insideCustomers:
                    if self.selection[0] == customer.seat[0] and self.selection[1]-1 == customer.seat[1]:
                        if customer.currDishOnDesk == Plate():
                            
                            for dish in customer.orderDishes:
                                if self.currentHoldPlate == dish:
                                    customer.currDishOnDesk = self.currentHoldPlate
                                    customer.currDishOnDesk.posX, customer.currDishOnDesk.posY = self.selection[0], self.selection[1]
                                    self.currentHoldPlate = Plate()
                                    customer.eatingTimeStamps = poirotCafe.cafeTime
                                    print(customer.currDishOnDesk)
                                    print(customer.eatingTimeStamps)
                                    break

                


    def updateDish(self):
        if self.selection in [(3,4), (1,8), (3,8), (5,8), (6,8)]:
            self.currentPlate.posX = self.selection[0]
            self.currentPlate.posY = self.selection[1]

    def holdFood(self):
        if self.selection in self.validDeskSelection:
            if self.selection == (5,4):
                if self.currentHoldIngredient == None:

                    ingredient1 = self.selectionToIngredient[self.select1selection]
                    self.currentHoldIngredient = ingredient1

                else:
                    selection1 = self.ingredientToSelection[self.currentHoldIngredient]
                    if self.select1selection == selection1 and self.validUnselection():
                        self.currentHoldIngredient = None
            elif self.selection == (6,4):
                if self.currentHoldIngredient == None:

                    ingredient1 = self.selectionToIngredient[self.select2selection]
                    self.currentHoldIngredient = ingredient1
                
                else:
                    selection1 = self.ingredientToSelection[self.currentHoldIngredient]
                    if self.select2selection == selection1 and self.validUnselection():
                        self.currentHoldIngredient = None

    def putDownIngredients(self):
        if self.selection == (0,0):
            pass

        if (self.currentHoldIngredient != None and 
            self.currentPlate.currentIngredients != [] and 
            self.selection == (3,4)):
            if (self.currentPlate.currentIngredients[0] == plate and 
                self.currentHoldIngredient not in self.currentPlate.currentIngredients):
                self.currentPlate.addIngredients(self.currentHoldIngredient)
                self.currentHoldIngredient = None

    def doCookFoodSelection(self):
        for desk in self.cookFoodSelections:
            if (desk['posX'][0] <= self.playerPosX <= desk['posX'][1] and
                desk["posY"][0] <= self.playerPosY <= desk["posY"][1] and
                self.playerDirX == desk['dirX'] and self.playerDirY == desk['dirY']):
                
                if self.selection == (0, 0):
                    self.selection = desk['selection']
                else:
                    self.selection = (0, 0)
                break

    def cookFood(self):
        # print('self.selection', self.selection)
        # print('self.currentHoldIngredient', self.currentHoldIngredient)
        if (self.selection in [(4,4,0), (5,4,0), (6,4,0)] and 
            self.currentHoldIngredient != None):
            if not self.currentHoldIngredient.cooked:
                if self.currentHoldIngredient.cookingUtensil != None:
                    utensil = self.nameToUtensil[self.currentHoldIngredient.cookingUtensil]
                    if self.selection == utensil.selectionCoor:
                        if not utensil.isCooking:
                            self.currentHoldIngredient.isCooking = True
                            self.currentHoldIngredient.inUtensil = True
                            utensil.isCooking = True
                            utensil.ingredientInside = self.currentHoldIngredient
                            self.currentHoldIngredient = None
                            # print(self.currentHoldIngredient.cookingUtensil.isCooking)

    def pickUpCookedIng(self):
        if self.selection in [(4,4,0), (5,4,0), (6,4,0)]:
            utensil = self.selectionToUtensil[self.selection]
            # print('curr utensil.........',utensil.name, utensil.isCooking)
            if self.currentHoldIngredient == None:
                if not utensil.isCooking and utensil.ingredientInside != None:
                    utensil.ingredientInside.inUtensil = False
                    self.currentHoldIngredient = utensil.ingredientInside
                    utensil.ingredientInside = None

    def startDialogue(self):
        if self.selection in [(1,8), (3,8), (5,8), (6,8)]:
            self.startCustomerDialogue = not self.startCustomerDialogue


#######
# initialize player
#######

# amuro = Player(32, 280, 'amuro')
amuro = Player(480, 216, 'amuro')
amuro.getCafeValidMovement()