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
        start_game.load_board()

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        mouse = MouseClick(event)
        x_left, y_left = mouse.left_click()
        x_right, y_right = mouse.right_click()
        button_draw = start_game.get_game().make_a_left_click(x_left, y_left, button_draw)
        cell = start_game.get_game().make_a_right_click(x_right, y_right)
        start_game.render_attributes(cell)

    pygame.display.flip()