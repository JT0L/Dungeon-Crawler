class Room:
    __slots__ = 'name', 'doors', 'x', 'y'

    def __init__(self, name, doors, x=None, y=None):
        self.name = name
        self.doors = doors
        self.x = x
        self.y = y

    def set_coordinates(self, prev_x, prev_y, direction):
        """
        I chose these axes:
                o - >
                |
                v
        """
        if direction == 'n':
            self.x = prev_x
            self.y = prev_y - 1
        elif direction == 's':
            self.x = prev_x
            self.y = prev_y + 1
        elif direction == 'e':
            self.x = prev_x + 1
            self.y = prev_y
        elif direction == 'w':
            self.x = prev_x - 1
            self.y = prev_y
        else:
            ValueError('Wrong direction')
