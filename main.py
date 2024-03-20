from Board import *
from MouseClick import MouseClick
import pygame
from StateGame import StateGame

draw = False

while True :
    pygame.init()

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        mouse_click = MouseClick(event)
        pos_left_click = mouse_click.left_click()
        
    if draw == False:
        draw = True
        start_game = Board('easy', events)
        start_game.draw_matrice()
        start_game.draw_hints()
        start_game.draw_mines()
        start_game.button_cell()


    pygame.display.flip()
