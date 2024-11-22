import copy
import random
#Ishika Agarwal 22BCE3179
class EightPuzzle:
    def __init__(self, initial_state):
        self.state = initial_state
        self.goal_state = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]
        ]
    
    def manhattan_distance(self, state):
        #Calculate Manhattan distance heuristic.
        distance = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != 0:
                    goal_pos = self.find_goal_position(state[i][j])
                    distance += abs(i - goal_pos[0]) + abs(j - goal_pos[1])
        return distance
    
    def find_goal_position(self, num):
        #Find goal position for a given number.
        for i in range(3):
            for j in range(3):
                if self.goal_state[i][j] == num:
                    return (i, j)
    
    def get_blank_position(self, state):
      #Find position of blank (0) tile.
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return (i, j)
        return None
    
    def get_possible_moves(self, state):
        #Generate possible moves by moving blank tile.
        moves = []
        directions = [
            (0, 1),  # right
            (0, -1),  # left
            (1, 0),  # down
            (-1, 0)  # up
        ]
        
        blank_pos = self.get_blank_position(state)
        
        for dx, dy in directions:
            new_x, new_y = blank_pos[0] + dx, blank_pos[1] + dy
            
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_state = copy.deepcopy(state)
                # Swap blank with adjacent tile
                new_state[blank_pos[0]][blank_pos[1]], new_state[new_x][new_y] = \
                new_state[new_x][new_y], new_state[blank_pos[0]][blank_pos[1]]
                moves.append(new_state)
        
        return moves
    
    def hill_climbing(self, max_iterations=100):
        #Hill Climbing algorithm to solve 8 Puzzle.
        current_state = self.state
        iterations = 0
        
        while iterations < max_iterations:
            # Check if current state is goal state
            if current_state == self.goal_state:
                print(f"Solution found in {iterations} iterations!")
                return current_state
            
            # Get possible moves
            possible_moves = self.get_possible_moves(current_state)
            
            # Evaluate moves and find best neighbor
            best_move = None
            best_heuristic = self.manhattan_distance(current_state)
            
            for move in possible_moves:
                move_heuristic = self.manhattan_distance(move)
                
                # Hill Climbing: Choose move with lowest heuristic
                if move_heuristic < best_heuristic:
                    best_move = move
                    best_heuristic = move_heuristic
            
            # Check for local maxima/plateau
            if best_move is None or best_heuristic >= self.manhattan_distance(current_state):
                print(f"Local maximum or plateau reached after {iterations} iterations.")
                return None
            
            current_state = best_move
            iterations += 1
        
        print("Maximum iterations reached without finding solution.")
        return None
    
    def print_state(self, state):
        """Print puzzle state."""
        for row in state:
            print(row)
        print()

def get_user_input():
    #Get initial puzzle configuration from user.
    print("Enter the initial 8-Puzzle configuration:")
    print("Use numbers 0-8, with 0 representing the blank space")
    print("Enter each row with space-separated numbers")
    
    initial_state = []
    for i in range(3):
        while True:
            try:
                row = list(map(int, input(f"Enter row {i+1} (space-separated): ").split()))
                if len(row) != 3 or any(num < 0 or num > 8 for num in row) or len(set(row)) != len(row):
                    print("Invalid input. Ensure 3 unique numbers between 0-8.")
                    continue
                initial_state.append(row)
                break
            except ValueError:
                print("Invalid input. Use space-separated numbers.")
    
    return initial_state

def main():
    # Get user input for initial state
    initial_state = get_user_input()
    
    print("\nInitial State:")
    puzzle = EightPuzzle(initial_state)
    puzzle.print_state(initial_state)
    
    solution = puzzle.hill_climbing()
    
    if solution:
        print("Goal State:")
        puzzle.print_state(solution)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
