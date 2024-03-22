from Board import *
from MouseClick import MouseClick
import pygame
# from StateGame import StateGame
# from StateGraphic import StateGraphic

pygame.init()
draw = False
button_draw = False

while True:

    if not draw:
        draw = True
        start_game = Board('medium')
        start_game.get_game().initialize_game()
        start_game.size_screen()

    if not button_draw:
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
        button_draw = start_game.get_game().make_a_click(x_left, y_left, button_draw)

            #     # Si l'utilisateur clique sur un bouton dans le menu
            # if menu.handle_click(event.pos):
            #     # Récupérez la difficulté choisie dans le menu
            #     difficulty = menu.get_difficulty()
            #     # Fermez la fenêtre du menu
            #     menu.close()
            #     # Lancez la fenêtre du jeu avec la difficulté choisie
            #     game_window = GameWindow(difficulty)
            #     game_window.run_game()

    pygame.display.flip()  