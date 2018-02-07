from __future__ import division
from random import shuffle
import matplotlib.pyplot as plt
import numpy as np

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


def add_paths(maze, ax):
    x, y = zip(*(maze.stack))
    ax.plot(x, y, color='black', lw=1.5)
    return ax


def add_maze(maze, ax):
    directions = [UP, RIGHT]
    coordinate_min = -0.5
    coordinate_max = float(maze.dimension) + 0.5
    maze_walls = []

    for x in np.arange(coordinate_min, coordinate_max):
        for y in np.arange(coordinate_min, coordinate_max):
            for direction in directions:
                start_point = (x, y)
                end_point = (x + direction[0], y + direction[1])
                if coordinate_min < end_point[0] < coordinate_max and coordinate_min < end_point[1] < coordinate_max:
                    if is_not_in_path(start_point, maze, direction):
                        maze_walls.append((start_point, end_point))

    maze_walls.append(((-0.5, maze.dimension - 0.5), (-0.5, -0.5)))
    maze_walls.append(((-0.5, -0.5), (maze.dimension - 0.5, -0.5)))

    for wall in maze_walls:
        x = []
        y = []
        for point in wall:
            x.append(point[0])
            y.append(point[1])
        ax.plot(x, y, color='k', lw=1.5)
    return ax


def show_all(maze):
    figure, ax = plt.subplots(nrows=1)
    add_maze(maze, ax)
    add_start_and_stop(maze, ax)
    #add_paths(maze, ax)
    ax.set_ylim([-1.5, maze.dimension + 0.5])
    ax.set_xlim([-1.5, maze.dimension + 0.5])
    ax.set_aspect('equal')
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.set_yticks([])
    ax.set_xticks([])
    plt.show()

def add_start_and_stop(maze, ax):
    start_point = (0, 0)
    end_point = (maze.dimension - 1, maze.dimension - 1)
    ax.scatter(start_point[0], start_point[1], color='b', lw=2)
    ax.scatter(end_point[0], end_point[0], color='r', lw=2)
    return ax


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


