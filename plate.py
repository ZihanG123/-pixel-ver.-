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

    def __repr__(self):
        return f', '.join(str(ingredient) for ingredient in self.currentIngredients)
    
    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        self.currentIngredients = sorted(self.currentIngredients)
        other.currentIngredients = sorted(other.currentIngredients)
        if len(self.currentIngredients) != other.currentIngredients:
            return False
        else:
            for i in range(len(self.currentIngredients)):
                if self.currentIngredients[i] != other.currentIngredients[i]:
                    return False
                
        return True