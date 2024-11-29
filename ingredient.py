from cmu_graphics import *
from PIL import Image

from kitchen import *


class Ingredient:

    # name should be a string
    def __init__(self, name, cooked, cookTime, utensil):

        self.name = name
        self.image = f'./images/hold/{name}HoldImage.PNG'
        self.cooked = cooked
        self.cookTime = cookTime
        self.cookingUtensil = utensil
        self.isCooking = False
        self.inUtensil = False
        self.cookedOnce = False
        

    def __repr__(self):
        return f'{self.name}'
    
    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        return (isinstance(other, Ingredient) and 
                self.name == other.name and 
                self.cooked == other.cooked)
    

########
# initialize ingredients
########

ketchup = Ingredient('ketchup', True, None, None)
curry = Ingredient('curry', True, None, None)
bread = Ingredient('bread', False, 3, chopping)
mayonnaise = Ingredient('mayonnaise', True, None, None)
ham = Ingredient('ham', False, 3, chopping)
lettuce = Ingredient('lettuce', False, 3, chopping)
plate = Ingredient('plate', True, None, None)
rice = Ingredient('rice', False, 7, pan)
chicken = Ingredient('chicken', False, 3, fryer)
tonkatsu = Ingredient('tonkatsu', False, 5, fryer)
tempura = Ingredient('tempura', False, 5, fryer)
spaghetti = Ingredient('spaghetti', False, 7, pan)