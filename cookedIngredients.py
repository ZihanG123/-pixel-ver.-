from ingredient import *

class CookedIngredient(Ingredient):
    def __init__(self, name, cookTime):
        super().__init__(name)
        self.cookTime = cookTime
    

#########
# initialize cooked dishes
#########
