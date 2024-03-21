from Board import *
from MouseClick import MouseClick
import pygame
from StateGame import StateGame

draw = False

while True :
    pygame.init()

    if draw == False:
        draw = True
        start_game = Board('easy')
        start_game.load_board()

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        mouse = MouseClick(event)
        x_left, y_left = mouse.left_click()
        x_right, y_right = mouse.right_click()
        start_game.get_game().make_a_click(x_left, y_left)


    pygame.display.flip()
