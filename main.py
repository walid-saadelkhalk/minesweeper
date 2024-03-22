from Board import *
from MouseClick import MouseClick
import pygame
from StateGame import StateGame

draw = False
button_draw = False
cell = None
first_click = False

while True :
    pygame.init()
    if draw == False:
        draw = True
        start_game = Board('easy')
        start_game.get_game().initialize_game()

    if button_draw == False:
        button_draw = True
        if cell != None:
            start_game.render_attributes(cell, screen)
        start_game.load_board(cell)

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        mouse = MouseClick(event)
        x_left, y_left = mouse.left_click()
        x_right, y_right = mouse.right_click()
        button_draw, first_click = start_game.get_game().make_a_left_click(x_left, y_left, button_draw, first_click)
        cell = start_game.get_game().make_a_right_click(x_right, y_right)
        if cell is not None:
            start_game.render_attributes(cell, screen)

    pygame.display.flip()