from queue import PriorityQueue


import math

with open("problems.txt") as f:
    cases = int(f.readline())
    case1 = list(map(int, f.readline().split()))
    case2 = list(map(int, f.readline().split()))
    case3 = list(map(int, f.readline().split()))
    case4 = list(map(int, f.readline().split()))

print(cases, case1, case2, case3)
c1 = len(case1)
c2 = len(case2)
c3 = len(case3)
c4 = len(case4)
print("The dimensions of the each example respectively  is : ", c1, c2, c3, c4)

def check_inversion(row):
    count=0
    size = int(math.sqrt(len(row)))
    print(size)
    row_size = size*size
    for i in range(row_size):
        for j in range(i+1,row_size):
            if(row[i]>row[j] and row[j] is not 0):
                count=count+1
    print(count)
    if((count%2==0 and row_size%2==1) or (count%2==1 and row_size%2==0)):
        return True
    else:
        return False

with open("problems.txt", "r") as file:
    n = int(file.readline().strip())
    #print(n)
    for i in range(n):
        row=list(map(int,file.readline().split()))
        #print(row)
        flag=check_inversion(row)
        if(flag):
            print("solvable")
        else:
            print("not solvable")

class Problem:  # defining a well define problem
    def __init__(self, ini_list, goal_state):
        self.ini_list = ini_list
        self.goal_state = goal_state



# Define the heuristic function (Misplaced Tiles)
def heuristic(state):
    count = 0
    for i in range(len(state)):
        if state[i] != goal_state[i]:
            count += 1
    return count

# Define the A* search algorithm
def a_star_search(initial_state, goal_state):
    queue = PriorityQueue()
    queue.put((0, initial_state, []))  # (priority, state, moves)
    visited = set()
    visited.add(tuple(initial_state))

    dim = int(len(initial_state) ** 0.5)  # Dimension of the 2D array

    while not queue.empty():
        cost, current_state, moves = queue.get()

        if current_state == goal_state:
            return moves

        # Find the index of the empty tile (0)
        empty_tile_index = current_state.index(0)

        # Generate all possible next states by moving the empty tile
        for move in get_possible_moves(empty_tile_index, dim):
            next_state = current_state[:]
            next_state[empty_tile_index], next_state[move] = next_state[move], next_state[empty_tile_index]

            # Check if the next state has not been visited before
            if tuple(next_state) not in visited:
                visited.add(tuple(next_state))
                priority = cost + 1 + heuristic(next_state)
                next_moves = moves + [move]
                queue.put((priority, next_state, next_moves))

    return None  # If no solution is found

# Define the possible moves based on the current index of the empty tile
def get_possible_moves(empty_tile_index, dim):
    possible_moves = []

    if empty_tile_index >= dim:
        possible_moves.append(empty_tile_index - dim)  # Move Up

    if empty_tile_index < (dim - 1) * dim:
        possible_moves.append(empty_tile_index + dim)  # Move Down

    if empty_tile_index % dim != 0:
        possible_moves.append(empty_tile_index - 1)  # Move Left

    if (empty_tile_index + 1) % dim != 0:
        possible_moves.append(empty_tile_index + 1)  # Move Right

    return possible_moves

# Run the A* search algorithm
moves = a_star_search(initial_state, goal_state)

if moves is None:
    print("No solution found.")
else:
    print("Sequence of moves to reach the goal:")
    for move in moves:
        if move == initial_state.index(0) - 1:
            print("Move Left")
        elif move == initial_state.index(0) + 1:
            print("Move Right")
        elif move == initial_state.index(0) - dim:
            print("Move Up")
        elif move == initial_state.index(0) + dim:
            print("Move Down")
        initial_state[initial_state.index(0)], initial_state[move] = initial_state[move], initial_state[initial_state.index(0)]
        print(initial_state)



goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
p = Problem(case2, goal)
A_Star(p)
