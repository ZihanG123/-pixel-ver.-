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