    # def doSelectionDesk(self):
    #     if (216 <= self.playerPosX <= 256 and 224 <= self.playerPosY <= 240 and
    #          self.playerDirX == 0 and self.playerDirY == 1):
    #         if self.selection == (0,0):
    #             self.selection = (3,4)
    #         else:
    #             self.selection = (0,0)

    #     elif (264 <= self.playerPosX <= 320 and 224 <= self.playerPosY <= 240 and
    #          self.playerDirX == 0 and self.playerDirY == 1):
    #         if self.selection == (0,0):
    #             self.selection = (4,4)
    #         else:
    #             self.selection = (0,0)
            
    #     elif (328 <= self.playerPosX <= 384 and 224 <= self.playerPosY <= 240 and
    #          self.playerDirX == 0 and self.playerDirY == 1):
    #         if self.selection == (0,0):
    #             self.selection = (5,4)
    #         else:
    #             self.selection = (0,0)
            
    #     elif (392 <= self.playerPosX <= 448 and 224 <= self.playerPosY <= 240 and
    #          self.playerDirX == 0 and self.playerDirY == 1):
    #         if self.selection == (0,0):
    #             self.selection = (6,4)
    #         else:
    #             self.selection = (0,0)

    #     elif (216 <= self.playerPosX <= 232 and 192 <= self.playerPosY <= 240 and
    #          self.playerDirX == -1 and self.playerDirY == 0):
    #         if self.selection == (0,0):
    #             self.selection = (2,3)
    #         else:
    #             self.selection = (0,0)

    #     elif ((464 <= self.playerPosX <= 512 and 184 <= self.playerPosY <= 224 and
    #          self.playerDirX == 0 and self.playerDirY == -1) or 
    #          (528 <= self.playerPosX <= 536 and 120 <= self.playerPosY <= 176 and
    #          self.playerDirX == -1 and self.playerDirY == 0)):
    #         if self.selection == (0,0):
    #             self.selection = (7,2)
    #         else:
    #             self.selection = (0,0)

        # if (216 <= self.playerPosX <= 224 and 184 <= self.playerPosY <= 216 and
        #      self.playerDirX == 0 and self.playerDirY == -1):
        #     if self.selection == (0,0):
        #         self.selection = (3,2)
        #     else:
        #         self.selection = (0,0)

        # elif (232 <= self.playerPosX <= 256 and 184 <= self.playerPosY <= 216):
        #     if self.selection == (0,0):
        #         self.selection = (3.5,2)
        #     else:
        #         self.selection = (0,0)

        # elif (264 <= self.playerPosX <= 288 and 184 <= self.playerPosY <= 216):
        #     if self.selection == (0,0):
        #         self.selection = (4,2)
        #     else:
        #         self.selection = (0,0)
        
        # elif (296 <= self.playerPosX <= 320 and 184 <= self.playerPosY <= 216):
        #     if self.selection == (0,0):
        #         self.selection = (4.5,2)
        #     else:
        #         self.selection = (0,0)

        # elif (328 <= self.playerPosX <= 352 and 184 <= self.playerPosY <= 216):
        #     if self.selection == (0,0):
        #         self.selection = (5,2)
        #     else:
        #         self.selection = (0,0)

        # elif (360 <= self.playerPosX <= 384 and 184 <= self.playerPosY <= 216):
        #     if self.selection == (0,0):
        #         self.selection = (5.5,2)
        #     else:
        #         self.selection = (0,0)

        # elif (392 <= self.playerPosX <= 416 and 184 <= self.playerPosY <= 216):
        #     if self.selection == (0,0):
        #         self.selection = (6,2)
        #     else:
        #         self.selection = (0,0)

    # drawImage('./images/chairImage.PNG', 96, 480, width=64, height=64, align='center')
    # drawImage('./images/chairImage.PNG', 224, 480, width=64, height=64, align='center')
    # drawImage('./images/chairImage.PNG', 352, 480, width=64, height=64, align='center')
    # drawImage('./images/chairImage.PNG', 416, 480, width=64, height=64, align='center')

    # drawImage('./images/desk1Image.PNG', 96, 544, width=64, height=64, align='center')
    # drawImage('./images/desk1Image.PNG', 224, 544, width=64, height=64, align='center')
    # drawImage('./images/desk1Image.PNG', 352, 544, width=64, height=64, align='center')
    # drawImage('./images/desk1Image.PNG', 416, 544, width=64, height=64, align='center')

        # def move(x, y, visited):
        #     if (x, y) == (self.target[0], self.target[1]):
        #         print("Target reached:", x, y)
        #         return visited
            
        #     if not (0 <= x < 640 and 0 <= y < 640) or validBoard[x][y] == 0 or (x, y) in visited:
        #         return False
            
        #     print("Visiting:", x, y)

        #     for dx, dy in availableDir:
        #         newX, newY = x + dx*self.speed, y + dy*self.speed

        #         if ((newX, newY) not in visited 
        #             and 0 <= newX < len(validBoard) 
        #             and 0 <= newY < len(validBoard[0])):
        #             if validBoard[newX][newY] == 1:
        #                 visited.add((newX, newY))
        #                 print("Valid:", newX, newY)
        #                 solution = move(newX, newY, visited)
        #                 if solution != None:
        #                     self.customerPosX = newX
        #                     self.customerPosY = newY
        #                     print(f"Moved customer to: {newX}, {newY}")
        #                     return solution
        #                 visited.remove((newX, newY))

        #     return None
        
        
        # if move(self.customerPosX, self.customerPosY, self.visited):
        #     print("Final position:", self.customerPosX, self.customerPosY)
        # else:
        #     print("No path found.")
        # print("Visited set:", self.visited)
        
        # # move(self.customerPosX, self.customerPosY, self.visited)
        # # print(self.visited)

# validBoard = [[1]*640 for row in range(640)]

# def getCustomerValidMovement():
#         validSpaceImg = Image.open('./images/customerValidMovementImage.PNG')
#         # print(validSpaceImg.width, validSpaceImg.height)
#         validSpaceImg = validSpaceImg.resize((640,640))
#         # print(validSpaceImg.width, validSpaceImg.height)
#         for x in range(validSpaceImg.width):
#             for y in range(validSpaceImg.height):
#                 pixel = validSpaceImg.getpixel((x, y))
#                 if pixel == (0,0,0,0):
#                     validBoard[x][y] = 0

# getCustomerValidMovement()

# def updateCustomerPosition():
#     if not akai.isSeated():
#         akai.moveCustomer(validBoard, availableDir)
#         print("Customer moved.")
    # for customer in customers:
    #     if not customer.isSeated():
    #         customer.moveCustomer()



###############################
# from PIL import *
# import random

# from menu import *

# class Customer:

#     # name should be string
#     def __init__(self, name, validBoard, target):
#         self.name = name
#         self.image = f'./images/customers/{self.name}Image.PNG'
#         self.customerPosX = 0
#         self.customerPosY = 4

#         self.speed = 8
#         self.validBoard = validBoard

#         self.targetX = target[0]
#         self.targetY = target[1]

#         self.visited = set()
#         self.path = []
#         self.pixelPath = [(-self.speed*v, 256) for v in range(10,0,-1)]
        
#         self.isSeated = False
#         self.seat = None

#         self.orderNumber = 0
#         self.orderDishes = []
        
#     def isValidMove(self, x, y):
#             return (0 <= x < len(self.validBoard) and 0 <= y < len(self.validBoard[0]) 
#                     and self.validBoard[y][x] == 1 
#                     and (x, y) not in self.visited)


#     def moveCustomer(self):
#         directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

#         if self.move(self.customerPosX, self.customerPosY, directions):
#             return self.path
#         else:
#             return None

        
#     def move(self, x, y, directions):
#         if (x, y) == (self.targetX, self.targetY):
#             self.path.append((x, y))
#             return True
        
#         self.visited.add((x, y))
#         self.path.append((x, y))

#         random.shuffle(directions)

#         for dx, dy in directions:
#             newX, newY = x + dx, y + dy
#             if self.isValidMove(newX, newY):
#                 if self.move(newX, newY, directions):
#                     return True
                
#         self.visited.remove((x, y))
#         self.path.pop()
#         return False

#     # def isSeated(self):
#     #     return (self.path[-1][0], self.path[-1][1]) == (self.targetX*64, self.targetY*64)
    
#     def boardPathToPixelPath(self):

#         for i in range(len(self.path) - 1):
#             start = self.path[i]
#             end = self.path[i + 1]

#             dx = (end[0] - start[0]) * 64
#             dy = (end[1] - start[1]) * 64

#             totalDistance = max(abs(dx), abs(dy))
#             steps = totalDistance // self.speed 
#             for step in range(steps):
#                 px = start[0] * 64 + (dx // steps) * step
#                 py = start[1] * 64 + (dy // steps) * step
#                 self.pixelPath.append((px, py))

#         self.pixelPath.append((self.path[-1][0] * 64, self.path[-1][1] * 64))

#         if (self.pixelPath[-1][0], self.pixelPath[-1][1]) == (self.targetX*64, self.targetY*64):
#             self.seat = (self.targetX, self.targetY)

#     # def startToOrder(self, cafeMenu):
#     #     if self.isSeated == True:
#     #         self.orderNumber = random.randint(1,3)
#     #         for i in range(self.orderNumber):
#     #             self.orderDishes.append(cafeMenu[random.randint(0,9)])
#     #     return self.orderNumber, self.orderDishes

    


# ##########
# # initialize customers
# ##########

# availableSeating = [(1, 7), (3, 7), (5, 7), (6, 7)]

# validBoard = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
#     [1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
#     [1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 1, 0, 1, 0, 0, 1, 1, 1],
#     [0, 0, 0, 0, 1, 0, 0, 0, 1, 1]
# ]

# akai = Customer('akai', validBoard, availableSeating[random.randint(0, 3)])
# ai = Customer('ai', validBoard, availableSeating[random.randint(0, 3)])
# conan = Customer('conan', validBoard, availableSeating[random.randint(0, 3)])
# heiji = Customer('heiji', validBoard, availableSeating[random.randint(0, 3)])
# jin = Customer('jin', validBoard, availableSeating[random.randint(0, 3)])
# kazuha = Customer('kazuha', validBoard, availableSeating[random.randint(0, 3)])
# kid = Customer('kid', validBoard, availableSeating[random.randint(0, 3)])
# matsuda = Customer('matsuda', validBoard, availableSeating[random.randint(0, 3)])
# ran = Customer('ran', validBoard, availableSeating[random.randint(0, 3)])
# sera = Customer('sera', validBoard, availableSeating[random.randint(0, 3)])
# suzuki = Customer('suzuki', validBoard, availableSeating[random.randint(0, 3)])


# customers = [akai, ai, conan, heiji, jin, kazuha, kid, matsuda, ran, sera, suzuki]

# currentCustomer = customers[random.randint(0, 9)]

# currentCustomer.moveCustomer()
# currentCustomer.boardPathToPixelPath()
# # print(akai.path)
# # print(currentCustomer.pixelPath)

# # print(currentCustomer.isSeated)
# print(currentCustomer.seat)


    # if (amuro.currentHoldIngredient != None and 
    #     not amuro.currentHoldIngredient.cooked and 
    #     amuro.currentHoldIngredient.cookingUtensil != None):
    #     if amuro.currentHoldIngredient.cookingUtensil.isCooking:
    #         if app.cookingOnStepCounter <= amuro.currentHoldIngredient.cookTime*30:
    #             app.cookingOnStepCounter += 1
    #             if app.cookingOnStepCounter % 30 == 0:
    #                 amuro.currentHoldIngredient.cookingUtensil.cookingCounter += 1

    #             #######
    #             # print(app.cookingOnStepCounter)
    #             # print('utensil.cookingCounter', amuro.currentHoldIngredient.cookingUtensil.cookingCounter)


    #         else:
    #             amuro.currentHoldIngredient.cooked = True
    #             amuro.currentHoldIngredient.isCooking = False
    #             app.cookingOnStepCounter = 0
    #             amuro.currentHoldIngredient.cookingUtensil.cookingCounter = 0
    #             amuro.currentHoldIngredient.cookingUtensil.isCooking = False
    #             amuro.currentHoldIngredient.cookedOnce = True

    #             # print('     ',app.cookingOnStepCounter)
    #             # print('      utensil.cookingCounter', amuro.currentHoldIngredient.cookingUtensil.cookingCounter)

#  and 
#         not amuro.currentHoldIngredient.isCooking and 
#         not amuro.currentHoldIngredient.inUtensil


    # posX, posY = currentCustomer.pixelPath[app.currentCustomerStep]
    # drawImage(currentCustomer.image, posX+35, posY+21, width=128, height=128, align='center')

    # for customer in poirotCafe.insideCustomers:
    #     if not customer.isSeated:

    #         if poirotCafe.customerTimeStamps != []:
    #             prevCustomerStamp = poirotCafe.customerTimeStamps[-1]
    #             if poirotCafe.cafeTime >= prevCustomerStamp + customer.nextCustomerDelay:
    #                 posX, posY = customer.pixelPath[customer.currentStep]
    #                 drawImage(customer.image, posX+35, posY+21, width=128, height=128, align='center')
    #         else:
    #             posX, posY = customer.pixelPath[customer.currentStep]
    #             drawImage(customer.image, posX+35, posY+21, width=128, height=128, align='center')

    #     else:
    #         posX, posY = customer.pixelPath[-1]
    #         drawImage(customer.image, posX+35, posY+21, width=128, height=128, align='center')

    # index = 0
    # while index < len(poirotCafe.insideCustomers):
    #     customer = poirotCafe.insideCustomers[index]
    #     if poirotCafe.customerTimeStamps == []:
    #         posX, posY = customer.pixelPath[customer.currentStep]
    #         drawImage(customer.image, posX+35, posY+21, width=128, height=128, align='center')
    #     else:
    #         prevCustomerStamp = poirotCafe.customerTimeStamps[index-1]
    #         if poirotCafe.cafeTime >= prevCustomerStamp + customer.nextCustomerDelay:
    #             posX, posY = customer.pixelPath[customer.currentStep]
    #             drawImage(customer.image, posX+35, posY+21, width=128, height=128, align='center')

    #     if customer.isSeated:
    #         index += 1

    #     self.visited = set()
    #     self.targetX, self.targetY = 0, 4
    #     self.path = [self.seat]
    #     self.pixelPath = []
    #     if self.move(self.seat[0], self.seat[1]-1, self.directions):
    #         self.boardPathToPixelPath()
    #         self.pixelPath.append((-self.speed*v, 256) for v in range(0,80//self.speed+1))
    #         return self.pixelPath
    #     else:
    #         return None

    # if poirotCafe.currLeavingCustomer != None:
    #     customer = poirotCafe.currLeavingCustomer
    #     if customer.isSeated:
    #         posX, posY = customer.pixelPath[-1]
    #         drawImage(customer.image, posX+35, posY+21, width=128, height=128, align='center')

# {'posX':(216,232), 'posY':(192,240), 'dirX':-1, 'dirY':0, 'selection':(2,3)}

# def gameOver_onKeyPress(app, key):
#     if key == 'space':
#         setActiveScreen('start')

    # def drawCookingIngredient(self):
    #     # print(f'{self.name}', self.ingredientInside)
    #     if self.ingredientInside != None:
    #         currCookingIng = self.ingredientInside
    #         drawImage(currCookingIng.image, self.selectionCoor[0]*64, self.selectionCoor[1]*64, width=64, height=64)
    #         if not currCookingIng.cookedOnce:
    #             if currCookingIng.cookTime-self.cookingCounterSeconds > 0:
    #                 drawLabel(str(currCookingIng.cookTime-self.cookingCounterSeconds), 
    #                     self.selectionCoor[0]*64+8, self.selectionCoor[1]*64+8, 
    #                     size=20, align='center', font='monospace', bold=True, fill='white')