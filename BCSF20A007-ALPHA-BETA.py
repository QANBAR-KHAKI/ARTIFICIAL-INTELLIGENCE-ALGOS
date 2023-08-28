# choice = int(input(
#     "Enter the index at where you want to put the TIK \n "))  # user enters the number at where he wants to tik  in the game
#      state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
# for i in range(9):
#     if choice == i + 1:
#         state[i] = 1


def board_display(state):
    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])


def action(state):
    action_list = []
    for i in range(9):
        if state[i] == 0:
            action_list.append(i)

    # the first above part is generating the index where the action can be performed 0 values

    ## -----   STATE  GENERATION -------- ##

    for i in range(len(state)):
        if i in action_list:
            new_state = state.copy()
            new_state[i] = -1
            total_states.append(new_state)

    # the loop iterate over the index and according to that actions index generating a states
    return total_states, action_list


def Max_value(state, alpha, beta):
    flag, value = terminal_test(state)
    if flag:
        return value
    else:
        v = float('-inf')  # negative infinity

        for states in total_states:
            v = max(v, Min_Value(states, alpha, beta))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v


def Min_Value(state, alpha, beta):
    flag, value = terminal_test(state)
    if flag:
        return value
    else:
        v = float('inf')  # positive infinity
        for states in total_states:
            v = min(v, Max_value(states, alpha, beta))
            if v >= beta:
                return v
            alpha = min(alpha, v)
        return v


def terminal_test(state):
    flag = False
    value = 0
    # state
    for i in range(len(state)):
        if state[i] == 0:

            for i in range(0, 3, 3):
                if state[i] == state[i + 1] and state[i] == state[i + 2]:
                    flag = True
                    return flag, state[i]

            # col
            for i in range(3):
                if state[i] == state[i + 3] and state[i] == state[i + 6]:
                    flag = True
                    return flag, state[i]

            # primary diagonal
            diagonal = 0
            if state[diagonal] == state[diagonal + 4] and state[diagonal] == state[diagonal + 8]:
                flag = True
                return flag, state[diagonal]

            # secondary diagonal
            diagonal = 2
            if state[diagonal] == state[diagonal + 2] and state[diagonal] == state[diagonal + 4]:
                flag = True
                return flag, state[diagonal]

            return flag, value

    # draw
    flag = True
    return flag, value


def alpha_beta(state):
    infinity = float('inf')
    neg_infinity = float('-inf')

    states_list, action_list = action(state)

    v = Max_value(state, neg_infinity, infinity)
    a2 = None
    for a in action_list:
        v2 = Max_value(state, neg_infinity, infinity)
        if v == v2:
            a2 = a
            break

    return a2

    # #### ========================  M A I N     F U N C T I O N  =============== #### # already merged with the action function
    # states_list = action(state)
    #
    # for states in states_list:
    #     board_display(states)
    #     print("----------")
    #
    # choice = int(input(
    #     "Enter the index at where you want to put the TIK \n "))  # user enters the number at where he wants to tik  in the game
    #      state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    # for i in range(9):
    #     if choice == i + 1:
    #         state[i] = 1
    #
    # #

total_states = []

state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
i = 1  # turn
while True:
    if 0 < i <= 9:

        if i % 2 == 0:  # even take will  be taken by the AI System
            print(" Player 1 (system) Turn \n ")
            print(" \t \t Current State \n ")
            board_display(state)
            print(" \t \t Possible Moves AI can perform \n ")
            states_list, action_list = action(state)
            for states in states_list:
                board_display(states)
                print("----------")

            best_move = alpha_beta(state)
            state[best_move] = 1

        else:  # odd Turn will be used by the User/ Human

            while True:
                print(" \t \t Current State \n ")
                board_display(state)
                choice = int(input("Enter the index where you want to place 'X': "))
                if state[choice] == 0:
                    state[choice] = -1
                    break
                else:
                    print("Illegal move! Try again.")
    else:
        print(" GAME IS OVER \n ")
    i = i + 1


# # Generate possible moves for AI
# total_states = action(state)
#
# # Choose the best move for AI
# best_move = alpha_beta(state)
# state[best_move[0]] = -1

# # =============================== M A I N  Function ENDS HERE ====================================#
