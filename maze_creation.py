from __future__ import division
from random import shuffle
from maze import *

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

            if new_maze.is_inside_board(new_x, new_y):
                if new_maze.is_not_active(new_x, new_y):
                    new_maze.stack.append((new_x, new_y))
                    new_maze.walls[new_x][new_y] = 0
                    new_maze.board[new_x][new_y].is_active = True
                    is_able_to_move_forward = True
                    break
        if not is_able_to_move_forward:
            if new_maze.all_board_cells_active():
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

        if new_maze.has_not_active_neighbour(x, y):
            is_able_to_move_forward = True
            new_maze.stack.append((x, y))

        stack_index = stack_index - 1
    return new_maze



