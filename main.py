import maze_creation as mc
import maze_solving as ms
import visualization as v
import maze

DIMENSION = 10

main_maze = maze.Maze(DIMENSION)
main_maze = mc.move_forward(main_maze)
path = ms.solve(main_maze)
#v.show_all(main_maze, path)
v.animate_solution(main_maze, path.short_path)
