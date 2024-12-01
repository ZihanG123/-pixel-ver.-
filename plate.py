# class for the plate that the player currently have
from ingredient import *

class Plate:
    def __init__(self):
        self.currentIngredients = []
        self.posX, self.posY = 3, 4

    # ingredient is a string
    def addIngredients(self, ingredient):
        if ingredient.cooked:
            self.currentIngredients.append(ingredient)
            ingredient.isCooking = False
            ingredient.inUtensil = False
            ingredient.cookedOnce = False
            if ingredient.name in ['ketchup', 'curry', 'mayonnaise', 'plate']:
                ingredient.cooked =  True
            else:
                ingredient.cooked =  False

    # throw away current plate to trash can
    def throwAway(self):
        self.currentIngredients = []

    def __repr__(self):
        return f', '.join(str(ingredient) for ingredient in self.currentIngredients)
    
    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        # self.currentIngredients = sorted(self.currentIngredients)
        # other.currentIngredients = sorted(other.currentIngredients)
        if isinstance(other, Plate):
            if self.currentIngredients == [] and other.currentIngredients == []:
                return True
            else:
                if len(self.currentIngredients) != len(other.currentIngredients):
                    return False
                for i in range(len(self.currentIngredients)):
                    if self.currentIngredients[i] != other.currentIngredients[i]:
                        return False
            return True
        else:
            if len(self.currentIngredients) != len(other.ingredientsNeeded):
                return False
            else:
                for i in range(len(self.currentIngredients)):
                    if self.currentIngredients[i] != other.ingredientsNeeded[i]:
                        return False

                    # if not self.currentIngredients[i].cooked:
                    #     print(self.currentIngredients[i], self.currentIngredients[i].cooked)
                    #     print('33333333')
                    #     return False
            return True