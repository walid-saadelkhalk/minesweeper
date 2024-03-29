import random
from Cell import Cell


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
    def initial_matrice(self):
        total_x, total_y = self.matrice_size()
        for i in range(total_x):
            self.__matrice.append([])
            for j in range(total_y):
                self.__matrice[i].append(0)

    # Define randomly the number of mines depending on the level
    def mine_number(self):
        if self.__level == 'easy':
            min_mine = 5
            max_mine = 11
            random_mine = random.randint(min_mine, max_mine)
        elif self.__level == 'medium':
            min_mine = 20
            max_mine = 41
            random_mine = random.randint(min_mine, max_mine)
        elif self.__level == 'hard':
            min_mine = 50
            max_mine = 99
            random_mine = random.randint(min_mine, max_mine)
        return random_mine
    
    # Place the mines in the matrice with the value -1
    def mine_in_matrice(self):
        mine_number = self.mine_number()
        total_x, total_y = self.matrice_size()
        for i in range(mine_number):
            x = random.randint(0, total_x-1)
            y = random.randint(0, total_y-1)
            for cell in self.__list_cells_objects:
                if cell.get_position() == (x, y) and cell.get_state() == False:    
                    if self.__matrice[x][y] != -1:
                        self.__matrice[x][y] = -1
                    else:
                        i -= 1

    # Fill the matrice with the hint number around each cell clicked
    def fill_number_hint(self):
        total_x, total_y = self.matrice_size()
        for i in range(total_x):
            for j in range(total_y):
                if self.__matrice[i][j] == -1:
                    if i > 0 and j > 0 and self.__matrice[i-1][j-1] != -1:
                        self.__matrice[i-1][j-1] += 1
                    if i > 0 and self.__matrice[i-1][j] != -1:
                        self.__matrice[i-1][j] += 1
                    if i > 0 and j < total_y-1 and self.__matrice[i-1][j+1] != -1:
                        self.__matrice[i-1][j+1] += 1
                    if j > 0 and self.__matrice[i][j-1] != -1:
                        self.__matrice[i][j-1] += 1
                    if j < total_y-1 and self.__matrice[i][j+1] != -1:
                        self.__matrice[i][j+1] += 1
                    if i < total_x-1 and j > 0 and self.__matrice[i+1][j-1] != -1:
                        self.__matrice[i+1][j-1] += 1
                    if i < total_x-1 and self.__matrice[i+1][j] != -1:
                        self.__matrice[i+1][j] += 1
                    if i < total_x-1 and j < total_y-1 and self.__matrice[i+1][j+1] != -1:
                        self.__matrice[i+1][j+1] += 1 

    # fill the matrice with the mines and the hint numbers
    def filled_matrice(self):
        self.initial_matrice()
        self.mine_in_matrice()
        self.fill_number_hint()

    # Fill the list of cells objects with objetcs of class Cell
    def fill_list_cells_objects(self):
        total_x, total_y = self.matrice_size()
        for i in range(total_x):
            for j in range(total_y):
                cell = Cell(i, j, False)
                self.__list_cells_objects.append(cell)