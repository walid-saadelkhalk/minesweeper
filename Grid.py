'''
Class Grid is a 2D array of cells. Each cell has a state and a position.
The numbers of cells depends on the difficulty level of the game.
It allows to create the logical matrice of the game.
'''

class Grid:
    def __init__(self, level):
        self.__level = level
        self.__matrice = []
        self.__list_cells_objects = []

    
    def get_level(self):
        return self.__level
    
    def set_level(self, level):
        self.__level = level

    def get_matrice(self):
        return self.__matrice
    
    def set_matrice(self, matrice):
        self.__matrice = matrice
    
    def get_list_cells_objects(self):
        return self.__list_cells_objects 
    
    def set_list_cells_objects(self, list_cells_objects):
        self.__list_cells_objects = list_cells_objects

    # Return the size of the matrice depending on the level
    def matrice_size(self):
        if self.__level == 'easy':
            total_x = 7
            total_y = 8
        elif self.__level == 'medium':
            total_x = 16
            total_y = 16
        elif self.__level == 'hard':
            total_x = 31
            total_y = 16
        return total_x, total_y
    
    # Fill the matrice with information about the cells
    def fill_matrice(self):
        total_x, total_y = self.matrice_size()
        for i in range(total_x):
            self.__matrice.append([])
            for j in range(total_y):
                self.__matrice[i].append(0)


    

# grid = Grid('easy')
# grid.fill_matrice()
# print(grid.get_matrice())
    
    
    

    