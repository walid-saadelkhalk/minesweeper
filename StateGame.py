from Grid import Grid
from MouseClick import MouseClick

class StateGame:
    def __init__(self, level):
        self.__grid_object = Grid(level)
        self.__mouse_click = MouseClick()

    def get_grid_object(self):
        return self.__grid_object
    
    def set_grid_object(self, grid_object):
        self.__grid_object = grid_object


    def lose(self):
        x, y = self.__mouse_click.left_click()
        if self.__grid_object.get_matrice()[x][y] == -1:
            return True


    def win(self):
        x, y = self.__mouse_click.left_click()
        for cell in self.__grid_object.list_cells_objects:
            if cell.get_state() == False and self.__grid_object.get_matrice()[x][y] == -1:
                return True
            
    

    