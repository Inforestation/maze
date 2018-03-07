import matplotlib.pyplot as plt
import numpy as np
from maze import UP, RIGHT
from matplotlib import animation


def add_paths(maze, ax, path):
    x, y = zip(*(path))
    ax.plot(x, y, color='green', lw=1.5)
    return ax


def add_maze(maze, ax):  # creates a visualization of a maze based on the set path
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


def show_all(maze, path):
    figure, ax = plt.subplots(nrows=1)
    add_paths(maze, ax, path)
    add_maze(maze, ax)
    add_start_and_stop(maze, ax)
    ax.set_ylim([-1.5, maze.dimension + 0.5])
    ax.set_xlim([-1.5, maze.dimension + 0.5])
    ax.set_aspect('equal')
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.set_yticks([])
    ax.set_xticks([])
    plt.show()


def add_start_and_stop(maze, ax):  # adds indication of starting and finishing points
    start_point = (0, 0)
    end_point = (maze.dimension - 1, maze.dimension - 1)
    ax.scatter(start_point[0], start_point[1], color='b', lw=2)
    ax.scatter(end_point[0], end_point[0], color='r', lw=2)
    return ax


def is_not_in_path(start_point, maze, direction):  # checks whether two points are in path (stack)
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


def animate_solution(maze, path):
    fig = plt.figure()
    ax = plt.axes(xlim=(-1.5, maze.dimension + 0.5), ylim=(-1.5, maze.dimension + 0.5))
    add_maze(maze, ax)

    ax.set_aspect('equal')
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.set_yticks([])
    ax.set_xticks([])
    add_start_and_stop(maze, ax)
    line, = ax.plot([], [], lw=2, color='green')

    def init():
        line.set_data([], [])
        return line,

    def animate(i):
        x, y = zip(*(path))
        line.set_data(x[:i+2], y[:i+2])
        return line,

    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=len(path)-1, interval=200, blit=False, repeat=False)
    plt.show()






