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
        # board = Board('easy')
        # board.draw_matrice()
        # board.draw_hints()
        # board.draw_mines()
        start_game = Board('easy', events)
        start_game.get_game().initialize_game()
        print('avant')
        print(start_game.get_game().get_grid_object().get_matrice())
        print(start_game.get_game().get_grid_object().get_list_cells_objects())
        start_game.get_game().initialize_game()
        print('apres')
        print(start_game.get_game().get_grid_object().get_matrice())
        print(start_game.get_game().get_grid_object().get_list_cells_objects())
        start_game.draw_matrice()
        start_game.draw_hints()
        start_game.draw_mines()
        # game.button_cell()


    pygame.display.flip()
