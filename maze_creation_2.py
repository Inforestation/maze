from random import shuffle
import matplotlib.pyplot as plt

DIMENSION = 10
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


def move_forward(maze, steps_count):
    new_maze = maze
    directions = [UP, RIGHT, DOWN, LEFT]

    for step in range(steps_count):
        shuffle(directions)

        is_able_to_move_forward = False

        for direction in directions:
            new_x, new_y = new_maze.stack[-1]

            new_x = new_x + direction[0]
            new_y = new_y + direction[1]

            # if direction == UP:
            #     new_y = new_y + 1
            # elif direction == RIGHT:
            #     new_x = new_x + 1
            # elif direction == DOWN:
            #     new_y = new_y - 1
            # elif direction == LEFT:
            #     new_x = new_x - 1

            if is_inside_board(new_maze, new_x, new_y):
                if is_not_active(new_maze, new_x, new_y):
                    new_maze.stack.append((new_x, new_y))
                    new_maze.board[new_x][new_y].is_active = True
                    is_able_to_move_forward = True
                    break
        if not is_able_to_move_forward:
            new_maze = move_backward(new_maze)
        print step
    print new_maze.stack
    return new_maze


def move_backward(maze):
    if all_board_cells_active(maze): return None #!

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
    for x in range(DIMENSION):
        for y in range(DIMENSION):
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
    plt.ylim([-1, 11])
    plt.xlim([-1, 11])
    plt.show()



maze = Maze(DIMENSION)
maze = move_forward(maze, 100)
show_board(maze)
