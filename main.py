from Board import *
from MouseClick import MouseClick
import pygame
from StateGame import StateGame
from StateGraphic import StateGraphic

draw = False

while True :
    pygame.init()

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        mouse = MouseClick(event)
        x, y = mouse.left_click()
        x, y = mouse.right_click()

    menu = StateGraphic()
    menu.draw_buttons()

    if draw == False:
        draw = True
        start_game = Board('easy', x, y)
        start_game.load_board(x, y)


    pygame.display.flip()
