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

            if self.cookingCounter < currCookingIng.cookTime*30:
                if not currCookingIng.cookedOnce:
                    self.cookingCounter += 1
                    # print(currCookingIng, self.cookingCounter)
                    if self.cookingCounter % 30 == 0:
                        self.cookingCounterSeconds += 1
                        # print(self.cookingCounterSeconds)
            else:
                self.cookingCounter = 0
                self.cookingCounterSeconds = 0
                currCookingIng.cooked = True
                currCookingIng.isCooking = False
                self.isCooking = False
                currCookingIng.cookedOnce = True
                # currCookingIng.image = f'./images/cooked/{currCookingIng.name}CookedImage.PNG'

    def drawCookingIngredient(self):
        # print(f'{self.name}', self.ingredientInside)
        if self.ingredientInside != None:
            currCookingIng = self.ingredientInside
            drawImage(currCookingIng.image, self.selectionCoor[0]*64, self.selectionCoor[1]*64, width=64, height=64)
            if not currCookingIng.cookedOnce:
                if currCookingIng.cookTime-self.cookingCounterSeconds > 0:
                    drawLabel(str(currCookingIng.cookTime-self.cookingCounterSeconds), 
                        self.selectionCoor[0]*64+8, self.selectionCoor[1]*64+8, 
                        size=20, align='center', font='monospace', bold=True, fill='white')



#########
chopping = Kitchen('chopping', (4,4,0))
pan = Kitchen('pan', (5,4,0))
fryer = Kitchen('fryer', (6,4,0))