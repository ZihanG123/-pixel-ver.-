from plate import *
from dish import *
from ingredient import *

rice = Ingredient('rice', True, 7, 'pan')
chicken = Ingredient('chicken', True, 5, 'fryer')

testPlate = Plate()
testPlate.addIngredients(plate)
testPlate.addIngredients(curry)
rice.cooked = True
testPlate.addIngredients(rice)
chicken.cooked = True
testPlate.addIngredients(chicken)

testOrder = [chickenCurryRice, sandwich]

print(testPlate.currentIngredients)
print(chickenCurryRice.ingredientsNeeded)

for i in range(len(testPlate.currentIngredients)):
    print(testPlate.currentIngredients[i] == chickenCurryRice.ingredientsNeeded[i])

print(testPlate == chickenCurryRice)
print(testPlate in testOrder)
for dish in testOrder:
    print(dish)
    print(testPlate == dish)