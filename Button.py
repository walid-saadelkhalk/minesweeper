import pygame
import time



class Button():
    def __init__(self, x, y, image, hover_image=None):
        self.image = image
        self.hover_image = hover_image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.active = True
        self.last_click_time = time.time()


    def draw(self, surface):
        surface.blit(self.image, self.rect)


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
    #     if self.active:
    #         self.draw(screen)
    #         return self.check_clicked()
    #     else:
    #         return False