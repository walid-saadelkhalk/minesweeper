from Board import *
import pygame


while True :
    pygame.init()

    events = pygame.event.get()
    if pygame.event.Event(pygame.QUIT) in events:
        break
