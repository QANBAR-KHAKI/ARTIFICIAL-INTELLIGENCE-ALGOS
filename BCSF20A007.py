size = 0
grid = None
score = 0
arrows = 0
user_loc = (1, 1)


def is_valid_pos(pos, message):
    if 0 <= pos[0] < int(size) and 0 <= pos[1] < int(size):
        grid[pos[0]][pos[1]].append(message)


with open("environment.txt") as file:
    size = file.readline()
    grid = [[[] for i in range(int(size))] for j in range(int(size))]

    arrows = file.readline()

    line = file.readline()
    while line:
        line = line.split(" ")
        if line[0] == "p":
            grid[int(line[1]) - 1][int(line[2]) - 1].append("pit")
            position = [int(line[1]) - 1, int(line[2]) - 2]
            is_valid_pos(position, "breeze")
            position = [int(line[1]) - 2, int(line[2]) - 1]
            is_valid_pos(position, "breeze")
            position = [int(line[1]) - 1, int(line[2])]
            is_valid_pos(position, "breeze")
            position = [int(line[1]), int(line[2]) - 1]
            is_valid_pos(position, "breeze")
        elif line[0] == "w":
            grid[int(line[1]) - 1][int(line[2]) - 1].append("wumpus")
            position = [int(line[1]) - 1, int(line[2]) - 2]
            is_valid_pos(position, "strench")
            position = [int(line[1]) - 2, int(line[2]) - 1]
            is_valid_pos(position, "strench")
            position = [int(line[1]) - 1, int(line[2])]
            is_valid_pos(position, "strench")
            position = [int(line[1]), int(line[2]) - 1]
            is_valid_pos(position, "strench")
        elif line[0] == "g":
            grid[int(line[1]) - 1][int(line[2]) - 1].append("gold")

        line = file.readline()

for i in range(int(size)):
    print(grid[i])


def check_cell(grid, current_location, score, arrows):
    _exit = False
    if len(grid[current_location[0]][current_location[1]]) == 0:
        print("You are on safe cell")
        return _exit, arrows
    for thing in grid[current_location[0]][current_location[1]]:
        if thing == "wumpus":
            print("Entered in live wumpus!!!\nGame over...")
            _exit = True
            return _exit, arrows
    for thing in grid[current_location[0]][current_location[1]]:
        if thing == "gold":
            print("Gold found\nYou are Winner!!!")
            score += 150
            print(f"Cost to reach = {score}")
            _exit = True
            return _exit, arrows
    for thing in grid[current_location[0]][current_location[1]]:
        if thing == "pit":
            print("Entered in pit cell!!!\nGame over...")
            _exit = True
            return _exit, arrows
    print(f"{grid[current_location[0]][current_location[1]]} found in this cell!!!")
    if "strench" in grid[current_location[0]][current_location[1]]:
        choice = input("Want to shoot arrow (y/n)? ")
        if choice == 'y':
            direction = input("Enter direction to shoot (left/ right/ up/ down)? ")
            if arrows > 0:
                if direction == "left":
                    index = current_location[1]
                    while index >= 0:
                        if "wumpus" in grid[current_location[0]][index]:
                            grid[current_location[0]][index].remove("wumpus")
                            print("wumpus killed")
                            arrows -= 1
                            print(f"Remaining arrows: {arrows}")
                            score -= 10
                            return _exit, arrows
                        index -= 1

                if direction == "right":
                    index = current_location[1]
                    while index < int(size):
                        if "wumpus" in grid[current_location[0]][index]:
                            grid[current_location[0]][index].remove("wumpus")
                            print("wumpus killed")
                            arrows -= 1
                            print(f"Remaining arrows: {arrows}")
                            score -= 10
                            return _exit, arrows
                        index += 1

                if direction == "up":
                    index = current_location[0]
                    while index >= 0:
                        if "wumpus" in grid[index][current_location[1]]:
                            grid[index][current_location[1]].remove("wumpus")
                            print("wumpus killed")
                            arrows -= 1
                            print(f"Remaining arrows: {arrows}")
                            score -= 10
                            return _exit, arrows
                        index -= 1

                if direction == "down":
                    index = current_location[0]
                    while index < int(size):
                        if "wumpus" in grid[index][current_location[1]]:
                            grid[index][current_location[1]].remove("wumpus")
                            print("wumpus killed")
                            arrows -= 1
                            print(f"Remaining arrows: {arrows}")
                            score -= 10
                            return _exit, arrows
                        index += 1

                print("Failed to kill wumpus!!!")
                arrows -= 1
                print(f"Remaining arrows: {arrows}")
                score -= 10
            else:
                print("Can't shoot arrow")
                print(f"Remaining arrows: {arrows}")
    return _exit, arrows


def play(score, arrows):
    user_grid = [[' ' for i in range(int(size))] for j in range(int(size))]
    x, y = user_loc
    current_loc = [x - 1, y - 1]
    user_grid[current_loc[0]][current_loc[1]] = 'a'
    for i in range(int(size)):
        print(user_grid[i])
    print("You are on safe cell")
    next_action = input("Enter where you want to move next (left/ right/ up/ down)? ")
    while next_action != "left" and next_action != "right" and next_action != "up" and next_action != "down":
        print("Invalid input!\nPlease enter (left/ right/ up/ down)")
        next_action = input("Enter your input: ")

    while True:
        if next_action == "left":
            if 0 <= current_loc[1] - 1:
                user_grid[current_loc[0]][current_loc[1]] = ' '
                user_grid[current_loc[0]][current_loc[1] - 1] = 'a'
                current_loc = [current_loc[0], current_loc[1] - 1]
            else:
                print("bump")
                next_action = input("Enter your input: ")
                continue
        elif next_action == "right":
            if current_loc[1] + 1 < int(size):
                user_grid[current_loc[0]][current_loc[1]] = ' '
                user_grid[current_loc[0]][current_loc[1] + 1] = 'a'
                current_loc = [current_loc[0], current_loc[1] + 1]
            else:
                print("bump")
                next_action = input("Enter your input: ")
                continue
        elif next_action == "up":
            if 0 <= current_loc[0] - 1:
                user_grid[current_loc[0]][current_loc[1]] = ' '
                user_grid[current_loc[0] - 1][current_loc[1]] = 'a'
                current_loc = [current_loc[0] - 1, current_loc[1]]
            else:
                print("bump")
                next_action = input("Enter your input: ")
                continue
        elif next_action == "down":
            if current_loc[0] + 1 < int(size):
                user_grid[current_loc[0]][current_loc[1]] = ' '
                user_grid[current_loc[0] + 1][current_loc[1]] = 'a'
                current_loc = [current_loc[0] + 1, current_loc[1]]
            else:
                print("bump")
                next_action = input("Enter your input: ")
                continue
        else:
            print("Invalid input!\nPlease enter (left/ right/ up/ down)")
            next_action = input("Enter your input: ")
            continue

        for i in range(int(size)):
            print(user_grid[i])

        print(f"Moved to location {current_loc[0] + 1}, {current_loc[1] + 1}")
        score -= 1
        condition, arrows = check_cell(grid, current_loc, score, int(arrows))
        if condition:
            break

        next_action = input("Enter where you want to move next (left/ right/ up/ down)? ")


play(score, arrows)
