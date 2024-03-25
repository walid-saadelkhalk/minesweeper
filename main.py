from Board import *
from MouseClick import MouseClick
import pygame
from StateGraphic import StateGraphic

pygame.init()
draw = False
menu_draw = False
button_draw = False
cell = None
first_click = False

# Stage of the game
MENU_SCREEN = 0
GAME_SCREEN = 1

CURRENT_SCREEN = MENU_SCREEN

while True:
    # Menu screen where we can choose the difficulty of the game
    if CURRENT_SCREEN == MENU_SCREEN:
        if not menu_draw:
            menu = StateGraphic()
            menu_draw = True
            menu.draw_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse = MouseClick(event)
                CURRENT_SCREEN = menu.selected_difficulty(mouse)

    # Game screen where we can play the game
    elif CURRENT_SCREEN == GAME_SCREEN:
        if not draw:
            draw = True
            game = Board(menu.get_selected_difficulty())
            game.get_game().initialize_game()
            game.size_screen()
            game.draw_visual_info()
            game.draw_visual_flag()
            game.back_menu()
        if not button_draw:
            button_draw = True
            game.load_board()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            mouse = MouseClick(event)
            x_left, y_left = mouse.left_click()
            x_right, y_right = mouse.right_click()
            button_draw = game.get_game().make_a_left_click(x_left, y_left, button_draw)
            game.game_running_render()
            cell = game.get_game().make_a_right_click(x_right, y_right)
            if game.back_menu() == 1:
                CURRENT_SCREEN = MENU_SCREEN
                draw = False
                menu_draw = False
                button_draw = False
                cell = None
                first_click = False
                break
            if cell is not None and cell.get_attributes() == 1 : 
                game.draw_visual_flag()
            elif cell is not None and cell.get_attributes() == 2 : 
                game.draw_visual_flag()
            elif cell is not None and cell.get_attributes() == 0 :
                game.draw_visual_flag()
            game.render_attributes(cell)


    pygame.display.update()  

