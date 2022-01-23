class Printer:
    def __init__(self, dungeon):
        self.x_size = dungeon.x_size
        self.y_size = dungeon.y_size
        self.map_matrix = [[None for _ in range(self.x_size)] for _ in range(self.y_size)]

        self._update_map_matrix(dungeon)

    def _update_map_matrix(self, dungeon):
        for room in dungeon.rooms.values():
            self.map_matrix[room.y][room.x] = room

    def print_map(self, current_room_name):
        print()
        for row in self.map_matrix:
            Printer._print_row(row, current_room_name)

    @staticmethod
    def _print_row(row, current_room_name):
        gap_below = ""
        for room in row:
            if room is None:
                print("   ", end="")
                gap_below += "   "
            else:
                gap_below = Printer._print_room(room, gap_below, current_room_name)

        Printer._print_gap_between_rows(gap_below)

    @staticmethod
    def _print_room(room, gap_below, current_room_name):
        if room.name != current_room_name:
            print(room.name, end="")
        else:
            print("**", end="")

        if room.doors['e'] is not None:
            print("-", end="")
        else:
            print(" ", end="")

        if room.doors['s'] is not None:
            gap_below += "|  "
        else:
            gap_below += "   "

        return gap_below

    @staticmethod
    def _print_gap_between_rows(gap_below):
        print()
        print(gap_below)
