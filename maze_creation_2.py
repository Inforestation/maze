from __future__ import division
from random import shuffle
import matplotlib.pyplot as plt
import numpy as np

DIMENSION = 20
UP = (0, 1)
RIGHT = (1, 0)
DOWN = (0, -1)
LEFT = (-1, 0)

class Cell:

    def __init__(self):
        self.wall_top = True
        self.wall_right = True
        self.wall_bottom = True
        self.wall_left = True
        self.is_active = False

class Maze:

    def __init__(self, dimension):
        self.board = [[Cell() for _ in range(dimension)] for _ in range(dimension)]
        self.stack = [(0, 0)]
        self.dimension = dimension
        self.board[0][0].is_active = True
        self.walls = np.ones((dimension, dimension))


def move_forward(maze):
    new_maze = maze
    directions = [UP, RIGHT, DOWN, LEFT]
    creation_ended = False
    while not creation_ended:
        shuffle(directions)

        is_able_to_move_forward = False

        for direction in directions:
            new_x, new_y = new_maze.stack[-1]

            new_x = new_x + direction[0]
            new_y = new_y + direction[1]

            if is_inside_board(new_maze, new_x, new_y):
                if is_not_active(new_maze, new_x, new_y):
                    new_maze.stack.append((new_x, new_y))
                    new_maze.walls[new_x][new_y] = 0
                    new_maze.board[new_x][new_y].is_active = True
                    is_able_to_move_forward = True
                    break
        if not is_able_to_move_forward:
            if all_board_cells_active(new_maze):
                creation_ended = True
            else:

                new_maze = move_backward(new_maze)
    return new_maze


def move_backward(maze):
    new_maze = maze
    is_able_to_move_forward = False
    stack_index = -2
    while not is_able_to_move_forward:
        x, y = new_maze.stack[stack_index]

        if has_not_active_neighbour(new_maze, x, y):
            is_able_to_move_forward = True
            new_maze.stack.append((x, y))

        stack_index = stack_index - 1
    return new_maze


def all_board_cells_active(maze):
    for x in range(maze.dimension):
        for y in range(maze.dimension):
            if not maze.board[x][y].is_active:
                return False
    return True


def has_not_active_neighbour(maze, x, y):
    directions = [UP, RIGHT, DOWN, LEFT]
    for direction in directions:
        new_x = x + direction[0]
        new_y = y + direction[1]
        if is_inside_board(maze, new_x, new_y):
            if not maze.board[new_x][new_y].is_active:
                return True
    return False


def is_inside_board(maze, x, y):
    if maze.dimension > x >= 0 and maze.dimension > y >= 0:
        return True
    else:
        return False


def is_not_active(maze, x, y):
    if not maze.board[x][y].is_active:
        return True
    else:
        return False


def show_board(maze):
    x, y = zip(*(maze.stack))
    plt.plot(x, y)
    plt.ylim([-1, maze.dimension + 1])
    plt.xlim([-1, maze.dimension + 1])
    plt.show()


def show_maze(maze):
    directions = [UP, RIGHT]
    coordinate_min = -0.5
    coordinate_max = float(maze.dimension) - 0.5
    maze_walls = []

    for x in np.arange(coordinate_min, coordinate_max):
        for y in np.arange(coordinate_min, coordinate_max):
            for direction in directions:
                start_point = (x, y)
                end_point = (x + direction[0], y + direction[1])
                if coordinate_min < end_point[0] < coordinate_max and coordinate_min < end_point[1] < coordinate_max:
                    if is_not_in_path(start_point, maze, direction):
                        maze_walls.append((start_point, end_point))
                    else:
                        print end_point
    print 'end'


def is_not_in_path(start_point, maze, direction):
    if direction == UP:
        path_point_1 = (start_point[0] - 0.5, start_point[1] + 0.5)
        path_point_2 = (start_point[0] + 0.5, start_point[1] + 0.5)
    elif direction == RIGHT:
        path_point_1 = (start_point[0] + 0.5, start_point[1] + 0.5)
        path_point_2 = (start_point[0] + 0.5, start_point[1] - 0.5)
    else:
        return False

    for index, coordinates in enumerate(maze.stack):
        if coordinates == path_point_1:
            if index > 0:
                if maze.stack[index - 1] == path_point_2:
                    return False
            if index < len(maze.stack) - 1:
                if maze.stack[index + 1] == path_point_2:
                    return False
    return True


maze = Maze(DIMENSION)
maze = move_forward(maze)
show_board(maze)
show_maze(maze)
