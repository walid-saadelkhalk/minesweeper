from collections.abc import Iterable
import pygame
from Grid import Grid
from Button import Button
from Image import Image

"""
class Board for the render of the matrice game 

"""

SCREEN_WIDTH = 930
SCREEN_HEIGHT = 530

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Minesweeper")
screen.fill((255, 255, 255))


class Board:
    def __init__(self, level):
        self.__button_list = []
        self.__grid = Grid(level)
        # dictionnary with the color of the different figures
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
        self.__mines_list = []

    def get_button_list(self):
        return self.__button_list

    # Draw the matrice of the game with rect 
    def draw_matrice(self):
        total_x, total_y = self.__grid.matrice_size()
        for i in range(total_x):
            for j in range(total_y):
                pygame.draw.rect(screen, (0, 0, 0), (i * 30, j * 30, 30, 30), 1)
                pygame.draw.rect(
                    screen, (255, 255, 255), (i * 30 + 1, j * 30 + 1, 28, 28), 0
                )

    # Return the color of the figure depending on the number
    def color_figures(self, number):
        return self.__FIGURE_COLOR[number]

    # Draw the hint of the game that give the number of mines around the cell
    def draw_hints(self):
        total_x, total_y = self.__grid.matrice_size()
        self.__grid.filled_matrice()
        for i in range(total_x):
            for j in range(total_y):
                if (
                    self.__grid.get_matrice()[i][j] != -1
                    and self.__grid.get_matrice()[i][j] != 0
                ):
                    color = self.color_figures(self.__grid.get_matrice()[i][j])
                    font = pygame.font.Font(None, 36)
                    text = font.render(
                        str(self.__grid.get_matrice()[i][j]), 1, color
                    )
                    screen.blit(text, (i * 30 + 9, j * 30 + 5))


    # Draw the mines in the matrice
    def draw_mines(self):
        total_x, total_y = self.__grid.matrice_size()
        for i in range(total_x):
            for j in range(total_y):
                if self.__grid.get_matrice()[i][j] == -1:
                    self.__mines_list.append(
                        Image("./assets/mines.png", (i * 30, j * 30))
                    )
        for mines in self.__mines_list:
            mines.draw_image(screen)


    def button_cell(self):
        total_x, total_y = self.__grid.matrice_size()
        for i in range(total_x):
            for j in range(total_y):
                button = Button(
                    i * 30,
                    j * 30,
                    Image("./assets/square.png", (i * 30, j * 30)).get_image_surface(),
                )
                self.__button_list.append(button)
                button.draw(screen)


