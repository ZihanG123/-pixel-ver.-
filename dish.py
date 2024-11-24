from cmu_graphics import *
from PIL import Image
from ingredient import *

# class for all the dishes in the menu
class Dish:

    # name should be string
    # ingredientsNeeded should be a list of strings
    def __init__(self,name,ingredientsNeeded):
        
        # name for dish
        self.name = name

        # ingredientsNeeded is a list of all the ingredients needed to cook the dish
        # ingredients should be of the class Ingredient
        self.ingredientsNeeded = ingredientsNeeded

    # check if the plate (food cooked by player) is the same dish as the customer ordered
    # check if every ingredient in plate is the same as every ingredient in dish
    # other is Plate
    def __eq__(self,other):
        self.ingredientsNeeded = sorted(self.ingredientsNeeded)
        other.currentIngredients = sorted(other.currentIngredients)
        if len(self.ingredientsNeeded) != other.currentIngredients:
            return False
        else:
            for i in range(len(self.ingredientsNeeded)):
                if self.ingredientsNeeded[i] != other.currentIngredients[i]:
                    return False
                
        return True
    
    # print name + ingredients
    def __repr__(self):
        return f'{self.name}: ' + ', '.join(self.ingredientsNeeded)
    
#######
# initialize dishes
#######

sandwich = Dish('sandwich',[plate, bread, lettuce, mayonnaise, ham])