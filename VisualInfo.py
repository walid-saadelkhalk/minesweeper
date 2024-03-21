import pygame
from Button import Button

'''
class 
'''

class VisualInfo:
    def __init__(self, screen_width, visual_info_height):
        self.screen_width = screen_width
        self.visual_info_height = visual_info_height
        self.background_color = (192, 192, 192)
        self.button_color = (0, 0, 0)
        self.font = pygame.font.Font(None, 20)
        self.buttons = []

    def add_button(self, x, y, image, hover_image=None):
        button = Button( x, y, image, hover_image=None)
        # button_rect = pygame.Rect(pos[0], pos[1], 150, 50)
        self.buttons.append((button))

    def timer(self, time):
        text_surface = self.font.render(str(time), True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.screen_width.get_width() - 50, self.visual_info_height // 2))
        self.screen.blit(text_surface, text_rect)

    def draw(self, screen):
        # Draw background
        screen_width = self.screen_width.get_width()
        pygame.draw.rect(screen, self.background_color, (0, 0, screen_width, self.visual_info_height))

        # Draw buttons
        for button in self.buttons:
            button.draw(screen) 
        # for text, rect in self.buttons:
        #     pygame.draw.rect(screen, self.button_color, rect)
        #     text_surface = self.font.render(text, True, (255, 255, 255))
        #     text_rect = text_surface.get_rect(center=rect.center)
        #     screen.blit(text_surface, text_rect)

        