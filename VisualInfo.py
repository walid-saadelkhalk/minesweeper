import pygame
from Button import Button

'''
class visual info for the render of the head bar of the game
we can see the number of bombs and the timer

'''

class VisualInfo:
    def __init__(self, screen_width, visual_info_height):
        self.screen_width = screen_width
        self.visual_info_height = visual_info_height
        self.background_color = (192, 192, 192)
        self.font = pygame.font.Font(None, 39)
        self.buttons = []
        self.bomb_counter = 0
        self.timer_value = 0


    #method that add a button to the visual info bar
    def add_button(self, x, y, image, hover_image=None):
        button = Button( x, y, image, hover_image=None)
        self.buttons.append((button))

    def set_bomb_counter(self, count):
        self.bomb_counter = count

    def set_timer_value(self, value):
        self.timer_value = value

    #method that draw the visual info bar
    def draw(self, screen):
        # Draw background
        screen_width = self.screen_width.get_width()
        pygame.draw.rect(screen, self.background_color, (0, 0, screen_width, self.visual_info_height))

        # Draw buttons
        for button in self.buttons:
            button.draw(screen) 

        # Draw bomb counter
        bomb_text = f"{self.bomb_counter}"
        bomb_surface = self.font.render(bomb_text, True, (0, 0, 0), (192, 192, 192))
        bomb_rect = bomb_surface.get_rect(midleft=(60, self.visual_info_height // 2))
        screen.blit(bomb_surface, bomb_rect)

        # Draw timer
        timer_text = f"{self.timer_value}"
        timer_surface = self.font.render(timer_text, True, (0, 0, 0), (192, 192, 192))
        timer_rect = timer_surface.get_rect(midright=(self.screen_width.get_width() - 60 , self.visual_info_height // 2))
        screen.blit(timer_surface, timer_rect)

        