from cmu_graphics import *
from PIL import Image

class Ingredient:

    # name should be a string
    def __init__(self, name, cooked, cookTime, utensil):

        self.name = name

        self.image = CMUImage(Image.open(f'./images/hold/{name}HoldImage.PNG'))
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
    
    def resetIngredient(self):
        self.image = CMUImage(Image.open(f'./images/hold/{self.name}HoldImage.PNG'))
        if self.name in ['ketchup', 'curry', 'mayonnaise', 'plate']:
            self.cooked = True
        else:
            self.cooked = False
        self.isCooking = False
        self.inUtensil = False
        self.cookedOnce = False

########
# initialize ingredients
########

ketchup = Ingredient('ketchup', True, None, None)
curry = Ingredient('curry', True, None, None)
bread = Ingredient('bread', False, 2, 'chopping')
mayonnaise = Ingredient('mayonnaise', True, None, None)
ham = Ingredient('ham', False, 2, 'chopping')
lettuce = Ingredient('lettuce', False, 2, 'chopping')
plate = Ingredient('plate', True, None, None)
rice = Ingredient('rice', False, 6, 'pan')
chicken = Ingredient('chicken', False, 4, 'fryer')
tonkatsu = Ingredient('tonkatsu', False, 4, 'fryer')
tempura = Ingredient('tempura', False, 4, 'fryer')
spaghetti = Ingredient('spaghetti', False, 6, 'pan')

ingredientAll = [ketchup, curry, bread, mayonnaise, ham, lettuce, plate, rice, chicken, tonkatsu, tempura, spaghetti]

###################