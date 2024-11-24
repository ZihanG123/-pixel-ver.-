from collections import deque
from customer import *

class Cafe:
    def __init__(self, seats):
        self.seats = seats 
        self.occupiedSeats = set()
        self.insideCustomers = []
        self.queue = []

    def addCustomerToQueue(self, customer):
        self.queue.append(customer)

    def letCustomerIn(self):
        if len(self.insideCustomers) < len(self.seats) and self.queue != None:
            customer = self.queue.pop()

            if (customer.targetX, customer.targetY) not in self.occupiedSeats:
                self.insideCustomers.append(customer)
                self.occupiedSeats.add(customer.seat)
            else:
                self.queue.append(customer)