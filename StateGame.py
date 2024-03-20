from Grid import Grid
from MouseClick import MouseClick

class StateGame:
    def __init__(self, level,event):
        self.__grid_object = Grid(level)
        self.__mouse_click = MouseClick(event)

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
            if cell.get_state() == False :
                cell.set_state(True)
                if self.__grid_object.get_matrice()[x][y] == -1:
                    return True
                
    def initialize_game(self):
        self.__grid_object.set_matrice([])
        self.__grid_object.filled_matrice()
        self.__grid_object.set_list_cells_objects([])
        self.__grid_object.fill_list_cells_objects()

    def next_move(self):
        x, y = self.__mouse_click.left_click()
        total_x, total_y = self.__grid_object.matrice_size()
        list_looking_for_zero = []
        if self.__grid_object.get_matrice()[x][y] == 0:
            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    if i >= 0 and i <= total_x and j >= 0 and j <= total_y:
                        if self.__grid_object.get_matrice()[i][j] != -1:
                            for cell in self.__grid_object.list_cells_objects:
                                if cell.get_position() == (i,j):
                                    cell.set_state(True)
                                    if cell.get_position() != (x,y):
                                        list_looking_for_zero.append(cell)
        for zero in list_looking_for_zero:
            if zero == 0 : 
                self.next_move()

                                    


            # if i > 0 and j > 0 and self.__matrice[i-1][j-1] != -1:
            #     self.__matrice[i-1][j-1] += 1
            # if i > 0 and self.__matrice[i-1][j] != -1:
            #     self.__matrice[i-1][j] += 1
            # if i > 0 and j < total_y-1 and self.__matrice[i-1][j+1] != -1:
            #     self.__matrice[i-1][j+1] += 1
            # if j > 0 and self.__matrice[i][j-1] != -1:
            #     self.__matrice[i][j-1] += 1
            # if j < total_y-1 and self.__matrice[i][j+1] != -1:
            #     self.__matrice[i][j+1] += 1
            # if i < total_x-1 and j > 0 and self.__matrice[i+1][j-1] != -1:
            #     self.__matrice[i+1][j-1] += 1
            # if i < total_x-1 and self.__matrice[i+1][j] != -1:
            #     self.__matrice[i+1][j] += 1
            # if i < total_x-1 and j < total_y-1 and self.__matrice[i+1][j+1] != -1:
            #     self.__matrice[i+1][j+1] += 1 
    
    
    

    