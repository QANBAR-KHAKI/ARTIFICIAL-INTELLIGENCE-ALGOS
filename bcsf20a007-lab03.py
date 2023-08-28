# LAB 04
with open("input.txt") as f:
    line = f.readline()
    val = line.split(" ")
    no_states = int(val[0])
    no_actions = val[1]
    no_test_Case = val[2]
    emp = f.readline()
    description = []
    for i in range(no_states):
        data = f.readline()
        description.append(data.strip())
    f.readline()
    a1 = f.readline()  # 0     clean
    a2 = f.readline()  # 1     movetoRoom1
    a3 = f.readline()  # 2     movetoRoom2
    action_1 = 0
    action_2 = 1
    action_3 = 2

    f.readline()

    matrix = []
    for i in range(no_states):
        row = f.readline()
        row = row.rstrip('\n')  # remove the new Line from the Table
        trans_matrix_row = row.split(" ")
        matrix.append(trans_matrix_row)
    f.readline()

    test_cases = []
    for i in range(int(no_test_Case)):
        data = f.readline()
        data = data.split("\t")
        data[0] = data[0].strip()
        data[1] = data[1].strip()
        test_cases.append(data)


# print(test_cases)
# print("\t \t Matrix\n  ", matrix)
# print(no_states, no_actions, no_test_Case, description, "\n", a1, a2, a3)
# print(matrix)


# Writing from the file Finished here
#  ...................................................
class Problem:  # defining a well define problem
    def __init__(self, in_st, action, trans_model, goal, path_cost):
        self.in_st = in_st
        self.action = int(action)
        self.trans_model = trans_model
        self.goal = goal
        self.path_cost = path_cost

    def GOAL_TEST(self, node):
        if self.goal == node.state:
            return 1
        else:
            return 0


class node:
    def __init__(self, state, parent, action, cost):
        self.state = int(state)
        self.parent = parent
        self.action = int(action)  # 0,1,2
        self.cost = cost


# ==========================================================================
frontier_q = []  # we can push and pop in it
explored_q = []


#     def Actions(self):
#
sol = []  # for action in problem.action()


def solution(child):
    if child is not None:
        par = child.parent
    else:
        print("The child cna never be Null \n ")
        return -1

    sol_list = []
    actions = []

    while par is not None:
        sol_list.append(par.state)
        # actions.append(par.action)
        par = par.parent
    sol_list.reverse()
    # actions.reverse()
    return sol_list  # , actions

    # temporary = child
    # while temporary.parent is not None:
    #     sol_list.append(temporary.action)
    #     temporary = temporary.parent


def action(child):
    action_list = []
    while child is not None:
        action_list.append(child.action)
        child = child.parent
    return action_list


def BFS(problem):
    nod_i = node(problem.in_st,None , -1, problem.path_cost)
    # par = problem
    if problem.GOAL_TEST(nod_i):
        print("Our Goal is found ", nod_i.state)
        return 0
    else:
        #
        frontier_q.append(nod_i)
        

        while True:
            if frontier_q is None:
                print("The Failure happen as Queue can never be empty\n")
                return 0
            else:
                try:
                    nod = frontier_q.pop()
                    e = matrix[nod.state]
                    rw = len(e)
                    explored_q.append(nod.state)
                    for j in range(rw):
                        if e[j] != nod.state:
                            # index = matrix[j]
                            child_node = node(e[j], nod, j, nod.cost + 1)
                            if child_node not in frontier_q and child_node.state not in explored_q:
                                if problem.GOAL_TEST(child_node):
                                    print("\t  Our Goal Find \n")
                                    sol_list = solution(child_node)
                                    sol_list.append(child_node.state)

                                    print("\t ", sol_list)
                                    action_list = action(child_node)
                                    print("\n  \n \t Actions Performed \n \t  ")
                                    action_list.reverse()
                                    for i in action_list:
                                        if i==0:
                                            print(" Clean")
                                        elif i==1:
                                            print(" MoveToRoom1 ")
                                        elif i==2:
                                            print(" MoveToRoom2 ")
                                        else:
                                            print("")
                                    print("\t or In the form of Array are : ")
                                    action_list.remove(0)
                                    print("\t ", action_list)
                                    print()
                                    return True
                                else:
                                    frontier_q.append(child_node)

                except Exception as e:
                    print("We can't find  this path by Given data  \n ")
                    print(str(e))
                    return False
    return False



p = Problem(2, -1, matrix, 3, 0)
flg = BFS(p)
if flg:
    print("Successfully Run \n ")

