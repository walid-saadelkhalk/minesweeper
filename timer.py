import pygame
import time

pygame.init()

WINDOW_WIDTH = 30
WINDOW_HEIGHT = 30
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("timer")


font = pygame.font.Font(None, 15)
text_color = (255, 255, 255)

def counter():
    try:
        for i in range(1000): 
            window.fill((0, 0, 0))
            text_surface = font.render(str(i).zfill(3), True, text_color)
            text_rect = text_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)) 
            window.blit(text_surface, text_rect)
            pygame.display.flip()  
            time.sleep(1)  
    except KeyboardInterrupt:
        pygame.quit()
        quit()
counter()
