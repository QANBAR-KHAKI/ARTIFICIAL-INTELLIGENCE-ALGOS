import random
import math  #


# import random
#
#
# # Generate the initial state randomly
# def generate_initial_state():
#     initial_state = [random.randint(0, 7) for _ in range(8)]
#     print(" The Initial State is : ", initial_state)
#     return initial_state
#
#
# def generate_Queen(initial_state):  # here we made a Queen in the form of 2D matrix/ A  rray
#     # initial_state = generate_initial_state()
#     queen = [[]]
#     rows, cols = (8, 8)
#     queen = [[0] * cols for _ in range(rows)]  # Create a 2D array with separate lists for each row
#
#     # Example initial state, replace with your desired values
#
#     for i in range(8):
#         n = initial_state[i]
#         queen[i][n] = 1  # Place "1" at the desired position
#
#     # Print the resulting array
#     for row in queen:
#         print(row)
#     return queen
#
#
# # Calculate the number of conflicts (attacks) in the given state
# def calculate_conflicts(state):
#     conflicts = 0
#     for i in range(7):
#         for j in range(i + 1, 8):
#             if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
#                 conflicts += 1
#     return conflicts
#
#
# #
# #
# # Generate a neighboring state by moving a queen to minimize conflicts
# def generate_neighbor_state(state):
#     neighbor = list(state)
#     min_conflicts = calculate_conflicts(state)
#     print(min_conflicts)
#
#     for column in range(8):
#         if neighbor[column] != 0:
#             original_row = neighbor[column]
#             for row in range(8):
#                 if row != original_row:
#                     neighbor[column] = row
#                     conflicts = calculate_conflicts(neighbor)
#                     if conflicts < min_conflicts:
#                         min_conflicts = conflicts
#                         break
#                 neighbor[column] = original_row
#
#     return neighbor
#
#   ## MY OWN Made
# # def generate_neighbor_(matrix):
# #     state = convert_matrix_to_1d(matrix)
# #     conf = calculate_conflicts(state)
# #     neighbor = []
# #     conflicts =[]
# #     min_conflicts = calculate_conflicts(state)
# #     print(min_conflicts)
# #     for i in range(8):
# #         n = state[i]
# #         new_state = [row[:] for row in state]
# #         for col in range(8):        # we are generating the states in the row just changing the value of the list
# #             if new_state[i] != 1 and i != n:
# #                 new_state[i] = 1
# #                 n = calculate_conflicts(new_state)
# #                 if n < conf:
# #                     new_state.append(neighbor)
# #                     conflicts.append(n)
# #                     new_state = [row[:] for row in state] # here we make a copy of the next new state
# #
# #
#
#
# ## The AI Generated code is here : just for the sake of understanding
#
# def generate_neighbor(state):
#     rows, cols = len(state), len(state[0])
#     c_conflicts = calculate_conflicts(state)
#     new_state = [row[:] for row in state]  # Create a copy of the current state
#
#     # Find the row and column of the queen (value 1)
#     queen_row, queen_col = None, None
#     for row in range(rows):
#         for col in range(cols):
#             if state[row][col] == 1:
#                 queen_row, queen_col = row, col
#                 break
#
#     conflict_list = []
#     # Generate a new state by moving the queen to a neighboring column
#     for col in range(cols):
#         if col != queen_col:
#             new_state[queen_row][queen_col] = 0  # Remove the queen from the current column
#             new_state[queen_row][col] = 1  # Place the queen in the neighboring column
#             # calculate the conflict in that state
#             c = calculate_conflicts(new_state)
#             if c < c_conflicts:
#                 conflict_list.append(c)
#             else:
#                 pass
#             break  # Only generate one neighbor
#
#     return new_state
#
#
# #
# # # Solve the 8-Queens problem using Hill Climbing with 100 sideways moves
# def solve_8_queens_hill_climbing():
#     current_state = generate_initial_state()
#     current_conflicts = calculate_conflicts(current_state)
#     explored_states = [current_state]
#
#     while current_conflicts > 0:
#         sideways_moves = 0
#         while sideways_moves < 100:
#             neighbor_state = generate_neighbor_state(current_state)
#             neighbor_conflicts = calculate_conflicts(neighbor_state)
#
#             if neighbor_conflicts < current_conflicts:
#                 current_state = neighbor_state
#                 current_conflicts = neighbor_conflicts
#                 explored_states.append(current_state)
#                 sideways_moves = 0
#             else:
#                 sideways_moves += 1
#                 if sideways_moves == 100:
#                     break
#
#     return current_state, explored_states


#
# # Print the states explored by the solution
# def print_explored_states(explored_states):
#     for state in explored_states:
#         print(state)
#
#
# # # state = [1, 2, 3, 4, 5, 6, 7, 8,0]
# # # state.reverse()
#
# def convert_matrix_to_1d(matrix):  # we made this function in order to convert the 2d array into the list
#     rows, cols = len(matrix), len(matrix[0])
#     one_d_list = []
#     column_indices = []
#
#     for row in range(rows):
#         for col in range(cols):
#             if matrix[row][col] == 1:
#                 one_d_list.append((row, col))
#                 column_indices.append(col)
#
#     return column_indices
#
#
# # Run the 8-Queens problem solver
# # solution_state, explored_states = solve_8_queens_hill_climbing()
# # print_explored_states(explored_states)
# # print("Solution found:")
# # print(solution_state)
# # print(generate_initial_state())
# # print("The Number of the conflicts are : ",calculate_conflicts(state))
# initial_state = generate_initial_state()
# print("The total Number of the Conflicts are : ", calculate_conflicts(initial_state))
# matrix = generate_Queen(initial_state)
#
# lst = convert_matrix_to_1d(matrix)
# print(lst)
# solve_8_queens_hill_climbing()
# CODE:
class problem:
    def __init__(self):
        # self.initial=[3,2,8,5,4,1,7,6]
        # self.initial=[7, 6, 2, 3, 4, 1, 5, 8]
        #          5,6,7,4,5,6,7,6
        self.initial = []
        i = 0
        while i < 8:
            a = random.randint(1, 8)
            # if a not in self.initial:
            self.initial.append(a)
            i += 1


class Node:
    def __init__(self, state, parent, cost, action):
        self.state = state
        self.action = action
        self.parent = parent
        self.cost = cost


def makenode(state, parent=None, cost=None, action=None):
    if cost != None:
        cost += 1
        child = Node(state, parent, cost, action)
    else:
        child = Node(state, parent, 0, action)
    return child


def calculateScore(state):
    diagnol = []
    for i in range(len(state)):
        y = i
        x = state[i] - 1
        d = []
        while y < 7:
            y += 1
            d.append((x, y))
        y = i
        while y < 7 and x > 0:
            y += 1
            x -= 1
            d.append((x, y))
        y = i
        x = state[i] - 1
        while y < 7 and x < 7:
            x += 1
            y += 1
            d.append((x, y))
        diagnol.append(d)

    Score = []
    for indices in range(len(diagnol)):
        count = 0
        for j in range(indices + 1, len(state)):
            x = state[j] - 1
            y = j
            index = (x, j)
            if index in diagnol[indices]:
                count += 1
        Score.append(count)
    return 28 - sum(Score)


def makesuccesor(state):
    succesors = []
    for i in range(len(state)):
        for j in range(1, 9):
            s = state[:]
            if j != state[i]:
                s[i] = j
                succesors.append(s)
    return succesors


def HillClimbing(problem):
    iterations = 0
    current = makenode(problem.initial)
    count = 0
    max_Node = None
    while True:
        iterations += 1
        neighbour = makesuccesor(current.state)
        max = 0
        index = 0
        for x in neighbour:
            score = calculateScore(x)
            if score > max:
                max = score
                index = x
        if calculateScore(current.state) < max:
            current = makenode(index, current, current.cost)
            if max_Node == None:
                max_Node = current
            else:
                if calculateScore(current.state) > calculateScore(max_Node.state):
                    max_Node = current
        else:
            if count < 100:
                count += 1
                current = makenode(index, current, current.cost)
                if max_Node == None:
                    max_Node = current
                else:
                    if calculateScore(current.state) > calculateScore(max_Node.state):
                        max_Node = current
            else:
                # print(iterations)
                return max_Node
                # return current


def print_actions(Node):
    if Node.parent == None:
        print("You are at goal")
        print(Node.state)
        return
    Stack = []
    while Node.parent != None:
        Stack.append(Node)
        Node = Node.parent
    size = len(Stack)
    path = ""
    for i in range(size):
        x = Stack.pop()
        if (i == size - 1):
            print(x.state, calculateScore(x.state))
        else:
            print(x.state, calculateScore(x.state))
            print("          |          ")


p = problem()
# print("Parent score  is ",calculateScore(p.initial),"\t","Parent state is ",p.initial)
ans = HillClimbing(p)
# ans=simulated_anealing(p,somefunc)
# print(ans.state)
print("Child score is ", calculateScore(ans.state), "\t", "Child state is ", ans.state)
print("Path to reach ans is")
print_actions(ans)
lis = []
for i in range(8):
    l = []
    for j in range(8):
        if ans.state[i] - 1 == j:
            l.append('Q')
        else:
            l.append('_')
    lis.append(l)

for i in range(8):
    for j in range(8):
        print(lis[j][i], end=' ')
    print()
