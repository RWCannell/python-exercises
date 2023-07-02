

def is_valid(maze, row, col):
    if row < 0 or row >= len(maze):
        return False
    if col < 0 or col >= len(maze):
        return False
    if maze[row][col] != 1:
        return False
    return True

def is_complete(maze, row, col):
    if row == len(maze) - 1 and col == len(maze) - 1:
        maze[row][col] = 1
        return True
    return False

def move(maze, row, col):
    if is_complete(maze, row, col):
        return True
    if is_valid(maze, row, col):
        maze[row][col] = 1

        # move to the right
        if move(maze, row, col + 1):
            return True
        
        # move downwards
        if move(maze, row + 1, col):
            return True
        
        maze[row][col] = 0
    return False

def solve_maze_problem(maze):
    if move(maze, 0, 0) == False:
        print("No solution")

    completed_maze = [["-" for i in range(len(maze))] for j in range(len(maze))]
    for i in range(len(maze)):
        for j in range(len(maze)):
            if maze[i][j] == 1:
                completed_maze[i][j] = "+"
            print(completed_maze[i][j], end=" ")
        print()

if __name__ == '__main__':
    maze = [[1, 1, 1, 1, 1], [0, 0, 1, 0, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1], [1, 1, 1, 0, 1]]
    solve_maze_problem(maze)