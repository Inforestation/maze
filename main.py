import maze_creation_2 as mc
import maze_solving
import maze

DIMENSION = 10

main_maze = maze.Maze(DIMENSION)
main_maze = mc.move_forward(main_maze)
mc.show_all(main_maze)