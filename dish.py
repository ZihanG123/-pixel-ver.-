from ingredient import *
# class for all the dishes in the menu
class Dish:

    # name should be string
    # ingredientsNeeded should be a list of strings
    def __init__(self, name, ingredientsNeeded):
        
        # name for dish
        self.name = name

        # ingredientsNeeded is a list of all the ingredients needed to cook the dish
        # ingredients should be of the class Ingredient
        self.ingredientsNeeded = ingredientsNeeded

    # check if the plate (food cooked by player) is the same dish as the customer ordered
    # check if every ingredient in plate is the same as every ingredient in dish
    # other is Plate
    def __eq__(self, other):
        # self.ingredientsNeeded = sorted(self.ingredientsNeeded)
        # other.currentIngredients = sorted(other.currentIngredients)
        if len(self.ingredientsNeeded) != other.currentIngredients:
            return False
        else:
            for i in range(len(self.ingredientsNeeded)):
                if self.ingredientsNeeded[i] != len(other.currentIngredients[i]):
                    return False
                
        return True
    
    # print name + ingredients
    def __repr__(self):
        # return f'{self.name}: ' + '+ '.join(str(ingredient) for ingredient in self.ingredientsNeeded)
        return f'{self.name}'
    
    def __hash__(self):
        return hash(str(self))

    
#######
# initialize dishes
#######

sandwich = Dish('sandwich',[plate, bread, mayonnaise, ham, lettuce])

chickenCurryRice = Dish('chicken curry rice', [plate, curry, rice, chicken])
tonkatsuCurryRice = Dish('tonkatsu curry rice', [plate, curry, rice, tonkatsu])
tempuraCurryRice = Dish('tempura curry rice', [plate, curry, rice, tempura])

chickenCurrySpaghetti = Dish('chicken curry spaghetti', [plate, curry, spaghetti, chicken])
tonkatsuCurrySpaghetti = Dish('tonkatsu curry spaghetti', [plate, curry, spaghetti, tonkatsu])
tempuraCurrySpaghetti = Dish('tempura curry spaghetti', [plate, curry, spaghetti, tempura])

chickenTomatoSauceSpaghetti = Dish('chicken tomato sauce spaghetti', [plate, ketchup, spaghetti, chicken])
tonkatsuTomatoSauceSpaghetti = Dish('tonkatsu tomato sauce spaghetti', [plate, ketchup, spaghetti, tonkatsu])
tempuraTomatoSauceSpaghetti = Dish('tempura tomato sauce spaghetti', [plate, ketchup, spaghetti, tempura])