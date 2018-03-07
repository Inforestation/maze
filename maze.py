import numpy as np

UP = (0, 1)
RIGHT = (1, 0)
DOWN = (0, -1)
LEFT = (-1, 0)


class Cell: # cell with 4 walls

    def __init__(self):
        self.wall_top = True
        self.wall_right = True
        self.wall_bottom = True
        self.wall_left = True
        self.is_active = False


class Maze:

    def __init__(self, dimension):
        self.board = [[Cell() for _ in range(dimension)] for _ in range(dimension)]
        self.stack = [(0, 0)] # a list of cells creating a maze form start to finish
        self.dimension = dimension
        self.board[0][0].is_active = True
        self.walls = np.ones((dimension, dimension))

    def is_inside_board(self, x, y):
        if self.dimension > x >= 0 and self.dimension > y >= 0:
            return True
        else:
            return False

    def all_board_cells_active(self):  # checks if maze is finished
        for x in range(self.dimension):
            for y in range(self.dimension):
                if not self.board[x][y].is_active:
                    return False
        return True

    def has_not_active_neighbour(self, x, y):
        directions = [UP, RIGHT, DOWN, LEFT]
        for direction in directions:
            new_x = x + direction[0]
            new_y = y + direction[1]
            if self.is_inside_board(new_x, new_y):
                if not self.board[new_x][new_y].is_active:
                    return True
        return False

    def is_not_active(self, x, y):
        if not self.board[x][y].is_active:
            return True
        else:
            return False

    def is_in_stack(self, last_x, last_y, new_x, new_y):
        for index, value in enumerate(self.stack):
            if value == (last_x, last_y):
                if self.stack[index + 1] == (new_x, new_y) or self.stack[index - 1] == (new_x, new_y):
                    return True
        return False


class Path:
    def __init__(self):
        self.short_path = [(0, 0)]

    def is_not_in_path(self, new_x, new_y):
        if (new_x, new_y) in self.short_path:
            return False
        return True
