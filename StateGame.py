from Grid import Grid
from MouseClick import MouseClick

'''
This class is the state of the game. It contains the grid object and the mouse click object.
It allows to manage the game.
'''

class StateGame:
    def __init__(self, level):
        self.__grid_object = Grid(level)
        # self.__x = x
        # self.__y = y

    def get_grid_object(self):
        return self.__grid_object

    def set_grid_object(self, grid_object):
        self.__grid_object = grid_object

    # def get_x(self):
    #     return self.__x
    
    # def set_x(self, x):
    #     self.__x = x

    # def get_y(self):
    #     return self.__y
    
    # def set_y(self, y):
    #     self.__y = y

    # when the player click on a mine
    def lose(self, x, y):
        if self.__grid_object.get_matrice()[x][y] == -1:
            return True

    # when the only cells left are mines
    def win(self, x, y):
        for cell in self.__grid_object.get_list_cells_objects():
            if cell.get_state() == False:
                cell.set_state(True)
                if self.__grid_object.get_matrice()[x][y] == -1:
                    return True

    # When the player want to restart the game
    def initialize_game(self):
        self.__grid_object.set_matrice([])
        self.__grid_object.filled_matrice()
        self.__grid_object.set_list_cells_objects([])
        self.__grid_object.fill_list_cells_objects()

    # When the player click on a "zero" cell #recursive function
    def next_move(self, x, y):
        total_x, total_y = self.__grid_object.matrice_size()
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i >= 0 and i <= total_x and j >= 0 and j <= total_y :
                    for cell in self.__grid_object.get_list_cells_objects():
                        if cell.get_state() == False:
                            if cell.get_position() == (i, j):
                                cell.set_state(True)
                                if self.__grid_object.get_matrice()[i][j] == 0:
                                    self.next_move(x, y)
                            
    # When the player click on a cell
    def make_a_click(self, x, y):
        if x != -1 and y != -1:
            for cell in self.__grid_object.get_list_cells_objects():
                if cell.get_position() == (x, y) and cell.get_state() == False:
                    cell.set_state(True)
                    if self.__grid_object.get_matrice()[x][y] == 0:
                        self.next_move(x, y)
                        self.win(x, y)
                    elif self.__grid_object.get_matrice()[x][y] == -1:
                        self.lose(x, y)
                    else:
                        self.win(x, y)
