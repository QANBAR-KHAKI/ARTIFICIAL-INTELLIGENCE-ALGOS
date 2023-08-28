                            # GOAL BASE AGENT
goal_conditions = []
goal_actions = []
trans_matrix = []
test_cases = []

#===========================================================
 # this is function which return the index 
#===========================================================     
def getConditionNum(data):
    for i in range(len(goal_conditions)):
        if data == goal_conditions[i]:
            return i

    return -1


#===========================================================

# this is class for psuh of forntier and for back  tracking...

#===========================================================

class node:
    def __init__(self, condition, parent, action, cost):
        self.condition = condition
        self.parent = parent
        self.action = action
        self.cost = cost
#=============================================================
        
# in this part we get the filename from the text file which is provided

#==============================================================
name = input("Enter the file name:\n")
with open("input.txt", 'r') as file:
    
    #====== reading the first line for values of M N T=========
    data = file.readline()
    nums = data.split(" ")

        
    file.readline()

    #======== here we reading the goal_conditions==============
    for i in range(int(nums[0])):
        data = file.readline()
        goal_conditions.append(data.strip())

    file.readline()
    # =======reading goal_actions=================================
    for i in range(int(nums[1])):
        data = file.readline()
        goal_actions.append(data.strip())

    file.readline()
    # =========reading transition matrix==========================

    loop = int(nums[0])
    for i in range(loop):
        data = file.readline()
        data = data.split(" ")
        tmp = []
        for i in data:
            tmp.append(int(i))

        trans_matrix.append(tmp)
    
    file.readline()
    #========== reading testcases=================================
    for i in range(int(nums[2])):
        data = file.readline()
        data = data.split("\t")
        data[0] = data[0].strip()
        data[1] = data[1].strip()
        test_cases.append(data)
    

# ==============converting M N T to int for further use===========
val1 = int(nums[0])
val2 = int(nums[1])  # of actions
val3 = int(nums[2])

#====================================================================
# The main function of program , which gets initial and final state and prints result
# if no path is available it prints "No valid path is Available"
#====================================================================

def ShowResult(initialState, finalState):
    frontierQueue = []
    trackingStack = []
    exploredSet = []

    var = node(initialState, None, -1, 0)

    frontierQueue.append(var)
    exploredSet.append(initialState)

    while len(frontierQueue) > 0:
        current = frontierQueue.pop(0)
        
        if current.condition == finalState:
            temporary = current
            while temporary.parent is not None:
                trackingStack.append(temporary.action)
                temporary = temporary.parent

            string = ""
            if len(trackingStack) > 0:
                num = trackingStack.pop()
                string = goal_actions[num]
                while len(trackingStack) > 0:
                    num = trackingStack.pop()
                    string = string + "->" + goal_actions[num]
                
                print(string)

            return
        
        for i in range(val2):
            childCondition = trans_matrix[current.condition][i]

            if (childCondition) not in exploredSet:
                child = node(childCondition, current, i, current.cost + 1)
                frontierQueue.append(child)
                exploredSet.append(childCondition)

    print("No valid path is Available.")


#=================== calling result of all testcases=====================
print("\n----  The  OUTPUT is following  ----\n")
for i in range(val3):
    init_state = getConditionNum(test_cases[i][0])
    final_state = getConditionNum(test_cases[i][1])
    ShowResult(0, 7)

