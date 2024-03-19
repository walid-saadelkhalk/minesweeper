import pygame
from Grid import Grid

'''
class Board for the render of the matrice game 

'''

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Minesweeper')
screen.fill((255, 255, 0))

class Board:
    def __init__(self, grid):         
        self.__button_list = []
        self.__grid = Grid('easy')


    




