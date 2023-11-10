import random

# ANSI escape codes for colors
START_COLOR = '\033[1;33m'  # Yellow
END_COLOR = '\033[1;35m'    # Magenta
WALL_COLOR = '\033[1;31m'   # Red
OPEN_SPACE_COLOR = '\033[1;34m'  # Blue
PATH_COLOR = '\033[1;32m'   # Green
RESET_COLOR = '\033[0m'

def generate_maze(n):
    maze = [[f'{OPEN_SPACE_COLOR}◌{RESET_COLOR}' for _ in range(n)] for _ in range(n)]

    # Mark top-left corner as start (S)
    maze[0][0] = f'{START_COLOR}S{RESET_COLOR}'

    # Mark bottom-right corner as end (E)
    maze[n - 1][n - 1] = f'{END_COLOR}E{RESET_COLOR}'

    # Generate random walls
    for _ in range(int(0.25 * n * n)):
        i, j = random.randint(0, n - 1), random.randint(0, n - 1)
        while maze[i][j] != f'{OPEN_SPACE_COLOR}◌{RESET_COLOR}' or (i, j) == (0, 0) or (i, j) == (n - 1, n - 1):
            i, j = random.randint(0, n - 1), random.randint(0, n - 1)
        maze[i][j] = f'{WALL_COLOR}▓{RESET_COLOR}'

    return maze

def print_maze(maze):
    for row in maze:
        for cell in row:
            print(cell, end=' ')
        print()

def find_path(maze, current, end, visited):
    if current == end:
        return [current]

    visited.add(current)

    neighbors = get_neighbors(maze, current)

    for neighbor in neighbors:
        if neighbor not in visited and maze[neighbor[0]][neighbor[1]] == f'{OPEN_SPACE_COLOR}◌{RESET_COLOR}':
            path = find_path(maze, neighbor, end, visited.copy())
            if path:
                return [current] + path

    return []

def get_neighbors(maze, cell):
    neighbors = []

    # Check the neighbor above
    if cell[0] - 1 >= 0:
        neighbors.append((cell[0] - 1, cell[1]))

    # Check the neighbor below
    if cell[0] + 1 < len(maze):
        neighbors.append((cell[0] + 1, cell[1]))

    # Check the neighbor to the left
    if cell[1] - 1 >= 0:
        neighbors.append((cell[0], cell[1] - 1))

    # Check the neighbor to the right
    if cell[1] + 1 < len(maze[0]):
        neighbors.append((cell[0], cell[1] + 1))

    return neighbors

def mark_path(maze, path):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if (i, j) in path:
                maze[i][j] = f'{PATH_COLOR}◍{RESET_COLOR}'

def print_path_in_maze(maze):
    for row in maze:
        for cell in row:
            print(cell, end=' ')
        print()

def main():
    while True:
        n = int(input("Enter the maze size (n * n): "))
        maze = generate_maze(n)
        start = (0, 0)
        end = (n - 1, n - 1)
        visited = set()
        path = find_path(maze, start, end, visited)

        print("\nStart (S) and End (E)")
        print(f"Walls: {WALL_COLOR}▓{RESET_COLOR} (red)")
        print(f"Open Space {OPEN_SPACE_COLOR}◌{RESET_COLOR} (Blue)")
        print(f"Path {PATH_COLOR}◍{RESET_COLOR} (Green)")
        print_maze(maze)

        if path:
            mark_path(maze, path)
            print("\nMaze with Marked Path (Solid Circle):")
            print_path_in_maze(maze)
        else:
            print("\nNo Path Found.")

        action = input("\n1. Generate another puzzle\n2. Exit game\nPlease enter your choice: ")

        if action == '2':
            print("Exiting the Maze Solver.")
            break

if __name__ == "__main__":
    main()
