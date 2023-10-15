import math
from queue import PriorityQueue

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


            ## Task 01 Done Task 2 Started

class Node:
    def __init__(self, initial_state, cost, action, heuristic, zeroindex, parent):
        self.initial_state = initial_state  # this is the list of the input
        self.parent = parent
        self.action = action  # UP , DOWN , LEFT , RIGHT
        self.cost = cost
        self.zeroindex = zeroindex
        self.heuristic = heuristic
        self.priority = cost + heuristic


def Goal_Test(state, goal):
    if state == goal:
        return True
    else:
        return False


class Problem:  # defining a well define problem
    def __init__(self, ini_list, goal_state):
        self.ini_list = ini_list
        self.goal_state = goal_state


def heuristic(state,
              goal_state):  # this function will give us the value that show how much our goal look alike our current state
    count = 0
    for i in range(len(state)):
        if state[i] != goal_state[i]:
            count += 1
    return count


def swap(lst, index1, index2):
    # Create a copy of the original list
    new_lst = lst.copy()

    # Swap the values at the specified indices
    new_lst[index1], new_lst[index2] = new_lst[index2], new_lst[index1]

    return new_lst


def check(state1, state2):
    for i in range(len(state1)):
        if state1[i] != state2[i]:
            return False
    return True


def solution(node):
    actions = []
    while node.parent is not None:
        actions.append(node.action)
        node = node.parent

    actions.reverse()
    return actions


def A_Star(p):
    length = len(p.ini_list)

    dim = math.sqrt(length)  # this will show us the dimension of the 2d array from row major
    frontier = PriorityQueue()

    h = heuristic(p.ini_list, p.goal_state)
    if h == 0:
        print(" we are already at the goal state \n ")
        return
    zindex = int(p.ini_list.index(0))
    n = Node(p.ini_list, 0, None, h, zindex, None)
    frontier.put((n.priority, n))
    explored = []  # we only put state in it
    action_list = []
    while not frontier.empty():
        priority, n = frontier.get()  # we get node, on the base of the priority

        flag = Goal_Test(n.initial_state, p.goal_state)
        if flag:
            print(" Goal Found \n ")
            action_list = solution(n)
            return
        explored.append(n.initial_state)
        val = 0
        index = int(p.ini_list.index(val))
        row = index // dim
        col = index % dim
        if row - 1 >= 0:
            # we can move upward action name is 1
            ind = int(row - dim)  # this is the index at where we have to put zero it's not a zero index
            # create a separate state for this
            # swapping the values with the index
            # initial_state, cost, action, heuristic, zeroindex, parent):

            nlist = swap(n.initial_state, int(n.zeroindex), ind)
            h = heuristic(nlist, p.goal_state)
            index = int(nlist.index(0))
            child = Node(nlist, n.cost + 1, "UP", h, index,
                         n)  # the priority value will be set in the constructor  on the bases of cost and heuristic value

            found = False
            matched_node = None
            for existing_node in frontier.queue:
                if child.initial_state == existing_node.initial_state:
                    found = True
                    matched_node = existing_node
                    break

            if not found:
                frontier.put((child.priority, child))
            else:
                if child.priority < matched_node.priority:
                    frontier.queue.remove(matched_node)
                    frontier.put((child.priority, child))
                else:
                    pass  # do nothing

        if row + 1 < dim:
            # we can move to down we name this action as 10
            ind = int(row + dim)  # ye wo index hai jis k sath hme swapping krni hai

            nlist = swap(n.initial_state, int(n.zeroindex), ind)
            h = heuristic(nlist, p.goal_state)
            index = int(nlist.index(0))
            child = Node(nlist, n.cost + 1, "DOWN", h, index, n)
            found = False
            matched_node = None
            for existing_node in frontier.queue:
                if child.initial_state == existing_node[1].initial_state:
                    found = True
                    matched_node = existing_node
                    break

            if not found:
                frontier.put((child.priority, child))
            else:
                if child.priority < matched_node.priority:
                    frontier.queue.remove(matched_node)
                    frontier.put((child.priority, child))
                else:
                    pass  # do nothing

        if col + 1 < dim:
            # move to the right we name this action as a 2
            ind = int(col + 1)  # ye wo index hai jis k sath hme swapping krni hai

            nlist = swap(n.initial_state, int(n.zeroindex), ind)
            h = heuristic(nlist, p.goal_state)
            index = int(nlist.index(0))
            child = Node(nlist, n.cost + 1, "RIGHT", h, index, n)

            found = False
            matched_node = None
            for existing_node in frontier.queue:
                if child.initial_state == existing_node[1].initial_state:
                    found = True
                    matched_node = existing_node
                    break

            if not found:
                frontier.put((child.priority, child))
            else:
                if child.priority < matched_node.priority:
                    frontier.queue.remove(matched_node)
                    frontier.put((child.priority, child))
                else:
                    pass  # do nothing

        if col - 1 >= 0:
            # move to the Left and we name this action as 20
            ind = int(col - 1)
            nlist = swap(n.initial_state, int(n.zeroindex), ind)
            h = heuristic(nlist, p.goal_state)
            index = int(nlist.index(0))
            child = Node(nlist, n.cost + 1, "LEFT", h, index, n)

            found = False
            matched_node = None
            for existing_node in frontier.queue:
                if child.initial_state == existing_node[1].initial_state:
                    found = True
                    matched_node = existing_node
                    break

            if not found:
                frontier.put((child.priority, child))
            else:
                if child.priority < matched_node.priority:
                    frontier.queue.remove(matched_node)
                    frontier.put((child.priority, child))
                else:
                    pass  # do nothing

            # if child not in frontier_q and child.index not in explored_q:
            #     if p.GOAL_TEST(goal1):
            #         print("Our Goal Found \n ")
            #         # sol_list = solution(child)
            #         # sol_list.append(child.index)
            #         action_list = action(child)
            #         action_list.reverse()
            #
            #         print("\t or In the form of Array are : ")
            #         action_list.remove(0)
            #         print("\t ", action_list)
            #         print()
            #         return True
            #     else:
            #         frontier_q.append(child)
    return n


### =============## Main Function======================= ##

goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
p = Problem(case2, goal)
A_Star(p)
