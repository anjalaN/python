#!/usr/bin/env python3
from collections import deque

goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

def is_goal(state):
    return state == goal_state

def get_possible_moves(puzzle):
    index_of_zero = puzzle.index(0)
    row, col = divmod(index_of_zero, 3)
    possible_moves = []

    for move in moves:
        new_row, new_col = row + move[0], col + move[1]
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_puzzle = puzzle[:]
            new_puzzle[index_of_zero], new_puzzle[new_index] = new_puzzle[new_index], new_puzzle[index_of_zero]
            possible_moves.append(new_puzzle)

    return possible_moves

def bfs(start_state):
    if is_goal(start_state):
        return [start_state]
    
    queue = deque([(start_state, [])])  # Queue stores (state, path)
    visited = set()

    while queue:
        current_state, path = queue.popleft()

        if tuple(current_state) in visited:
            continue
        visited.add(tuple(current_state))

        # Print the current puzzle state at each step
        print("Current Puzzle State:")
        print_puzzle(current_state)

        for next_state in get_possible_moves(current_state):
            if is_goal(next_state):
                return path + [current_state, next_state]
            queue.append((next_state, path + [current_state]))

    return None  # If no solution is found

# Function to print the puzzle state
def print_puzzle(puzzle):
    for i in range(0, len(puzzle), 3):
        print(puzzle[i:i+3])
    print()

def main():
    initial_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]  # Example starting state
    print("Initial Puzzle:")
    print_puzzle(initial_state)
    
    solution = bfs(initial_state)

    if solution is None:
        print("The puzzle is unsolvable.")
    else:
        print("Solution found:")
        for step in solution:
            print_puzzle(step)

if __name__ == "__main__":
    main()




































































