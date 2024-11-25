from cmu_graphics import *
from PIL import Image
from plate import *
from dish import *
from ingredient import *


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
        self.validSpaceImage = './images/cafeValidMovementImage.PNG'
        self.validBoard = [[1]*640 for row in range(640)]
        self.selection = (0,0)

        self.select1selection = (5,4)
        self.select2selection = (6,4)

        # the plate on the table
        self.currentPlate = Plate()
        self.currentHoldPlate = Plate()

        self.curentHoldIngredient = None


        self.validIngredientSelection = [(3,2), (3.5,2), (4,2), (4.5,2), (5,2), (5.5,2), (6,2)]
        self.ingredientToSelection = {'ketchup':(3,2), 'curry':(3.5,2), 'bread':(4,2), 'mayonnaise':(4.5,2), 
                                      'ham':(5,2), 'lettuce':(5.5,2), 'plate':(6,2), 'rice':(5,4), 
                                      'spaghetti':(5,5), 'tonkatsu':(6,4), 'chicken':(6,5), 'tempura':(6,6)}
        self.selectionToIngredient = {(3,2):'ketchup', (3.5,2):'curry', (4,2):'bread', (4.5,2):'mayonnaise', 
                                      (5,2):'ham', (5.5,2):'lettuce', (6,2):'plate', (5,4):'rice', (5,5):'spaghetti', 
                                      (6,4):'tonkatsu', (6,5):'chicken', (6,6):'tempura'}
        
        self.validDeskSelection = [(3,4), (4,4), (5,4), (6,4)]
        
        self.deskSelections = [
        {'posX': (216, 256), 'posY': (224, 240), 'dirX': 0, 'dirY': 1, 'selection': (3, 4)},
        {'posX': (264, 320), 'posY': (224, 240), 'dirX': 0, 'dirY': 1, 'selection': (4, 4)},
        {'posX': (328, 384), 'posY': (224, 240), 'dirX': 0, 'dirY': 1, 'selection': (5, 4)},
        {'posX': (392, 448), 'posY': (224, 240), 'dirX': 0, 'dirY': 1, 'selection': (6, 4)},
        {'posX': (216, 232), 'posY': (192, 240), 'dirX': -1, 'dirY': 0, 'selection': (2, 3)},
        {'posX': (464, 512), 'posY': (184, 224), 'dirX': 0, 'dirY': -1, 'selection': (7, 2)},
        {'posX': (528, 536), 'posY': (120, 176), 'dirX': -1, 'dirY': 0, 'selection': (7, 2)},]

        self.ingredientSelections = [
        {'posX': (216, 224), 'posY': (184, 216), 'dirX': 0, 'dirY': -1, 'selection': (3, 2)},
        {'posX': (232, 256), 'posY': (184, 216), 'dirX': 0, 'dirY': -1, 'selection': (3.5, 2)},
        {'posX': (264, 288), 'posY': (184, 216), 'dirX': 0, 'dirY': -1, 'selection': (4, 2)},
        {'posX': (296, 320), 'posY': (184, 216), 'dirX': 0, 'dirY': -1, 'selection': (4.5, 2)},
        {'posX': (328, 352), 'posY': (184, 216), 'dirX': 0, 'dirY': -1, 'selection': (5, 2)},
        {'posX': (360, 384), 'posY': (184, 216), 'dirX': 0, 'dirY': -1, 'selection': (5.5, 2)},
        {'posX': (392, 416), 'posY': (184, 216), 'dirX': 0, 'dirY': -1, 'selection': (6, 2)},]

        self.spritePilImages = []
        self.spriteAnimatedImages = []
        self.loadSpritePilImages()
        self.spriteAnimatedImages = [CMUImage(pilImage) for pilImage in self.spritePilImages]

        self.customerDeskSelections = [
        {'posX': (464, 480), 'posY': (504, 568), 'dirX': -1, 'dirY': 0, 'selection': (6, 8)},
        {'posX': (392, 480), 'posY': (560, 568), 'dirX': 0, 'dirY': -1, 'selection': (6, 8)},
        {'posX': (296, 384), 'posY': (560, 568), 'dirX': 0, 'dirY': -1, 'selection': (5, 8)},
        {'posX': (296, 384), 'posY': (560, 568), 'dirX': 0, 'dirY': -1, 'selection': (5, 8)}
        ]
    
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

    def loadSpritePilImages(self):
        spritestrip = Image.open('./images/amuroAnimationImage.PNG')
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
            if (ingredient['posX'][0] <= self.playerPosX <= ingredient['posX'][1] and
                ingredient['posY'][0] <= self.playerPosY <= ingredient['posY'][1] and
                self.playerDirX == ingredient['dirX'] and self.playerDirY == ingredient['dirY']):

                if self.selection == (0, 0):
                    self.selection = ingredient['selection']
                else:
                    self.selection = (0, 0)
                break

    # throw away the current plate
    def throwAwayPlate(self):
        if self.selection == (7,2):
            self.currentHoldPlate.throwAway()

    # pick up ingredients
    # only one ingredient can be held at a time
    def holdIngredients(self):
        if self.selection in self.validIngredientSelection:
            if self.curentHoldIngredient == None:

                # ingredient1 will output the ingredient name
                ingredient1 = self.selectionToIngredient[self.selection]
                self.curentHoldIngredient = Ingredient(ingredient1)

            
            else:
                # get the selection of the ingredient the player currently has
                # temp2 will output the selection of this ingredient
                selection1 = self.ingredientToSelection[self.curentHoldIngredient.name]
                if self.selection == selection1 and self.validUnselection():
                    # self.selection = (0,0)
                    self.curentHoldIngredient = None
        
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
                        if self.curentHoldIngredient.name == self.selectionToIngredient[self.select1selection]:
                            return True
                    elif self.selection == (6,4):
                        if self.curentHoldIngredient.name == self.selectionToIngredient[self.select2selection]:
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
        if self.curentHoldIngredient != None and self.selection == (3,4):
            nextIndex = len(self.currentPlate.currentIngredients)
            if nextIndex < len(sandwich.ingredientsNeeded):
                requiredIngredient = sandwich.ingredientsNeeded[nextIndex]
                if self.curentHoldIngredient == requiredIngredient:
                    self.currentPlate.addIngredients(self.curentHoldIngredient)
                    self.curentHoldIngredient = None

    # pick up the dish currently have to the table (3,4)
    def pickUpDish(self):
        if (self.currentPlate.currentIngredients != [] and self.selection == (3,4) and 
            self.currentHoldPlate.currentIngredients == []):

            self.currentHoldPlate = self.currentPlate
            self.currentPlate = Plate()

    # put back the dish to the table (3,4)
    def putBackDish(self):
        if (self.currentHoldPlate.currentIngredients != [] and self.selection == (3,4) and
            self.currentPlate.currentIngredients == []):

            self.currentPlate = self.currentHoldPlate
            self.currentHoldPlate = Plate()

    def holdFood(self):
        if self.selection in self.validDeskSelection:
            if self.selection == (5,4):
                if self.curentHoldIngredient == None:

                    ingredient1 = self.selectionToIngredient[self.select1selection]
                    self.curentHoldIngredient = Ingredient(ingredient1)

                else:
                    selection1 = self.ingredientToSelection[self.curentHoldIngredient.name]
                    if self.select1selection == selection1 and self.validUnselection():
                        self.curentHoldIngredient = None
            elif self.selection == (6,4):
                if self.curentHoldIngredient == None:

                    ingredient1 = self.selectionToIngredient[self.select2selection]
                    self.curentHoldIngredient = Ingredient(ingredient1)
                
                else:
                    selection1 = self.ingredientToSelection[self.curentHoldIngredient.name]
                    if self.select2selection == selection1 and self.validUnselection():
                        self.curentHoldIngredient = None

    def putDownIngredients(self):
        if self.selection == (0,0):
            pass

        if self.curentHoldIngredient != None and self.currentPlate.currentIngredients != [] and self.selection == (3,4):
            if self.currentPlate.currentIngredients[0] == plate and self.curentHoldIngredient not in self.currentPlate.currentIngredients:
                self.currentPlate.addIngredients(self.curentHoldIngredient)
                self.curentHoldIngredient = None

#######
# initialize player
#######

# amuro = Player(32, 280, 'amuro')
amuro = Player(480, 216, 'amuro')
amuro.getCafeValidMovement()