from cmu_graphics import *
from PIL import Image

class Player():
    def __init__(self, playerPosX, playerPosY, name):
        self.playerDirX, self.playerDirY = 0, 0
        self.playerPosX = playerPosX
        self.playerPosY = playerPosY
        self.name = name
        self.validSpaceImage = './images/cafeValidMovementImage.PNG'
        self.validBoard = [ [1]*640 for row in range(640) ]
                
    def playerKeyPress(self, key):
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

    
    # move the player
    def move(self):
        newPosX = self.playerPosX + self.playerDirX * 8
        newPosY = self.playerPosY + self.playerDirY * 8
        if 0 <= newPosX < len(self.validBoard) and 0 <= newPosY < len(self.validBoard[0]):
            if self.validBoard[newPosX][newPosY] == 1:
                self.playerPosX = newPosX
                self.playerPosY = newPosY

    
    def getCafeValidMovement(self):
        validSpaceImg = Image.open('./images/cafeValidMovementImage.PNG')
        print(validSpaceImg.width, validSpaceImg.height)
        validSpaceImg = validSpaceImg.resize((640,640))
        print(validSpaceImg.width, validSpaceImg.height)
        for x in range(validSpaceImg.width):
            for y in range(validSpaceImg.height):
                pixel = validSpaceImg.getpixel((x, y))
                if pixel == (0,0,0,0):
                    self.validBoard[x][y] = 0



        
        
