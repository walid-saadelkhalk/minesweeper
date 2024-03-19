'''
Class Cell is a single cell of the game. It has a state and a position.
It allows to create the logical cells of the game.
When the game starts, the cells are hidden. When the player clicks on a cell, the state of the cell changes.
'''

class Cell:
    def __init__(self, x, y, state = False):
        self.__state = state
        self.__position = (x,y)

    
    def get_state(self):
        return self.__state
    def set_state(self, state):
        self.__state = state   

    def get_position(self):
        return self.__position
    def set_position(self, position):
        self.__position = position



