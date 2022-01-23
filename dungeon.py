from bfs import bfs


class Dungeon:
    __slots__ = 'rooms', 'x_size', 'y_size'

    def __init__(self, rooms, starting_room_name="a0"):
        self.rooms = rooms
        self.x_size = None
        self.y_size = None

        self._assert_condition_for_all_rooms(self._check_if_opposite_door_exists)
        self._preprocess(starting_room_name)  # we will preprocess dungeon in order to be able display it later
        self._assert_condition_for_all_rooms(self._check_if_rooms_are_adjacent)  # Still we must check if all the connected rooms are adjacent by edge (doors are not portals)

    def _assert_condition_for_all_rooms(self, checking_function):
        for room in self.rooms.values():
            for direction, neighbour_name in room.doors.items():  # in this approach we will check each door 2 times. We can do this better(for example check doors with bfs) but since dungeon is quite small(max 20 x 20) such optimalization will not bring that much value
                if neighbour_name is not None:
                    assert checking_function(room, self.rooms[neighbour_name], direction)

    @staticmethod
    def _check_if_rooms_are_adjacent(room_1, room_2, direction):  # left this unused parameter in order to fit this function into the pattern
        if room_1.x is not None and room_2.x is not None: # check if these rooms are in the connected area
            return abs(room_1.x - room_2.x) + abs(room_1.y - room_2.y) == 1

    @staticmethod
    def _check_if_opposite_door_exists(current_room, neighbour_room, direction):
        opposite_direction = Dungeon._get_opposite_direction(direction)
        return neighbour_room.doors[opposite_direction] == current_room.name

    def _normalize_coordinates(self, min_n, min_w):  # we are moving the origin of the coordinate system from the first chosen room to that in the left, upper corner
        for room in self.rooms.values():
            room.x = room.x - min_w
            room.y = room.y - min_n

    def _preprocess(self, starting_room_name):
        bfs(self, starting_room_name)  # first with bfs we will find part of the dungeon connected to the starting room
        min_n, min_e, max_s, max_w = self._get_size_of_dungeon()  # size is required for displaying the dungeon in the console

        self._normalize_coordinates(min_n, min_e)
        self.x_size = max_w - min_e + 1
        self.y_size = max_s - min_n + 1

    def _get_size_of_dungeon(self):
        min_n, min_w, max_s, max_e = 0, 0, 0, 0  #

        for room in self.rooms.values():
            min_n = min(room.y, min_n)
            min_w = min(room.x, min_w)
            max_s = max(room.y, max_s)
            max_e = max(room.x, max_e)

        return min_n, min_w, max_s, max_e

    @staticmethod
    def _get_opposite_direction(direction):
        if direction == 'n':
            return 's'
        elif direction == 's':
            return 'n'
        elif direction == 'e':
            return 'w'
        elif direction == 'w':
            return 'e'
        else:
            ValueError('Wrong direction')

