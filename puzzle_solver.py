#!/usr/bin/env python3

from collections import deque

# Goal state for the 8-puzzle
GOAL_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Function to flatten a 2D grid into a 1D list
def flatten(grid):
    return [tile for row in grid for tile in row]

# Function to count inversions
def count_inversions(grid):
    flattened = flatten(grid)
    flattened = [x for x in flattened if x != 0]  # Remove the empty space
    inversions = 0
    for i in range(len(flattened)):
        for j in range(i + 1, len(flattened)):
            if flattened[i] > flattened[j]:
                inversions += 1
    return inversions

# Function to check if the puzzle is solvable
def is_solvable(grid):
    inversions = count_inversions(grid)
    return inversions % 2 == 0

# Function to find the position of '0' in the grid
def find_empty(grid):
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                return i, j

# Function to generate all possible moves
def get_neighbors(grid):
    moves = []
    x, y = find_empty(grid)
    directions = [("UP", -1, 0), ("DOWN", 1, 0), ("LEFT", 0, -1), ("RIGHT", 0, 1)]
    
    for direction, dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            # Swap the tiles to generate a new state
            new_grid = [row[:] for row in grid]
            new_grid[x][y], new_grid[new_x][new_y] = new_grid[new_x][new_y], new_grid[x][y]
            moves.append((new_grid, direction))
    return moves

# BFS Algorithm to solve the puzzle
def solve_puzzle(grid):
    visited = set()
    queue = deque([(grid, [])])  # (current state, path of moves)

    while queue:
        state, path = queue.popleft()
        
        if state == GOAL_STATE:
            return path  # Return the solution path
        
        state_tuple = tuple(flatten(state))
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        for neighbor, direction in get_neighbors(state):
            queue.append((neighbor, path + [direction]))
    return None  # No solution found

# Function to display a grid
def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))
    print()

# Main function
def main():
    # Example initial state
    initial_state = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
    
    print("Initial state of the puzzle:")
    print_grid(initial_state)
    
    if not is_solvable(initial_state):
        print("Puzzle is unsolvable")
        return

    print("Solving the puzzle...")
    solution = solve_puzzle(initial_state)
    
    if solution:
        print(f"Solution found in {len(solution)} steps.")
        current_state = initial_state
        for i, move in enumerate(solution, start=1):
            print(f"Step {i}: {move}")
            for neighbor, direction in get_neighbors(current_state):
                if direction == move:
                    current_state = neighbor
                    break
            print_grid(current_state)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()
