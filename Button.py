class Button():
    def __init__(self, x, y, image, hover_image=None):
        self.__image = image
        self.__hover_image = hover_image
        self.__rect = self.__image.get_rect()
        self.__rect.topleft = (x, y)
        # self.__clicked = False
        # self.__active = True
        # self.__last_click_time = time.time()
    
    def get_rect(self):
        return self.__rect

    # Methode that draw button
    def draw(self, surface):
        surface.blit(self.__image, self.__rect)


    # def check_clicked(self):
    #     action = False
    #     pos = pygame.mouse.get_pos()
    #     if self.clicked and time.time() - self.last_click_time < 0.5:
    #         return False
    #     if self.rect.collidepoint(pos):
    #             self.last_click_time = time.time()
    #             self.clicked = True
    #             # print("Button clicked")
    #             action = True
    #     else:
    #         self.clicked = False
    #     return action

    # def render(self, screen):
    #     if self.__active:
    #         self.draw(screen)
            # return self.check_clicked()
        # else:
        #     return False