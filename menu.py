from cmu_graphics import *
from PIL import Image

from plate import *
from dish import *

# current menu that the player has
# include all dishes that the player can cook & the customers can order
class Menu:

    # menu should be a list
    def __init__(self, menu):
        self.cafeMenu = menu

cafeMenu = Menu([sandwich, chickenCurryRice, tonkatsuCurryRice, tempuraCurryRice, chickenCurrySpaghetti, 
            tonkatsuCurrySpaghetti, tempuraCurrySpaghetti, chickenTomatoSauceSpaghetti, tonkatsuTomatoSauceSpaghetti, 
            tempuraTomatoSauceSpaghetti])