from Board import *
from MouseClick import MouseClick
import pygame
from StateGraphic import StateGraphic

pygame.init()
draw = False
hihi = False
button_draw = False

# Stage of the game
MENU_SCREEN = 0
GAME_SCREEN = 1

CURRENT_SCREEN = MENU_SCREEN

while True:

    if CURRENT_SCREEN == MENU_SCREEN:
        menu = StateGraphic()
        if not hihi:
            hihi = True
            menu.draw_menu()
            menu.draw_buttons()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            mouse = MouseClick(event) 
            CURRENT_SCREEN = menu.selected_difficulty(mouse)

    elif CURRENT_SCREEN == GAME_SCREEN:
        print(CURRENT_SCREEN)
        if not draw:
            draw = True
            print("6")
            game = Board(menu.get_selected_difficulty())
            print("7")
            print(menu.get_selected_difficulty())
            print("8")
            game.get_game().initialize_game()
            print("9")
        if not button_draw:
            button_draw = True
            print("10")
            game.load_board()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            mouse = MouseClick(event)
            x_left, y_left = mouse.left_click()
            x_right, y_right = mouse.right_click()
            button_draw = game.get_game().make_a_click(x_left, y_left, button_draw)
        game.update_display()

    pygame.display.update()  

