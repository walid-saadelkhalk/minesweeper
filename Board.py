from collections.abc import Iterable
import pygame
from Grid import Grid

"""
class Board for the render of the matrice game 

"""

SCREEN_WIDTH = 930
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Minesweeper")
screen.fill((255, 255, 0))


class Board:
    def __init__(self, level):
        self.__button_list = []
        self.__grid = Grid(level)
        self.__FIGURE_COLOR = {
            1: (0, 0, 255),
            2: (0, 255, 0),
            3: (255, 0, 0),
            4: (255, 200, 0),
            5: (128, 0, 0),
            6: (0, 128, 128),
            7: (0, 0, 0),
            8: (128, 128, 128),
        }

    def draw_matrice(self):
        total_x, total_y = self.__grid.matrice_size()
        for i in range(total_x):
            for j in range(total_y):
                pygame.draw.rect(screen, (0, 0, 0), (i * 30, j * 30, 30, 30), 1)
                pygame.draw.rect(
                    screen, (255, 255, 255), (i * 30 + 1, j * 30 + 1, 28, 28), 0
                )

    def color_figure(self, number):
        return self.__FIGURE_COLOR[number]


    def draw_hint(self):
        total_x, total_y = self.__grid.matrice_size()
        self.__grid.filled_matrice()
        for i in range(total_x):
            for j in range(total_y):
                if (
                    self.__grid.get_matrice()[i][j] != -1
                    and self.__grid.get_matrice()[i][j] != 0
                ):
                    color = self.color_figure(self.__grid.get_matrice()[i][j])
                    font = pygame.font.Font(None, 36)
                    text = font.render(
                        str(self.__grid.get_matrice()[i][j]), 1, color
                    )
                    screen.blit(text, (i * 30 + 9, j * 30 + 5))
