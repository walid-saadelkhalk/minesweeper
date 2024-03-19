import pygame
import time

class Button():
    def __init__(self, x, y, text, font, scale, color, hover_color):
        self.text = text
        self.font = font
        self.color = color
        self.hover_color = hover_color
        self.clicked = False
        self.active = True
        self.last_click_time = time.time()

        self.create_button(x, y, scale)

    def create_button(self, x, y, scale):
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))


    # def check_clicked(self):
    #     action = False
    #     pos = pygame.mouse.get_pos()
    #     if self.clicked and time.time() - self.last_click_time < 0.5:

    #         return False
    #     if self.rect.collidepoint(pos) and get_mouse_click():
    #             self.last_click_time = time.time()
    #             self.clicked = True
    #             action = True
    #     else:
    #         self.clicked = False


    #     return action

    def render(self, screen):
        if self.active:
            self.draw(screen)
            return self.check_clicked()
        else:
            return False