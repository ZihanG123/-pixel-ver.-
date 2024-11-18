from cmu_graphics import *
from PIL import Image
from plate import *
from dish import *

# class for the character the player is controlling
class Player():

    # initialize player
    def __init__(self, playerPosX, playerPosY, name):
        self.playerDirX, self.playerDirY = 0, 0
        self.playerPosX = playerPosX
        self.playerPosY = playerPosY
        self.name = name
        self.validSpaceImage = './images/cafeValidMovementImage.PNG'
        self.validBoard = [ [1]*640 for row in range(640) ]
        self.selection = (0,0)
        self.currentPlate = Plate()

    
    # move the player
    def move(self,key):
        if key not in ['up','down','left','right']:
            pass
        if key == 'up':
            self.playerDirY = -1
            self.playerDirX = 0
        elif key == 'down':
            self.playerDirY = 1
            self.playerDirX = 0
        elif key == 'left':
            self.playerDirX = -1
            self.playerDirY = 0
        elif key == 'right':
            self.playerDirX = 1
            self.playerDirY = 0

        newPosX = self.playerPosX + self.playerDirX * 8
        newPosY = self.playerPosY + self.playerDirY * 8
        if 0 <= newPosX < len(self.validBoard) and 0 <= newPosY < len(self.validBoard[0]):
            if self.validBoard[newPosX][newPosY] == 1:
                self.playerPosX = newPosX
                self.playerPosY = newPosY

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
        if (216 <= self.playerPosX <= 256 and 224 <= self.playerPosY <= 240 and
             self.playerDirX == 0 and self.playerDirY == 1):
            if self.selection == (0,0):
                self.selection = (3,4)
            else:
                self.selection = (0,0)

        elif (264 <= self.playerPosX <= 320 and 224 <= self.playerPosY <= 240 and
             self.playerDirX == 0 and self.playerDirY == 1):
            if self.selection == (0,0):
                self.selection = (4,4)
            else:
                self.selection = (0,0)
            
        elif (328 <= self.playerPosX <= 384 and 224 <= self.playerPosY <= 240 and
             self.playerDirX == 0 and self.playerDirY == 1):
            if self.selection == (0,0):
                self.selection = (5,4)
            else:
                self.selection = (0,0)
            
        elif (392 <= self.playerPosX <= 448 and 224 <= self.playerPosY <= 240 and
             self.playerDirX == 0 and self.playerDirY == 1):
            if self.selection == (0,0):
                self.selection = (6,4)
            else:
                self.selection = (0,0)

        elif (216 <= self.playerPosX <= 232 and 192 <= self.playerPosY <= 240 and
             self.playerDirX == -1 and self.playerDirY == 0):
            if self.selection == (0,0):
                self.selection = (2,3)
            else:
                self.selection = (0,0)

        elif ((464 <= self.playerPosX <= 512 and 184 <= self.playerPosY <= 224 and
             self.playerDirX == 0 and self.playerDirY == -1) or 
             (528 <= self.playerPosX <= 536 and 120 <= self.playerPosY <= 176 and
             self.playerDirX == -1 and self.playerDirY == 0)):
            if self.selection == (0,0):
                self.selection = (7,2)
            else:
                self.selection = (0,0)

    # select the ingredient 
    def doSelectionFood(self):
        if (216 <= self.playerPosX <= 224 and 184 <= self.playerPosY <= 216 and
             self.playerDirX == 0 and self.playerDirY == -1):
            if self.selection == (0,0):
                self.selection = (3,2)
            else:
                self.selection = (0,0)

        elif (232 <= self.playerPosX <= 256 and 184 <= self.playerPosY <= 216):
            if self.selection == (0,0):
                self.selection = (3.5,2)
            else:
                self.selection = (0,0)

        elif (264 <= self.playerPosX <= 288 and 184 <= self.playerPosY <= 216):
            if self.selection == (0,0):
                self.selection = (4,2)
            else:
                self.selection = (0,0)
        
        elif (296 <= self.playerPosX <= 320 and 184 <= self.playerPosY <= 216):
            if self.selection == (0,0):
                self.selection = (4.5,2)
            else:
                self.selection = (0,0)

        elif (328 <= self.playerPosX <= 352 and 184 <= self.playerPosY <= 216):
            if self.selection == (0,0):
                self.selection = (5,2)
            else:
                self.selection = (0,0)

        elif (360 <= self.playerPosX <= 384 and 184 <= self.playerPosY <= 216):
            if self.selection == (0,0):
                self.selection = (5.5,2)
            else:
                self.selection = (0,0)

    # pick up ingredient and add to current plate  
    def pickUpIngredient(self):
        if self.selection == (0,0):
            pass
        elif self.selection == (3,2):
            self.currentPlate.addIngredients('plate')
        elif self.selection == (3.5,2):
            self.currentPlate.addIngredients('sauce')
        elif self.selection == (4,2):
            self.currentPlate.addIngredients('bread')
        elif self.selection == (4.5,2):
            self.currentPlate.addIngredients('mayonnaise')
        elif self.selection == (5,2):
            self.currentPlate.addIngredients('ham')
        elif self.selection == (5.5,2):
            self.currentPlate.addIngredients('lettuce')

    # throw away the current plate
    def throwAwayPlate(self):
        if self.selection == (7,2):
            self.currentPlate.throwAway()