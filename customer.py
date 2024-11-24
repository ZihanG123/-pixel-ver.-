from PIL import *
import random

class Customer:

    # name should be string
    def __init__(self, name, validBoard, target):
        self.name = name
        self.image = f'./images/customers/{self.name}Image.PNG'
        self.customerPosX = 0
        self.customerPosY = 4

        self.speed = 8
        self.validBoard = validBoard

        self.targetX = target[0]
        self.targetY = target[1]

        self.visited = set()
        self.path = []
        self.pixelPath = [(-self.speed*v, 256) for v in range(10,0,-1)]
        
    def isValidMove(self, x, y):
            return (0 <= x < len(self.validBoard) and 0 <= y < len(self.validBoard[0]) 
                    and self.validBoard[y][x] == 1 
                    and (x, y) not in self.visited)


    def moveCustomer(self):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        if self.move(self.customerPosX, self.customerPosY, directions):
            return self.path
        else:
            return None

        
    def move(self, x, y, directions):
        if (x, y) == (self.targetX, self.targetY):
            self.path.append((x, y))
            return True
        
        self.visited.add((x, y))
        self.path.append((x, y))

        random.shuffle(directions)

        for dx, dy in directions:
            newX, newY = x + dx, y + dy
            if self.isValidMove(newX, newY):
                if self.move(newX, newY, directions):
                    return True
                
        self.visited.remove((x, y))
        self.path.pop()
        return False

    def isSeated(self):
        return (self.customerPosX, self.customerPosY) == (self.targetX, self.targetY)
    
    def boardPathToPixelPath(self):

        for i in range(len(self.path) - 1):
            start = self.path[i]
            end = self.path[i + 1]

            dx = (end[0] - start[0]) * 64
            dy = (end[1] - start[1]) * 64

            totalDistance = max(abs(dx), abs(dy))
            steps = totalDistance // self.speed 
            for step in range(steps):
                px = start[0] * 64 + (dx // steps) * step
                py = start[1] * 64 + (dy // steps) * step
                self.pixelPath.append((px, py))

        self.pixelPath.append((self.path[-1][0] * 64, self.path[-1][1] * 64))

    


##########
# initialize customers
##########

availableSeating = [(1, 7), (3, 7), (5, 7), (6, 7)]


validBoard = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 1]
]


akai = Customer('akai', validBoard, availableSeating[random.randint(0, 3)])
ai = Customer('ai', validBoard, availableSeating[random.randint(0, 3)])
conan = Customer('conan', validBoard, availableSeating[random.randint(0, 3)])
heiji = Customer('heiji', validBoard, availableSeating[random.randint(0, 3)])
jin = Customer('jin', validBoard, availableSeating[random.randint(0, 3)])
kazuha = Customer('kazuha', validBoard, availableSeating[random.randint(0, 3)])
kid = Customer('kid', validBoard, availableSeating[random.randint(0, 3)])
matsuda = Customer('matsuda', validBoard, availableSeating[random.randint(0, 3)])
ran = Customer('ran', validBoard, availableSeating[random.randint(0, 3)])
sera = Customer('sera', validBoard, availableSeating[random.randint(0, 3)])
suzuki = Customer('suzuki', validBoard, availableSeating[random.randint(0, 3)])


customers = [akai, ai, conan, heiji, jin, kazuha, kid, matsuda, ran, sera, suzuki]

currentCustomer = customers[random.randint(0, 9)]

currentCustomer.moveCustomer()
currentCustomer.boardPathToPixelPath()
# print(akai.path)
print(currentCustomer.pixelPath)

