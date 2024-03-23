
from collections.abc import Iterable
import pygame
from StateGame import StateGame
from Button import Button
from Image import Image
from VisualInfo import VisualInfo

"""
class Board for the render of the matrice game 
"""

# SCREEN_WIDTH = 930
# SCREEN_HEIGHT = 530

# matrice_size = self.__game.get_grid_object().matrice_size()
# cell_size = 30 
# screen_width = matrice_size[0] * cell_size +5
# screen_height = matrice_size[1] * cell_size + 50
# screen = pygame.display.set_mode((screen_width, screen_height))

# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



class Board:
    def __init__(self, level):
        self.__screen = None
        self.__button_list = []
        self.__visual_info_height = 50  
        self.__cell_size = 30
        self.__game = StateGame(level)
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

    def get_game(self):
        return self.__game
    def get_button_list(self):
        return self.__button_list
    
    def size_screen(self):
        matrice_size = self.__game.get_grid_object().matrice_size()
        screen_width = matrice_size[0] * self.__cell_size
        screen_height = matrice_size[1] * self.__cell_size + self.__visual_info_height
        self.__screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Minesweeper")
        return self.__screen

    # Draw the matrice of the game with rect
    def draw_matrice(self):
        if self.__screen is not None: 
            total_x, total_y = self.__game.get_grid_object().matrice_size()
            grid_surface = pygame.Surface((total_x * self.__cell_size, total_y * self.__cell_size))
            
            for i in range(total_x):
                for j in range(total_y):
                    cell_rect = pygame.Rect(i * self.__cell_size, j * self.__cell_size, self.__cell_size, self.__cell_size)
                    pygame.draw.rect(grid_surface, (255, 255, 255), cell_rect)
                    pygame.draw.rect(grid_surface, (0, 0, 0), cell_rect, 1)

            self.__screen.blit(grid_surface, (0, self.__visual_info_height))
        else:
            print("The screen is not defined 0")

    # Return the color of the figure depending on the number
    def color_figures(self, number):
        return self.__FIGURE_COLOR[number]
    
    # Draw the hint of the game that give the number of mines around the cell
    def draw_hints(self):
        if self.__screen is not None:
            total_x, total_y = self.__game.get_grid_object().matrice_size()
            self.__game.get_grid_object()
            for i in range(total_x):
                for j in range(total_y):
                    value = self.__game.get_grid_object().get_matrice()[i][j]
                    if value != -1 and value != 0:
                        if value < 1 or value > 8:
                            print(f"Invalid value at position ({i}, {j}): {value}")
                        else:
                            color = self.color_figures(value)
                            font = pygame.font.Font(None, 36)
                            text = font.render(str(value), 1, color)
                            self.__screen.blit(text, (i * self.__cell_size + 9, j * self.__cell_size + 5 + self.__visual_info_height))
        else:
            print("The screen is not defined 1")

    # Draw the mines in the matrice
    def draw_mines(self):
        if self.__screen is not None:
            total_x, total_y = self.__game.get_grid_object().matrice_size()
            for i in range(total_x):
                for j in range(total_y):
                    if self.__game.get_grid_object().get_matrice()[i][j] == -1:
                        self.__mines_list.append(Image("./assets/mines.png", (i * self.__cell_size, j * self.__cell_size + self.__visual_info_height)))
            for mines in self.__mines_list:
                mines.draw_image(self.__screen)
        else:
            print("The screen is not defined 2")

    def button_cell(self):
        if self.__screen is not None:
            self.__button_list = []
            for cell in self.__game.get_grid_object().get_list_cells_objects():
                if cell.get_state() == False:
                    i, j = cell.get_position()
                    button = Button(i * self.__cell_size, j * self.__cell_size + self.__visual_info_height, Image("./assets/square.png", (i * self.__cell_size, j * self.__cell_size + self.__visual_info_height)).get_image_surface())
                    self.__button_list.append(button)
                    button.draw(self.__screen)
                    if cell.get_attributes() != 0:
                            self.render_attributes(cell)
        else:
            print("The screen is not defined 3")
            

    # Render the attributes of the cell
    def render_attributes(self, cell):
        if cell is not None:
            i, j = cell.get_position()
            x = i * 30
            y = j * 30
            y = y + 50
            button = Button(x, y, Image("./assets/square.png", (x, y)).get_image_surface())
            button.draw(self.__screen)

            if cell.get_attributes() == 1:
                image = Image("./assets/flag.png", (x, y))
                image.draw_image(self.__screen)
            elif cell.get_attributes() == 2:
                image = Image("./assets/doubt.png", (x, y))
                image.draw_image(self.__screen)

    # Load the board with the cells

    def load_board(self):
        # Load game board
        self.draw_matrice()
        self.draw_mines()
        self.draw_hints()
        self.button_cell()

        # Load visual info bar
        self.visual_info = VisualInfo(self.__screen, self.__visual_info_height)
        self.visual_info.add_button(0, 8, Image("./assets/back.png", (0, 0)).get_image_surface())
        self.visual_info.add_button((self.__screen.get_width() // 2  - 15), 8, Image("./assets/smiley_ok.png", (0, 0)).get_image_surface())
        self.visual_info.add_button(self.__screen.get_width() - self.__cell_size, 8, Image("./assets/question_mark.png", (0, 0)).get_image_surface())
        self.visual_info.draw(self.__screen)

