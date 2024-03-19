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
    
    
    

    