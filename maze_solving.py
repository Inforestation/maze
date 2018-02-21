import maze as mz
from random import shuffle
import matplotlib.pyplot as plt
import numpy as np


def solve(maze):
    directions = [mz.UP, mz.RIGHT, mz.DOWN, mz.LEFT]
    creation_ended = False
    path = [(0, 0)]

    while not creation_ended:
        shuffle(directions)

        is_able_to_move_forward = False

        for direction in directions:
            last_x, last_y = path[-1]

            new_x = last_x + direction[0]
            new_y = last_y + direction[1]

            if is_inside_board(maze, new_x, new_y):
                if is_not_in_path(path, new_x, new_y):
                    if is_in_stack(last_x, last_y, new_x, new_y, maze):
                        path.append((new_x, new_y))
                        is_able_to_move_forward = True
                        break

        if not is_able_to_move_forward:
            #creation_ended = True
            path = return_to_last_crossing(maze, path)

        if path[-1][0] == maze.dimension - 1 and path[-1][1] == maze.dimension - 1:
            return path
    return None


def return_to_last_crossing(maze, path):
    directions = [mz.UP, mz.RIGHT, mz.DOWN, mz.LEFT]
    shuffle(directions)
    for a in range(len(path)):
        for direction in directions:
            last_x, last_y = path[-1-a]

            new_x = last_x + direction[0]
            new_y = last_y + direction[1]

            if is_inside_board(maze, new_x, new_y):
                if is_not_in_path(path, new_x, new_y):
                    if is_in_stack(last_x, last_y, new_x, new_y, maze):
                        path.append((new_x, new_y))
                        return path


def is_inside_board(maze, x, y):
    if maze.dimension > x >= 0 and maze.dimension > y >= 0:
        return True
    else:
        return False


def is_not_in_path(path, new_x, new_y):
    if (new_x, new_y) in path:
        return False
    return True


def is_in_stack(last_x, last_y, new_x, new_y, maze):
    for index, value in enumerate(maze.stack):
        if value == (last_x, last_y):
            if maze.stack[index + 1] == (new_x, new_y) or maze.stack[index - 1] == (new_x, new_y):
                return True # !!! IndexError: list index out of range
    return False
