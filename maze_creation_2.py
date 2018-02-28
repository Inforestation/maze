from __future__ import division
from random import shuffle
from maze import UP, RIGHT, DOWN, LEFT, Maze


def move_forward(maze):  # proceed forward choosing random directions until there is no path available
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


def move_backward(maze):  # when no path is available, move backward using stack until there is a possible path
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


def all_board_cells_active(maze):  # checks if maze is finished
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


