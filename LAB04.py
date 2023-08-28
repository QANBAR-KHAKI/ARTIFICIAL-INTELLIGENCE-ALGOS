import math

with open("file.txt") as f:
    cases = f.readline()
    case1 = f.readline()
    case2 = f.readline()
    case3 = f.readline()

print(cases, case1, case2, case3)

length = len(case1)
dim = math.sqrt(length)  # this will show us the dimension of the 2d array from row major
print(dim)
print(case1)
print("-------------")


# int_array = [int(x) for x in case1.split()]
# Converting the string list into int list
# goal1 = [1,2,3,0]
# goal2=[1,2,3,4,5,6,7,8,0]
# goal3=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]

def action(child):
    action_list = []
    while child is not None:
        action_list.append(child.action)
        child = child.parent
    return action_list


def swap(lst, index1, index2):
    # Create a copy of the original list
    new_lst = lst.copy()

    # Swap the values at the specified indices
    new_lst[index1], new_lst[index2] = new_lst[index2], new_lst[index1]

    return new_lst


class Problem:  # defining a well define problem
    def __init__(self, ini_list, goal):
        self.ini_list = ini_list
        self.goal = goal

    def GOAL_TEST(self, g1):
        if self.goal == g1:
            return 1
        else:
            return 0


'''def solution(child):
    if child is not None:
        par = child.parent
    else:
        print("The child can never be Null \n ")
        return -1

    sol_list = []
    actions = []

    while par is not None:
        sol_list.append(par)
        # actions.append(par.action)
        par = par.parent
    sol_list.reverse()
    # actions.reverse()
    return sol_list  # , actions
'''
class Node():
    def __init__(self, lst, index, parent, action):
        self.lst = lst
        self.parent = parent
        self.action = int(action)  # 0,1,2,3
        self.index = index


# ==========================================================================
frontier_q = []  # we can push and pop in it
explored_q = []


def problem(p):
    l = len(p.ini_list)
    dimension = math.sqrt(l)  # this will show us the dimension of the 2d array from row major
    print(dimension)

    # start a code from here
    val = 0
    index = int(p.ini_list.index(val))

    n = Node(p.ini_list, index, None, -1)
    frontier_q.append(n)  # put the index where it is zero
    while True:
        if frontier_q is None:
            print("The Failure happen as Queue can never be empty\n")
            return 0
        nod = frontier_q.pop()
        explored_q.append(nod.index)
        row = nod.index // dim
        col = nod.index % 3
        # index = int(case.index("0"))
        index = nod.index
        # Node class lst,zindex, parent, action)

        if row - 1 >= 0:
            # we can move upward
            ind = int(row - dim)
            # create a separate state for this
            # swapping the values with the index

            nlist = swap(nod.lst, int(nod.index), ind)
            child = Node(nlist, ind, nod.index, 0)
            if child not in frontier_q and child.index not in explored_q:
                if p.GOAL_TEST(goal1):
                    print("Our Goal Found \n ")
                    # sol_list = solution(child)
                    # sol_list.append(child.index)
                    action_list = action(child)
                    action_list.reverse()

                    print("\t or In the form of Array are : ")
                    action_list.remove(0)
                    print("\t ", action_list)
                    print()
                    return True

                else:
                    frontier_q.append(child)

        if row + 1 < dim:
            # we can move to down
            ind = int(row + dim)
            nlist = swap(nod.lst, int(nod.index), ind)
            child = Node(nlist, ind, nod.index, 1)
            if child not in frontier_q and child.index not in explored_q:
                if p.GOAL_TEST(goal1):
                    print("Our Goal Found \n ")
                    # sol_list = solution(child)
                    # sol_list.append(child.index)
                    action_list = action(child)
                    action_list.reverse()

                    print("\t or In the form of Array are : ")
                    action_list.remove(0)
                    print("\t ", action_list)
                    print()
                    return True
                else:
                    frontier_q.append(child)
        if col + 1 < dim:
            # move to the right
            ind = int(col + 1)
            nlist = swap(nod.lst, int(nod.index), ind)
            child = Node(nlist, ind, nod.index, 2)
            if child not in frontier_q and child.index not in explored_q:
                if p.GOAL_TEST(goal1):
                    print("Our Goal Found \n ")
                    # sol_list = solution(child)
                    # sol_list.append(child.index)
                    action_list = action(child)
                    action_list.reverse()

                    print("\t or In the form of Array are : ")
                    action_list.remove(0)
                    print("\t ", action_list)
                    print()
                    return True
                else:
                    frontier_q.append(child)
        if col - 1 >= 0:
            # move to the Left
            ind = int(col - 1)
            nlist = swap(nod.lst, int(nod.index), ind)
            child = Node(nlist, ind, nod.index, 3)
            if child not in frontier_q and child.index not in explored_q:
                if p.GOAL_TEST(goal1):
                    print("Our Goal Found \n ")
                    #sol_list = solution(child)
                    #sol_list.append(child.index)
                    action_list = action(child)
                    action_list.reverse()

                    print("\t or In the form of Array are : ")
                    action_list.remove(0)
                    print("\t ", action_list)
                    print()
                    return True
                else:
                    frontier_q.append(child)

    return


int_array1 = [int(x) for x in case1.split()]
int_array2 = [int(x) for x in case2.split()]
int_array3 = [int(x) for x in case3.split()]
goal1 = [1, 2, 3, 0]
goal2 = [1, 2, 3, 4, 5, 6, 7, 8, 0]
goal3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
lst = [0, 2,1,3]
p = Problem(lst, goal1)
problem(p)



                                     # A STAR COMMENTED CODE

# import math
# import queue
# from queue import PriorityQueue
#
# from pkg_resources._vendor.pyparsing import empty
#
#
# class Problem:  # defining a well define problem
#     def __init__(self, ini_list, goal):
#         self.ini_list = ini_list
#         self.goal = goal
#
#
# def swap(lst, index1, index2):
#     # Create a copy of the original list
#     new_lst = lst.copy()
#
#     # Swap the values at the specified indices
#     new_lst[index1], new_lst[index2] = new_lst[index2], new_lst[index1]
#
#     return new_lst
#
#
# class Node():
#     def __init__(self, state_list, action, goN, hoN, foN, parent):
#         self.state_list = state_list
#         self.parent = parent
#
#         self.goN = goN
#         self.hoN = hoN
#         self.foN = foN
#         self.action = action
#
#
# # frontier = queue.PriorityQueue()
#
#
# def heuristic(state_list, goal, count=0):
#     for i in range(len(state_list)):
#         if state_list[i] == goal[i]:
#             count += 1
#
#     return count
#
#
# def A_star(p):
#     l = len(p.ini_list)
#     dim = math.sqrt(l)  # this will show us the dimension of the 2d array from row major
#     print(dim)
#
#     # start a code from here
#     val = 0
#     index = int(p.ini_list.index(val))  # will give us the index where 0 exist
#
#     # Node parameters          state_list,action, goN, hoN, foN, parent
#     node = Node(p.ini_list, None, 0, heuristic(p.ini_list, p.goal, 0), (0 + heuristic(p.ini_list, p.goal, 0)), None)
#     frontier = PriorityQueue()
#     frontier.put(heuristic(p.ini_list, p.goal, 0),node)
#     explored = []
#     while frontier is not empty:
#         nod = frontier.get()
#         explored.append(nod.index)
#         row = nod.index // dim
#         col = nod.index % 3
#
#         if row - 1 >= 0:
#             # we can move upward
#             ind = int(row - dim)
#             # create a separate state for this
#             # swapping the values with the index
#
#             nlist = swap(nod.lst, int(nod.index), ind)
#             child = Node(nlist, ind, nod.index, 0)
#             if child not in frontier and child.index not in explored:
#                 if p.GOAL_TEST(p.goal):
#                     print("Our Goal Found \n ")
#                     # sol_list = solution(child)
#                     # sol_list.append(child.index)
#                     action_list = action(child)
#                     action_list.reverse()
#
#                     print("\t or In the form of Array are : ")
#                     action_list.remove(0)
#                     print("\t ", action_list)
#                     print()
#                     return True
#
#                 else:
#                     frontier_q.append(child)
#
#         if row + 1 < dim:
#             # we can move to down
#             ind = int(row + dim)
#             nlist = swap(nod.lst, int(nod.index), ind)
#             child = Node(nlist, ind, nod.index, 1)
#             if child not in frontier_q and child.index not in explored_q:
#                 if p.GOAL_TEST(goal1):
#                     print("Our Goal Found \n ")
#                     # sol_list = solution(child)
#                     # sol_list.append(child.index)
#                     action_list = action(child)
#                     action_list.reverse()
#
#                     print("\t or In the form of Array are : ")
#                     action_list.remove(0)
#                     print("\t ", action_list)
#                     print()
#                     return True
#                 else:
#                     frontier_q.append(child)
#         if col + 1 < dim:
#             # move to the right
#             ind = int(col + 1)
#             nlist = swap(nod.lst, int(nod.index), ind)
#             child = Node(nlist, ind, nod.index, 2)
#             if child not in frontier_q and child.index not in explored_q:
#                 if p.GOAL_TEST(goal1):
#                     print("Our Goal Found \n ")
#                     # sol_list = solution(child)
#                     # sol_list.append(child.index)
#                     action_list = action(child)
#                     action_list.reverse()
#
#                     print("\t or In the form of Array are : ")
#                     action_list.remove(0)
#                     print("\t ", action_list)
#                     print()
#                     return True
#                 else:
#                     frontier_q.append(child)
#         if col - 1 >= 0:
#             # move to the Left
#             ind = int(col - 1)
#             nlist = swap(nod.lst, int(nod.index), ind)
#             child = Node(nlist, ind, nod.index, 3)
#             if child not in frontier and child.index not in explored_q:
#                 if p.GOAL_TEST(goal1):
#                     print("Our Goal Found \n ")
#                     # sol_list = solution(child)
#                     # sol_list.append(child.index)
#                     action_list = action(child)
#                     action_list.reverse()
#
#                     print("\t or In the form of Array are : ")
#                     action_list.remove(0)
#                     print("\t ", action_list)
#                     print()
#                     return True
#                 else:
#                     frontier.append(child)
