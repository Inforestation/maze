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