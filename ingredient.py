from cmu_graphics import *
from PIL import Image

from plate import *
from dish import *
from player import *

class Ingredient:

    # name should be a string
    def __init__(self,name):

        self.name = name
        self.image = f'./images/hold/{name}HoldImage.PNG'
        

    def __repr__(self):
        return f'{self.name}'
    
    def __hash__(self):
        return hash(str(self))

    def __eq__(self,other):
        return (isinstance(other, Ingredient) and self.name == other.name)

