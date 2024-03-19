from Grid import Grid

class StateGame:
    def __init__(self, level):
        self.__grid_object = Grid(level)

    def get_grid_object(self):
        return self.__grid_object
    
    def set_grid_object(self, grid_object):
        self.__grid_object = grid_object


    def lose(self):
       return self.__grid_object.lose()

    def win(self):
        for cell in self.__grid_object.list_cells_objects:
            if cell == -1 and cell.get_state() == False:
                return True
            elif  
            pass