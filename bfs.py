from collections import deque


def _bfs_init(dungeon, starting_room_name):
    visited = {}
    for room_name in dungeon.rooms:
        visited[room_name] = False

    visited[starting_room_name] = True
    starting_room = dungeon.rooms[starting_room_name]
    starting_room.x = 0
    starting_room.y = 0
    queue = deque()
    queue.append(starting_room_name)

    return queue, visited


def bfs(dungeon, starting_room_name):

    queue, visited = _bfs_init(dungeon, starting_room_name)

    while queue:
        current_room_name = queue.popleft()
        current_room = dungeon.rooms[current_room_name]

        for direction, neighbour_name in current_room.doors.items():
            if neighbour_name is not None:
                _process_node(dungeon, direction, neighbour_name, current_room, queue, visited)


def _process_node(dungeon, direction, neighbour_name, current_room, queue, visited):
    neighbour = dungeon.rooms[neighbour_name]
    if not visited[neighbour_name]:
        visited[neighbour_name] = True
        neighbour.set_coordinates(current_room.x, current_room.y, direction)
        queue.append(neighbour_name)
