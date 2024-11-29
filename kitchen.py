class Kitchen:
    def __init__(self, name, selection):
        self.name = name
        self.isCooking = False
        self.selectionCoor = selection
        self.cookingCounter = 0

    def __repr__(self):
        return f'{self.name}'
    
    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        return (isinstance(other, Kitchen) and self.name == other.name)


#########
chopping = Kitchen('chopping', (4,4,0))
pan = Kitchen('pan', (5,4,0))
fryer = Kitchen('fryer', (6,4,0))