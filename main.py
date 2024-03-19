from Board import *
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

        if event.type == pygame.MOUSEBUTTONDOWN:
            #Left click
            if event.button == 1:
                for button in board.get_button_list():
                    if button.render(screen):
                        print("Button clicked")

    pygame.display.flip()
