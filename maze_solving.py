import maze as mz
from random import shuffle


def solve(maze):
    directions = [mz.UP, mz.RIGHT, mz.DOWN, mz.LEFT]
    creation_ended = False
    path = mz.Path()

    while not creation_ended:
        shuffle(directions)

        is_able_to_move_forward = False

        for direction in directions:
            last_x, last_y = path.short_path[-1]

            new_x = last_x + direction[0]
            new_y = last_y + direction[1]

            if maze.is_inside_board(new_x, new_y):
                if path.is_not_in_path(new_x, new_y):
                    if maze.is_in_stack(last_x, last_y, new_x, new_y):
                        path.short_path.append((new_x, new_y))
                        is_able_to_move_forward = True
                        break

        if not is_able_to_move_forward:
            path = return_to_last_crossing(maze, path)

        if path.short_path[-1][0] == maze.dimension - 1 and path.short_path[-1][1] == maze.dimension - 1:
            return path
    return None


def return_to_last_crossing(maze, path):
    directions = [mz.UP, mz.RIGHT, mz.DOWN, mz.LEFT]
    shuffle(directions)
    for a in range(len(path.short_path)):
        for direction in directions:
            last_x, last_y = path.short_path[-1 - a]

            new_x = last_x + direction[0]
            new_y = last_y + direction[1]

            if maze.is_inside_board(new_x, new_y):
                if path.is_not_in_path(new_x, new_y):
                    if maze.is_in_stack(last_x, last_y, new_x, new_y):
                        path.short_path.append((new_x, new_y))
                        return path
