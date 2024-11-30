from ingredient import *

class Kitchen:
    def __init__(self, name, selection):
        self.name = name
        self.isCooking = False
        self.selectionCoor = selection
        self.cookingCounter = 0
        self.cookingCounterSeconds = 0
        self.ingredientInside = None

    def __repr__(self):
        return f'{self.name}'
    
    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        return (isinstance(other, Kitchen) and self.name == other.name)
    
    def cookFood(self):
        if self.ingredientInside != None:
            currCookingIng = self.ingredientInside
            if self.cookingCounter <= currCookingIng.cookTime*30:
                self.cookingCounter += 1
                if self.cookingCounter % 30 == 0:
                    self.cookingCounterSeconds += 1
            else:
                currCookingIng.cooked = True
                currCookingIng.isCooking = False
                self.cookingCounter = 0
                self.cookingCounterSeconds = 0
                self.isCooking = False
                currCookingIng.cookedOnce = True
                # currCookingIng.image = f'./images/cooked/{currCookingIng.name}CookedImage.PNG'



#########
chopping = Kitchen('chopping', (4,4,0))
pan = Kitchen('pan', (5,4,0))
fryer = Kitchen('fryer', (6,4,0))