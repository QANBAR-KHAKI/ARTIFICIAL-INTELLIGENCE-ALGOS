import math
from queue import PriorityQueue


def IsSolvable(input_list):
    count = 0
    size = len(input_list)
    for i in range(size):
        for j in range(i + 1, size):
            if input_list[i] > input_list[j]:
                count += 1

    dim = math.sqrt(size)
    if (count % 2 == 0 and size % 2 != 0) or (count % 2 != 0 and size % 2 == 0):
        return True
    else:
        return False


# with open("problems.txt") as f:
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
print(c1,c2,c3,c4)


# example_count = f.readline()
# example_count = int(example_count)
# example_set = []
# for i in range(example_count):
#     # example = list(map(int, f.readline().split('')))
#     example = list(map(int,f.readline().split()))
#
#     example_set.append(example)
# Now we want to create a goal state
# goal_list = []
# for example in example_set:
#     size = len(example)
#     goal = []
#     for j in range(size):
#         print(int(j+1)+2)
#         goal[j] = int(j + 1)
#     goal[size] = 0
#     goal_list.append(goal)
#

def problem_Status(input_list):
    flag = IsSolvable(input_list)
    if flag:
        print("This Problem is solvable ")
        return True
    else:
        print(" This Problem Statement is not Solvable \n ")
        return False


#
# # Define the goal state
# goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]  # 0 represents the empty tile
#
# Define the initial state
initial_state = [1, 2, 3, 4, 5, 0, 7, 8, 6]
print(" Problem Status \n ")
problem_Status(initial_state)


# Define the heuristic function (Misplaced Tiles)
def heuristic(state):
    count = 0
    for i in range(len(state)):
        if state[i] != goal_state[i]:
            count += 1
    return count


# Define the A* search algorithm
def a_star_search(initial_state, goal_state):
    length = len(initial_state)
    dim = math.sqrt(length)  # this will show us the dimension of the 2d array from row major
    queue = PriorityQueue()
    queue.put((0, initial_state, []))  # (priority, state, moves)
    visited = set()
    visited.add(tuple(initial_state))

    while not queue.empty():
        cost, current_state, moves = queue.get()

        if current_state == goal_state:
            return moves

        # Find the index of the empty tile (0)
        empty_tile_index = current_state.index(0)
        print("Zero state Index is : ", empty_tile_index)

        # Generate all possible next states by moving the empty tile
        for move in get_possible_moves(empty_tile_index, dim):
            next_state = current_state[:]
            next_state[empty_tile_index], next_state[move] = next_state[move], next_state[empty_tile_index]  # swapping here bro

            # Check if the next state has not been visited before
            if tuple(next_state) not in visited:
                visited.add(tuple(next_state))
                priority = cost + 1 + heuristic(next_state)
                next_moves = moves + [move]
                queue.put((priority, next_state, next_moves))

    return None  # If no solution is found


# Define the possible moves based on the current index of the empty tile
# def get_possible_moves(empty_tile_index, dim):
#     possible_moves = []
#
#     row = empty_tile_index // dim
#     col = empty_tile_index % 3
#
#     if empty_tile_index >= 3:
#         possible_moves.append(empty_tile_index - 3)  # Move Up
#
#     if empty_tile_index <= 5:
#         possible_moves.append(empty_tile_index + 3)  # Move Down
#
#     if empty_tile_index % 3 != 0:
#         possible_moves.append(empty_tile_index - 1)  # Move Left
#
#     if (empty_tile_index + 1) % 3 != 0:
#         possible_moves.append(empty_tile_index + 1)  # Move Right
#
#     return possible_moves

def get_possible_moves(empty_tile_index,dim):
    possible_moves = []

    rows = empty_tile_index // dim
    cols = empty_tile_index % dim
    print("THE SIZE OF ROW AND COLUMNS ARE : ",rows, cols)

    if empty_tile_index >= dim:
        possible_moves.append(empty_tile_index - dim)  # Move Up

    if empty_tile_index < (rows - 1) * dim:
        possible_moves.append(empty_tile_index + dim)  # Move Down

    if empty_tile_index % dim != 0:
        possible_moves.append(empty_tile_index - 1)  # Move Left

    if (empty_tile_index + 1) % dim != 0:
        possible_moves.append(empty_tile_index + 1)  # Move Right

    return possible_moves

# Run the A* search algorithm
# moves = a_star_search(initial_state, goal_state)


print(" \t \t  Main function \t \t ")
print(" Select a problem statement you want to run ")
print(
    " 1- 0 3 1 2 \n 2 - 0 3 2 1 6 4 8 7 5 \n 3 - 3 14 13 7 4 5 6 1 11 12 8 0 15 9 2 10 \n 4 - 4 8 7 5 0 3 2 1 6 \n 5 - 5 6 1 11 12 8 0 15 9 2 10 3 14 13 7 4")
choice = int(input("Enter your choice "))
if choice == 2:
    # flag = problem_Status(case2)
    # if flag == False:
    goal_state = []
    for i in range(c2):  # c1 is the length of the input list
        goal_state.append(i+1)
    goal_state[- 1] = 0
    moves = a_star_search(case2, goal_state)
    if moves is None:
        print("No solution found.")
    else:
        print("Sequence of moves to reach the goal:")
        for move in moves:
            if move == initial_state.index(0) - 1:
                print("Move Left")
            elif move == initial_state.index(0) + 1:
                print("Move Right")
            elif move == initial_state.index(0) - 3:
                print("Move Up")
            elif move == initial_state.index(0) + 3:
                print("Move Down")
            initial_state[initial_state.index(0)], initial_state[move] = initial_state[move], initial_state[
                initial_state.index(0)]
            print(initial_state)
