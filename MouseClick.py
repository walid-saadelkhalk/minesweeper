import pygame

class MouseClick:
    def __init__(self, event):
        self.__event = event
        self.__LEFT = 1
        self.__RIGHT = 3

    def get_position(self):
        return self.__event
    
    def set_position(self, event):
        self.__event = event

    def left_click(self):
        if self.__event.type == pygame.MOUSEBUTTONDOWN and self.__event.button == 1:
            pos = pygame.mouse.get_pos()
            return pos
    
    def right_click(self, event):
        if self.__event.type == pygame.MOUSEBUTTONDOWN and self.__event.button == 3:
            pos = pygame.mouse.get_pos()
            return pos