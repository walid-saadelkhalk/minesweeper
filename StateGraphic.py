import pygame
from Button import Button
from Image import Image

'''
'''

SCREEN_WIDTH_MENU = 930
SCREEN_HEIGHT_MENU = 530

screen_menu = pygame.display.set_mode((SCREEN_WIDTH_MENU, SCREEN_HEIGHT_MENU))
pygame.display.set_caption("Minesweeper_menu")
screen_menu.fill((255, 255, 255))

class StateGraphic():
    def __init__(self):
        self.__button_list = []
        self.__game = None

    # draw the difficulty buttons
    def draw_buttons(self):
        easy_button = Button(150, 50, Image("./assets/square.png",(0, 0)).get_image_surface())
        easy_button.draw(screen_menu)
        medium_button = Button(150, 120,Image("./assets/square.png",(0, 0)).get_image_surface())
        medium_button.draw(screen_menu)
        hard_button = Button(150, 190,Image("./assets/square.png",(0, 0)).get_image_surface())
        hard_button.draw(screen_menu)






