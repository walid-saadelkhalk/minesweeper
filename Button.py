'''
    This class is used to create buttons in the game

'''
class Button():
    def __init__(self, x, y, image, hover_image=None):
        self.__image = image
        self.__hover_image = hover_image
        self.__rect = self.__image.get_rect()
        self.__rect.topleft = (x, y)
    
    def get_rect(self):
        return self.__rect
    
    def get_position(self):
        return self.__rect.topleft

    # Method that draw button
    def draw(self, surface):
        surface.blit(self.__image, self.__rect)
