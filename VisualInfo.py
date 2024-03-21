'''
class 
'''

class Header():
    def __init__(self, screen, x, y):   
        self.__screen = screen
        self.__x = x
        self.__y = y
        self.__font = pygame.font.Font(None, 36)
        self.__text = self.__font.render("Minesweeper", True, (0, 0, 0))
        self.__text_rect = self.__text.get_rect()
        self.__text_rect.topleft = (self.__x, self.__y)
        