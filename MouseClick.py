import pygame

'''
This class is used to manage the event click of the mouse
    
'''

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
        if self.__event.type == pygame.MOUSEBUTTONDOWN and self.__event.button == self.__LEFT:
            pos = pygame.mouse.get_pos()
            x = pos[0] // 30 
            y = (pos[1] - 50)  // 30 
            return x, y
        return None, None
    
    def right_click(self):
        if self.__event.type == pygame.MOUSEBUTTONDOWN and self.__event.button == self.__RIGHT:
            pos = pygame.mouse.get_pos()
            x = pos[0] // 30
            y = (pos[1] - 50) // 30
            return x, y
        return None, None
    
    # Method that return the position of the mouse when the left click is pressed
    def left_click_menu(self):
        if self.__event.type == pygame.MOUSEBUTTONDOWN and self.__event.button == self.__LEFT:
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            return x, y
        return None, None