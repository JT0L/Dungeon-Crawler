from room import Room


class TxtLevelReader:
    @staticmethod
    def read_from_file(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.read().splitlines()
        return lines

    @staticmethod
    def parse_rooms(rooms_input):
        rooms = dict()
        for room_input_line in rooms_input:
            room = TxtLevelReader._read_room(room_input_line)
            assert room.name not in rooms  # check if this room name occurs for the first time
            rooms[room.name] = room

        return rooms

    @staticmethod
    def _read_room(room_input_line):
        parameters = room_input_line.split(" ")

        name = TxtLevelReader._get_name(parameters)
        doors = TxtLevelReader._get_doors(parameters, name)

        return Room(name, doors)

    @staticmethod
    def _get_initial_doors():
        doors = {
            "n": None,
            "s": None,
            "e": None,
            'w': None
        }

        return doors

    @staticmethod
    def _get_name(parameters):
        name = parameters[0]
        assert len(name) == 2

        return name

    @staticmethod
    def _get_doors(parameters, current_name):
        doors = TxtLevelReader._get_initial_doors()
        directions = {'n', 's', 'e', 'w'}

        for parameter in parameters[1:]:
            direction, neighbour_room_name = parameter.split(":")
            assert direction in directions
            assert neighbour_room_name != current_name
            directions.remove(direction)  # now we will be sure that room will have at most one door in each direction
            doors[direction] = neighbour_room_name

        return doors
