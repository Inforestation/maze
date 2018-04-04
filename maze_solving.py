import maze as mz
from random import shuffle
import numpy as np


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
                        path.real_path.append((new_x, new_y))
                        is_able_to_move_forward = True
                        break

        if not is_able_to_move_forward:
            path = return_to_last_crossing(maze, path)

        if path.short_path[-1][0] == maze.dimension - 1 and path.short_path[-1][1] == maze.dimension - 1:
            create_solution_path(path)
            return path
    return None


def return_to_last_crossing(maze, path):
    directions = [mz.UP, mz.RIGHT, mz.DOWN, mz.LEFT]
    shuffle(directions)
    real_path_origin = path.real_path[:]
    for a in range(len(path.real_path)):
        last_x, last_y = real_path_origin[-2 - a]
        path.real_path.append((last_x, last_y))
        for direction in directions:

            new_x = last_x + direction[0]
            new_y = last_y + direction[1]

            if maze.is_inside_board(new_x, new_y):
                if maze.is_in_stack(last_x, last_y, new_x, new_y):
                    if path.is_not_in_path(new_x, new_y):
                        path.short_path.append((new_x, new_y))
                        path.real_path.append((new_x, new_y))
                        return path


def create_solution_path(path):
    occurrences = []
    real_path_duplicate = set(path.real_path)

    for point1 in real_path_duplicate:
        point_occurrences = []
        for index, point2 in enumerate(path.real_path):
            if point1 == point2:
                point_occurrences.append(index)
        occurrences.append(point_occurrences)

    ranges_to_remove = []

    for index in range(len(occurrences) - 1, 0, -1):
        if len(occurrences[index]) > 2:
            ranges_to_remove.append([occurrences[index][0], occurrences[index][-1]])
        elif len(occurrences[index]) == 2:
            ranges_to_remove.append(occurrences[index])

    indexes_to_remove = []

    for index1 in ranges_to_remove:
        for index2 in ranges_to_remove:
            if index1[0] < index2[0] and index1[1] > index2[1]:
                indexes_to_remove.append(index2)

    ranges_to_remove = [x for x in ranges_to_remove if x not in indexes_to_remove]
    path.solution_path = path.real_path

    ranges_to_remove.sort(reverse=True, key=lambda indexes: indexes[0])

    for range_to_remove in ranges_to_remove:
        path.solution_path = path.solution_path[:range_to_remove[0]] + path.solution_path[range_to_remove[1]:]


