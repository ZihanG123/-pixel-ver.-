from cmu_graphics import *
from PIL import Image

# class for the plate that the player currently have
class Plate:
    def __init__(self):
        self.currentIngredients = []

    # ingredient is a string
    def addIngredients(self, ingredient):
        self.currentIngredients.append(ingredient)

    # throw away current plate to trash can
    def throwAway(self):
        self.currentIngredients = []