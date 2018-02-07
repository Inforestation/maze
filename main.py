import maze_creation_2 as mc
import maze_solving

DIMENSION = 10

maze = mc.Maze(DIMENSION)
maze = mc.move_forward(maze)
mc.show_all(maze)