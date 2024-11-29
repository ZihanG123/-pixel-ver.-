class Kitchen:
    def __init__(self, name, selection):
        self.name = name
        self.isCooking = False
        self.selectionCoor = selection
        self.cookingCounter = 0

#########
chopping = Kitchen('chopping', (4,4,0))
pan = Kitchen('pan', (5,4,0))
fryer = Kitchen('fryer', (6,4,0))