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
            list_pos_left = list(pos)
            x = list_pos_left[0] // 30
            y = list_pos_left[1] // 30
            return x,y
    
    def right_click(self, event):
        if self.__event.type == pygame.MOUSEBUTTONDOWN and self.__event.button == 3:
            pos = pygame.mouse.get_pos()
            list_pos_right = list(pos)
            x = list_pos_right[0] // 30
            y = list_pos_right[1] // 30
            return x,y