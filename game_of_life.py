import random
import os
import time

# Size of the grid (rows x cols)
ROWS = 20
COLS = 40
GENERATIONS = 50
SLEEP_TIME = 0.1  # Time between generations (in seconds)

def clear_screen():
    """Clears the terminal screen for better animation."""
    os.system('cls' if os.name == 'nt' else 'clear')

def create_grid(randomize=True):
    """Creates a 2D grid with dead (0) or alive (1) cells."""
    grid = []
    for _ in range(ROWS):
        row = []
        for _ in range(COLS):
            if randomize:
                cell = random.choice([0, 1])
            else:
                cell = 0
            row.append(cell)
        grid.append(row)
    return grid

def print_grid(grid, generation):
    """Prints the grid in a readable format."""
    print(f"Generation {generation}")
    for row in grid:
        line = ''
        for cell in row:
            line += '*' if cell == 1 else ' '
        print(line)

def count_neighbors(grid, row, col):
    """Counts alive neighbors around a given cell."""
    neighbors = 0
    for i in range(-1, 2):  # -1, 0, 1
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue  # Skip the cell itself
            r = (row + i) % ROWS
            c = (col + j) % COLS
            neighbors += grid[r][c]
    return neighbors

def next_generation(grid):
    """Calculates the next generation based on Game of Life rules."""
    new_grid = []
    for row in range(ROWS):
        new_row = []
        for col in range(COLS):
            alive = grid[row][col]
            neighbors = count_neighbors(grid, row, col)

            if alive == 1:
                # Rule 1 and 2
                if neighbors in [2, 3]:
                    new_row.append(1)
                else:
                    new_row.append(0)
            else:
                # Rule 3
                if neighbors == 3:
                    new_row.append(1)
                else:
                    new_row.append(0)
        new_grid.append(new_row)
    return new_grid

def run_simulation():
    """Main function to run the simulation."""
    grid = create_grid(randomize=True)
    for generation in range(1, GENERATIONS + 1):
        clear_screen()
        print_grid(grid, generation)
        grid = next_generation(grid)
        time.sleep(SLEEP_TIME)

if __name__ == "__main__":
    run_simulation()
