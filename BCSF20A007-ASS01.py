import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# xg: the X position of the light of power
# yg: the Y position of the light of power
# x: Thor's starting X position
# y: Thor's starting Y position
xg, yg, x, y = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns 
    #Thor can move. Do not remove this line.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    
    if(x>xg and y>yg):
        x-=1
        y-=1
        print("NW")
    elif(x>xg and y<yg):
        x-=1
        y+=1
        print("SW")
    elif(x>xg and y==yg):
        x-=1
        print("W")
    elif(x<xg and y>yg):
        y-=1
        x+=1
        print("NE")
    elif(x<xg and y<yg):
        x+=1
        y+=1
        print("SE")
    elif(x<xg and y==yg):
        x+=1
        print("E")
    elif(x==xg and y>yg):
        y-=1        
        print("N")
    elif(x==xg and y<yg):
        y+=1
        print("S")
    # A single line providing the move to be made: N NE E SE S SW W or NW
    