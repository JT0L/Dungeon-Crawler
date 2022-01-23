import traceback

from dungeon import Dungeon
from printer import Printer
import game_logic
from txt_level_reader import TxtLevelReader


if __name__ == '__main__':
    FILE_PATH = "levels/level1.txt"

    rooms_input = TxtLevelReader.read_from_file(FILE_PATH)
    rooms = TxtLevelReader.parse_rooms(rooms_input)

    starting_room_name = game_logic.get_starting_point(rooms)  # it can come out that it is not connected graph. In this case we will only be displaying the part that can be reached from the staring room
    dungeon = Dungeon(rooms, starting_room_name)  # creating dungeon and asserting it is properly built

    printer = Printer(dungeon)  # setting up tool to display map

    game_logic.game(printer, dungeon, starting_room_name)  # starting the game


#  Probably it's unnecessary to catch exceptions in such a simple program but I thought I gave a slightly unclear answer about the exceptions so to clarify I'm using them here.
#  Below there is an alternative version of main using cascading exceptions:
#
# if __name__ == '__main__':
#     FILE_PATH = "levels/level1.txt"
#     while True:
#         try:  # maybe it's unnecessary but I thought I gave a slightly unclear answer about exceptions so to clarify I'm using them here
#             rooms_input = TxtLevelReader.read_from_file(FILE_PATH)
#             rooms = TxtLevelReader.parse_rooms(rooms_input)
#
#             starting_room_name = game_logic.get_starting_point(rooms)  # it can come out that it is not connected graph. In this case we will only be displaying the part that can be reached from the staring room
#             dungeon = Dungeon(rooms, starting_room_name)  # creating dungeon and asserting it is properly built
#             break
#
#         except AssertionError:  # as I use assert only for checking validity of dungeon, this block occurs only if level was not properly built
#             print(traceback.format_exc())
#             print("Wrong dungeon in the input file. Choose different level: ")
#             new_level_name = input("\n")
#             FILE_PATH = "levels/" + new_level_name
#
#         except Exception:  # I could just omit it but in order to show exception cascading I put this code
#             print(traceback.format_exc())
#             exit()
