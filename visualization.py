import matplotlib.pyplot as plt
from maze import *
from matplotlib import animation


def add_paths(ax, path):
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
                    if maze.is_step_not_in_stack(start_point, direction):
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


def add_start_and_stop(maze, ax):  # adds indication of starting and finishing points
    start_point = (0, 0)
    end_point = (maze.dimension - 1, maze.dimension - 1)
    ax.scatter(start_point[0], start_point[1], color='b', lw=2, zorder=50)
    ax.scatter(end_point[0], end_point[0], color='b', lw=2, zorder=51)
    return ax


def set_ax(ax):
    ax.set_aspect('equal')
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.set_yticks([])
    ax.set_xticks([])


def show_all(maze, path):
    figure, ax = plt.subplots(nrows=1)
    add_paths(maze, ax, path)
    add_maze(maze, ax)
    add_start_and_stop(maze, ax)
    ax.set_ylim([-1.5, maze.dimension + 0.5])
    ax.set_xlim([-1.5, maze.dimension + 0.5])
    set_ax(ax)
    plt.show()


def animate_solution(maze, path):
    fig = plt.figure()
    ax = plt.axes(xlim=(-1.5, maze.dimension + 0.5), ylim=(-1.5, maze.dimension + 0.5))
    add_maze(maze, ax)
    set_ax(ax)
    add_start_and_stop(maze, ax)
    line, = ax.plot([], [], lw=2, color='green', zorder=2)
    line2, = ax.plot([], [], lw=4, color='red', zorder=1)
    dot = ax.scatter([], [], lw=0, s=40, c='black', zorder=3)

    def init():
        dot.set_offsets(([], []))
        line.set_data([], [])
        line2.set_data([], [])
        return line,

    def animate(i):
        x, y = zip(*(path.real_path))
        x2, y2 = zip(*(path.short_path))
        dot.set_offsets(([x[i + 1]], [y[i + 1]]))
        line.set_data(x[:i+2], y[:i+2])
        if i == len(path.real_path)-2:
            line2.set_data(x2, y2)
        return line, line2

    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=len(path.real_path)-1, interval=100, blit=False, repeat=False)
    plt.show()






