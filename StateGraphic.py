import pygame
from Button import Button
from Image import Image

'''
'''



class StateGraphic():
    def __init__(self):
        self.__button_list = []
        self.__game = None
        self.__selected_difficulty = None 

    def get_button_list(self): 
        return self.__button_list

    def get_selected_difficulty(self):
        return self.__selected_difficulty
    
    def set_selected_difficulty(self, difficulty):
        self.__selected_difficulty = difficulty

    
    def draw_menu(self):
        SCREEN_WIDTH_MENU = 930
        SCREEN_HEIGHT_MENU = 530

        screen_menu = pygame.display.set_mode((SCREEN_WIDTH_MENU, SCREEN_HEIGHT_MENU))
        pygame.display.set_caption("Minesweeper_menu")
        screen_menu.fill((255, 255, 255))
        return screen_menu

    # draw the difficulty buttons
    def draw_buttons(self):
        easy_button = Button(150, 50, Image("./assets/square.png",(0, 0)).get_image_surface())
        easy_button.draw(self.draw_menu())
        self.__button_list.append(easy_button)
        medium_button = Button(150, 120,Image("./assets/square.png",(0, 0)).get_image_surface())
        medium_button.draw(self.draw_menu())
        self.__button_list.append(medium_button)
        hard_button = Button(150, 190,Image("./assets/square.png",(0, 0)).get_image_surface())
        hard_button.draw(self.draw_menu())
        self.__button_list.append(hard_button)

    def selected_difficulty(self, mouse):
        difficulties = ["easy", "medium", "hard"]
        for i in range(len(self.__button_list)): 
            x, y = mouse.left_click_menu()
            if x is not None and y is not None:
                if self.__button_list[i].get_rect().collidepoint(x, y):
                    self.__selected_difficulty = difficulties[i]
                    return 1
        return 0

        
                    