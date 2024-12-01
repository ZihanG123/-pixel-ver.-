import random
from customer import *

class Cafe:
    def __init__(self):
        self.seats = [(1, 7), (3, 7), (5, 7), (6, 7)] 
        self.occupiedSeats = []
        self.availableSeats = [(1, 7), (3, 7), (5, 7), (6, 7)]
        self.insideCustomers = []
        self.queue = customersAll

    def letCustomerIn(self):
        if self.availableSeats != []:
            currQueueNum = len(self.queue)
            nextCustomer = random.randint(0, currQueueNum)
            


        if len(self.insideCustomers) < len(self.seats) and self.queue != None:
            customer = self.queue.pop()

            if (customer.targetX, customer.targetY) not in self.occupiedSeats:
                self.insideCustomers.append(customer)
                self.occupiedSeats.add(customer.seat)
            else:
                self.queue.append(customer)

poirotCafe = Cafe()