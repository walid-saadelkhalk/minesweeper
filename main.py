from Board import *
from MouseClick import MouseClick
import pygame

draw = False

while True :
    pygame.init()
    if draw == False:
        draw = True
        board = Board('hard')
        board.draw_matrice()
        board.draw_hints()
        board.draw_mines()
        board.button_cell()

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        mouse_click = MouseClick(event)
        pos_left_click = mouse_click.left_click()

    pygame.display.flip()
