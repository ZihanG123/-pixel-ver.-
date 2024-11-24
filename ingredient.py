from cmu_graphics import *
from PIL import Image


class Ingredient:

    # name should be a string
    def __init__(self,name):

        self.name = name
        self.image = f'./images/hold/{name}HoldImage.PNG'
        

    def __repr__(self):
        return f'{self.name}'
    
    def __hash__(self):
        return hash(str(self))

    def __eq__(self,other):
        return (isinstance(other, Ingredient) and self.name == other.name)
    

########
# initialize ingredients
########

ketchup = Ingredient('ketchup')
curry = Ingredient('curry')
bread = Ingredient('bread')
mayonnaise = Ingredient('mayonnaise')
ham = Ingredient('ham')
lettuce = Ingredient('lettuce')
plate = Ingredient('plate')
rice = Ingredient('rice')
chicken = Ingredient('chicken')
tonkatsu = Ingredient('tonkatsu')
tempura = Ingredient('tempura')
spaghetti = Ingredient('spaghetti')