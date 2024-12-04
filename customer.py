from random import *
from cmu_graphics import *
from PIL import Image

from plate import *

class Customer:

    # name should be string
    def __init__(self, name, validBoard, eatingTime):
        self.name = name
        self.image = CMUImage(Image.open(f'./images/customers/{self.name}Image.PNG'))
        self.customerPosX = 0
        self.customerPosY = 4

        self.speed = 6
        self.validBoard = validBoard

        self.seat = None

        self.targetX = None
        self.targetY = None

        self.visited = set()
        
        # walking in
        self.path = []
        self.pixelPath = [(-self.speed*v, 256) for v in range(80//self.speed+1,0,-1)]

        # leaving
        self.pathLeave = []
        self.pixelPathLeave = []

        self.isSeated = False

        self.ordered = False
        self.orderNumber = 0
        self.orderDishes = []

        self.eatingTime = eatingTime
        self.eaten = 0

        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        self.nextCustomerDelay = randint(20, 28)*30
        # self.nextCustomerDelay = 40

        # currentStep for walking in
        self.currentStep = 0

        # currentStep for leaving
        self.currentStepLeaving = 0

        self.timeStepRecorded = False

        self.currDishOnDesk = Plate()

        self.eatingTimeStamps = None

        self.hasLeft = False

        self.hasGeneratedPath = False

    def __repr__(self):
        return f'{self.name}'
    
    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        return (isinstance(other, Customer) and 
                self.name == other.name)

        
    def isValidMove(self, x, y):
            return (0 <= x < len(self.validBoard) and 0 <= y < len(self.validBoard[0]) 
                    and self.validBoard[y][x] == 1 
                    and (x, y) not in self.visited)


    def moveCustomer(self):

        if self.move(self.customerPosX, self.customerPosY, self.directions):
            return self.path
        else:
            return None

    # find path from the door (0,4) to the customer's seat (backtracking)    
    def move(self, x, y, directions):
        if (x, y) == (self.targetX, self.targetY):
            self.path.append((x, y))
            return True
        
        self.visited.add((x, y))
        self.path.append((x, y))

        # shuffle(directions)

        for dx, dy in directions:
            newX, newY = x + dx, y + dy
            if self.isValidMove(newX, newY):
                if self.move(newX, newY, directions):
                    return True
                
        self.visited.remove((x, y))
        self.path.pop()
        return False
    
    # make the path to pixel path so the customer can move more smoothly
    def boardPathToPixelPath(self):
        if not self.hasGeneratedPath:
            for i in range(len(self.path) - 1):
                start = self.path[i]
                end = self.path[i + 1]
                dx = (end[0] - start[0])*64
                dy = (end[1] - start[1])*64
                totalDistance = max(abs(dx), abs(dy))
                steps = totalDistance // self.speed 

                for step in range(steps):
                    px = start[0]*64 + (dx//steps) * step
                    py = start[1]*64 + (dy//steps) * step
                    self.pixelPath.append((px, py))

            self.pixelPath.append((self.path[-1][0]*64, self.path[-1][1]*64))

            if self.pixelPath[-1] == (self.targetX*64, self.targetY*64):
                self.seat = (self.targetX, self.targetY+1)


            self.pathLeave = list(reversed(self.path))
            self.pixelPathLeave = list(reversed(self.pixelPath))
            
            self.hasGeneratedPath = True

    
    # customer order
    def startToOrder(self, cafeMenu):
        if self.isSeated == True and self.ordered == False:
            self.orderNumber = randint(1,2)
            # self.orderNumber = 1
            self.ordered = True
            for i in range(self.orderNumber):
                menuLen = len(cafeMenu.menu)
                self.orderDishes.append(cafeMenu.menu[randint(0,menuLen-1)])
        
        if self.orderNumber != 0:
            print(self.orderNumber)
            print(self.orderDishes)

    def leaveCafe(self):
        for i in range(len(self.path)):
            self.pathLeave.append(self.path[len(self.path)-1-i])
        # self.pathLeave = list(reversed(self.path))
        # self.pixelPathLeave = list(reversed(self.pixelPath))
        for i in range(len(self.pixelPath)):
            self.pixelPathLeave.append(self.pixelPath[len(self.pixelPath)-1-i])
        
    def resetCustomer(self):
        self.customerPosX = 0
        self.customerPosY = 4

        self.targetX = None
        self.targetY = None

        self.seat = None

        self.visited = set()
        self.path = []
        self.pixelPath = [(-self.speed*v, 256) for v in range(80//self.speed+1,0,-1)]
        self.pathLeave = []
        self.pixelPathLeave = []

        self.isSeated = False

        self.ordered = False
        self.orderNumber = 0
        self.orderDishes = []

        self.eaten = 0

        self.nextCustomerDelay = randint(20, 28)*30
        self.currentStep = 0
        self.currentStepLeaving = 0

        self.timeStepRecorded = False

        self.currDishOnDesk = Plate()

        self.eatingTimeStamps = None

        self.hasLeft = False

        self.hasGeneratedPath = False


########################################
# Cafe class
########################################

class Cafe:
    def __init__(self):
        self.seats = [(1, 7), (3, 7), (5, 7), (6, 7)] 
        self.occupiedSeats = []
        self.availableSeats = [(1, 7), (3, 7), (5, 7), (6, 7)]
        self.nextCustomers = []
        self.insideCustomers = []
        self.queue = customersAll

        self.cafeTime = 0
        self.timeSeconds = 0

        self.customerTimeStamps = []
        self.currWalkingInCustomer = None
        self.prevWalkingInCustomer = None

        self.currLeavingCustomer = None


    # next customers
    def letCustomerIn(self):
        if self.availableSeats != []:
            currQueueNum = len(self.queue)
            print(self.queue)
            if self.prevWalkingInCustomer != None and self.currWalkingInCustomer != None:
                if self.prevWalkingInCustomer.isSeated and self.currWalkingInCustomer.isSeated:
                    nextCustomer = self.queue[randint(0, currQueueNum-1)]
                    print('next customer will be: ', nextCustomer)
                    print(nextCustomer.nextCustomerDelay)
                    
                    nextCustomer.seat = self.availableSeats[randint(0, len(self.availableSeats)-1)]
                    nextCustomer.targetX, nextCustomer.targetY = nextCustomer.seat[0], nextCustomer.seat[1]-1

                    nextCustomer.moveCustomer()
                    nextCustomer.path.append((nextCustomer.targetX, nextCustomer.targetY+1))
                    nextCustomer.boardPathToPixelPath()
                    # print('/////////////////////////////////', nextCustomer.path)
                    # print('?????????????????????????????????', nextCustomer.pixelPath)
                    # print('.................................', nextCustomer.pixelPathLeave)
                    # nextCustomer.leaveCafe()
                    
                    self.nextCustomers.append(nextCustomer)
                    self.occupiedSeats.append(nextCustomer.seat)
                    # print('occupied seats:', self.occupiedSeats)
                    self.queue.remove(nextCustomer)
                    self.availableSeats.remove(nextCustomer.seat)
                    print('nextCustomers List:', self.nextCustomers)
            else:
                nextCustomer = self.queue[randint(0, currQueueNum-1)]
                print('next customer will be: ', nextCustomer)
                print(nextCustomer.nextCustomerDelay)
                
                nextCustomer.seat = self.availableSeats[randint(0, len(self.availableSeats)-1)]
                nextCustomer.targetX, nextCustomer.targetY = nextCustomer.seat[0], nextCustomer.seat[1]-1

                nextCustomer.moveCustomer()
                nextCustomer.path.append((nextCustomer.targetX, nextCustomer.targetY+1))
                nextCustomer.boardPathToPixelPath()
                # print('/////////////////////////////////', nextCustomer.path)
                # print('?????????????????????????????????', nextCustomer.pixelPath)
                # print('.................................', nextCustomer.pixelPathLeave)
                # nextCustomer.leaveCafe()
                
                self.nextCustomers.append(nextCustomer)
                self.occupiedSeats.append(nextCustomer.seat)
                # print('occupied seats:', self.occupiedSeats)
                self.queue.remove(nextCustomer)
                self.availableSeats.remove(nextCustomer.seat)
                print('nextCustomers List:', self.nextCustomers)
        

    def recordTimeStep(self, customer):
        if customer.isSeated and customer.timeStepRecorded == False:
            self.customerTimeStamps.append(self.cafeTime)
            customer.timeStepRecorded = True

    def letCustomerLeave(self, potentialCustomer):
        if self.currLeavingCustomer == None:
            if potentialCustomer.eaten == potentialCustomer.orderNumber:
                self.currLeavingCustomer = potentialCustomer
            
            # print(customer.seat)
            # print(customer.path)
            # print(customer.pathLeave)
            # print(customer.pixelPathLeave)
            # print(f'currLeavingCustomer: {customer.name}')
            # print(self.insideCustomers)


    def walkInOneByOne(self):
        if self.currWalkingInCustomer == None:
            if len(self.nextCustomers) > 0:
                self.nextCustomers.pop()
                if len(self.nextCustomers) > 0:
                    self.currWalkingInCustomer = self.nextCustomers[-1]
        else:
            print('self.prevWalkingInCustomer is', self.prevWalkingInCustomer)
            print('self.prevWalkingInCustomer is', self.prevWalkingInCustomer)
            if self.prevWalkingInCustomer.isSeated and self.currWalkingInCustomer.isSeated:
                if len(self.nextCustomers) > 0:
                    self.nextCustomers.pop()
                    if len(self.nextCustomers) > 0:
                        self.currWalkingInCustomer = self.nextCustomers[-1]



########################################
# Seat class
########################################

class Seat:
    def __init__(self):
        pass


##########
# initialize customers
##########


validBoard = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 1]
]


akai = Customer('akai', validBoard, 6)
ai = Customer('ai', validBoard, 10)
conan = Customer('conan', validBoard, 9)
heiji = Customer('heiji', validBoard, 7)
jin = Customer('jin', validBoard, 8)
kazuha = Customer('kazuha', validBoard, 8)
kid = Customer('kid', validBoard, 7)
matsuda = Customer('matsuda', validBoard, 6)
ran = Customer('ran', validBoard, 8)
sera = Customer('sera', validBoard, 7)
suzuki = Customer('suzuki', validBoard, 8)

customersAll = [akai, ai, conan, heiji, jin, kazuha, kid, matsuda, ran, sera, suzuki]

poirotCafe = Cafe()

# availableSeating = poirotCafe.availableSeats
# availableSeatingNum = len(availableSeating)


# currentCustomer = customersAll[random.randint(0, 9)]

# currentCustomer.moveCustomer()
# currentCustomer.path.append((currentCustomer.targetX, currentCustomer.targetY+1))
# currentCustomer.boardPathToPixelPath()

# # print(currentCustomer.pixelPath)
# print(currentCustomer.seat)
# print((currentCustomer.targetX, currentCustomer.targetY+1))