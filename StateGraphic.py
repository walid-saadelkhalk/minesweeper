import pygame
from Button import Button
from Image import Image

'''
This class is used to create the window menu of the game
we can choose the difficulty of the game
'''



class StateGraphic():
    def __init__(self):
        self.__button_list = []
        self.__selected_difficulty = None 

    def get_button_list(self): 
        return self.__button_list

    def get_selected_difficulty(self):
        return self.__selected_difficulty
    
    def set_selected_difficulty(self, difficulty):
        self.__selected_difficulty = difficulty

    # Method that draw the menu of the game
    def draw_menu(self):
        SCREEN_WIDTH_MENU = 930
        SCREEN_HEIGHT_MENU = 530

        screen_menu = pygame.display.set_mode((SCREEN_WIDTH_MENU, SCREEN_HEIGHT_MENU))
        pygame.display.set_caption("Minesweeper_menu")
        background_image = pygame.image.load("./assets/menu_bcg.png").convert()
        screen_menu.blit(background_image, (0, 0))

        easy_button = Button(147, 140, Image("./assets/easy_difficulty.png",(0, 0)).get_image_surface())
        self.__button_list.append(easy_button)
        medium_button = Button(85, 240,Image("./assets/medium_difficulty.png",(0, 0)).get_image_surface())
        self.__button_list.append(medium_button)
        hard_button = Button(147, 340,Image("./assets/hard_difficulty.png",(0, 0)).get_image_surface())
        self.__button_list.append(hard_button)
        for button in self.__button_list:
            button.draw(screen_menu)


    # Method that return the difficulty selected by the player
    def selected_difficulty(self, mouse):
        difficulties = ["easy", "medium", "hard"]
        for i in range(len(self.__button_list)): 
            x, y = mouse.left_click_menu()
            if x is not None and y is not None:
                if self.__button_list[i].get_rect().collidepoint(x, y):
                    self.__selected_difficulty = difficulties[i]
                    return 1
        return 0

        
                    