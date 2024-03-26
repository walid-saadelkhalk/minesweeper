from Grid import Grid


'''
This class is the state of the game. It contains the grid object and the mouse click object.
It allows to manage the game.
'''
class StateGame:
    def __init__(self, level):
        self.__grid_object = Grid(level)
        self.__game_running = "en cours"

    def get_grid_object(self):
        return self.__grid_object
    def set_grid_object(self, grid_object):
        self.__grid_object = grid_object
    
    def get_game_running(self):
        return self.__game_running
    def set_game_running(self, game_running):
        self.__game_running = game_running

    # when the player click on a mine
    def lose(self, x, y):
        if self.__grid_object.get_matrice()[x][y] == -1:
            return True

    # when the only cells left are mines
    def win(self):
        for cell in self.__grid_object.get_list_cells_objects():
            if cell.get_state() == False:
                if self.__grid_object.get_matrice()[cell.get_position()[0]][cell.get_position()[1]] != -1:
                    return False
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
                                    self.next_move(i, j)
                            
    # When the player click on a cell
    def make_a_left_click(self, x, y, button_draw, first_click):
        for cell in self.__grid_object.get_list_cells_objects():
            if cell.get_position() == (x, y) and cell.get_state() == False:
                if first_click == 0:
                    for i in range(x-1, x+2):
                        for j in range(y-1, y+2):
                            for cell in self.__grid_object.get_list_cells_objects():
                                if cell.get_position() == (i, j):
                                    cell.set_state(True)
                                    button_draw = False
                                    first_click = 1
                else:
                    cell.set_state(True)
                    button_draw = False
                    if self.__grid_object.get_matrice()[x][y] == 0:
                        self.next_move(x, y)
                        if self.win():
                            self.__game_running = "gagné"
                    elif self.__grid_object.get_matrice()[x][y] == -1:
                        if self.lose(x, y):
                            self.__game_running = "perdu"
                    else:
                        if self.win():
                            self.__game_running = "gagné"
        return button_draw, first_click

    # When the player click on a cell with the right click
    def make_a_right_click(self, x, y):
        for cell in self.__grid_object.get_list_cells_objects():
            if cell.get_position() == (x, y) and cell.get_state() == False:
                if cell.get_attributes() == 0:
                    cell.set_attributes(1)
                elif cell.get_attributes() == 1:
                    cell.set_attributes(2)
                elif cell.get_attributes() == 2:
                    cell.set_attributes(0)
                return cell
