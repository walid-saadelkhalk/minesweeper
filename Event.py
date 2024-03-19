class Event:
    def __init__(self, position):
        self.__position = position

    def get_position(self):
        return self.__position
    
    def set_position(self, position):
        self.__position = position

    def left_click(self, position):
        return position
    
    def right_click(self, position):
        return position