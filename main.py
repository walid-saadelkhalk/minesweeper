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

    events = pygame.event.get()
    if pygame.event.Event(pygame.QUIT) in events:
        break

    pygame.display.flip()
