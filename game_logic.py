def game(printer, dungeon, current_room_name):
    while True:  # I left infinite loop as in example
        printer.print_map(current_room_name)
        current_room = dungeon.rooms[current_room_name]

        print(f"You are in room {current_room_name}")
        _print_possible_moves(dungeon, current_room_name)
        current_room_name = _move(dungeon, current_room)  # actual move


def get_starting_point(rooms):
    for rooms_name in rooms.keys():
        print(rooms_name, end=" ")

    starting_room_name = "x"
    while starting_room_name not in rooms.keys():
        starting_room_name = input("\nChoose staring room\n")

    return starting_room_name


def _print_possible_moves(dungeon, current_room_name):
    possible_moves = _get_possible_moves(dungeon, current_room_name)
    possible_moves_string = "".join(possible_moves)
    print(f"Possible moves: {possible_moves_string}")


def _get_possible_moves(dungeon, current_room_name):
    current_room = dungeon.rooms[current_room_name]
    possible_moves = []
    for direction, neighbour_name in current_room.doors.items():
        if neighbour_name is not None:
            possible_moves.append(direction)

    return possible_moves


def _move(dungeon, current_room):
    choice = input()
    print(f"Your choice: {choice}")
    for turn in choice:  # for each letter in user's choice
        set_of_choices = _get_possible_moves(dungeon, current_room.name)  # we check possible direction for the new position
        if turn in set_of_choices:
            current_room = _change_room(dungeon, current_room, turn)
        else:
            print("Wrong direction")  # I assumed that we will end move in the last allowed position
            break

    return current_room.name


def _change_room(dungeon, current_room, turn):
    new_room_name = current_room.doors[turn]
    new_room = dungeon.rooms[new_room_name]

    return new_room
