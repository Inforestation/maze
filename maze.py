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
        self.stack = [(0, 0)]  # a list of cells creating a maze form start to finish
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
                if self.is_not_active(x, y):
                    return False
        return True

    def has_not_active_neighbour(self, x, y):
        directions = [UP, RIGHT, DOWN, LEFT]
        for direction in directions:
            new_x = x + direction[0]
            new_y = y + direction[1]
            if self.is_inside_board(new_x, new_y):
                if self.is_not_active(new_x, new_y):
                    return True
        return False

    def is_not_active(self, x, y):
        if not self.board[x][y].is_active:
            return True
        else:
            return False

    @staticmethod
    def create_maze_stack_points(path_point, direction):
        if direction == UP:
            path_point_1 = (path_point[0] - 0.5, path_point[1] + 0.5)
            path_point_2 = (path_point[0] + 0.5, path_point[1] + 0.5)
            return path_point_1, path_point_2
        elif direction == RIGHT:
            path_point_1 = (path_point[0] + 0.5, path_point[1] + 0.5)
            path_point_2 = (path_point[0] + 0.5, path_point[1] - 0.5)
            return path_point_1, path_point_2
        else:
            return None

    def is_in_stack(self, last_x, last_y, new_x, new_y):
        for index, value in enumerate(self.stack):
            if value == (last_x, last_y):
                if index > 0:
                    if self.stack[index - 1] == (new_x, new_y):
                        return True
                if index < len(self.stack) - 1:
                    if self.stack[index + 1] == (new_x, new_y):
                        return True
        return False

    def is_step_not_in_stack(self, path_point, direction):  # checks whether two points are in stack
        path_point_1, path_point_2 = self.create_maze_stack_points(path_point, direction)
        return not self.is_in_stack(path_point_1[0], path_point_1[1], path_point_2[0], path_point_2[1])


class Path:
    def __init__(self):
        self.short_path = [(0, 0)]
        self.real_path = [(0, 0)]
        self.solution_path = [(0, 0)]

    def is_not_in_path(self, new_x, new_y):
        if (new_x, new_y) in self.short_path:
            return False
        return True
