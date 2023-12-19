from math import ceil
from dataclasses import dataclass


input = open("input.txt")

# starting location (S)
x = 0
y = 0
x_s = 0
y_s = 0

map = []

@dataclass
class node:
    char: str
    on_path: bool = False
    counted: bool = False
    inside_direction: str = ""


def travel(direction, coming_from):
    curr_x = 0
    curr_y = 0
    if direction == "|":
        if coming_from == "u":
            curr_y += 1
        else: curr_y -= 1

    elif direction == "-":
        if coming_from == "l":
            curr_x += 1
        else:
            curr_x -= 1
    
    elif direction == "L":
        if coming_from == "u":
            coming_from = "l"
            curr_x += 1
        else:
            coming_from = "d"
            curr_y -= 1

    elif direction == "J":
        if coming_from == "u":
            coming_from = "r"
            curr_x -= 1
        else:
            coming_from = "d"
            curr_y -= 1
    
    elif direction == "7":
        if coming_from == "l":
            coming_from = "u"
            curr_y += 1
        else:
            coming_from = "r"
            curr_x -= 1
    
    elif direction == "F":
        if coming_from == "r":
            coming_from = "u"
            curr_y += 1
        else:
            coming_from = "l"
            curr_x += 1

    else:
        print("GOT ISSUES")

    return[curr_x, curr_y, coming_from]


def change_dir(direction, inside_dir):
    if direction == "|" or direction == "-":
        return inside_dir
    elif direction == "L":
        if inside_dir == "u":
            return "r"
        elif inside_dir == "d":
            return "l"
        elif inside_dir == "l":
            return "d"
        elif inside_dir == "r":
            # print("here")
            return "u"
        
    elif direction == "J":
        if inside_dir == "u":
            return "l"
        elif inside_dir == "d":
            return "r"
        elif inside_dir == "l":
            return "u"
        elif inside_dir == "r":
            return "d"
    
    elif direction == "7":
        if inside_dir == "u":
            return "r"
        elif inside_dir == "d":
            return "l"
        elif inside_dir == "l":
            return "d"
        elif inside_dir == "r":
            return "u"
        
    elif direction == "F":
        if inside_dir == "u":
            return "l"
        elif inside_dir == "d":
            return "r"
        elif inside_dir == "l":
            return "u"
        elif inside_dir == "r":
            return "d"
        
    else:
        print("ISUES")


while True:
    line = input.readline().strip()

    if not line:
        break

    # not using list comprehension to make finding S possible
    chars = []
    x = 0
    for char in line:
        if char == "S":
            x_s = x
            y_s = y
        chars.append(node(char=char))  # [character, on path, counted]


        x += 1

    map.append(chars)
    y += 1

width = len(map[0])
height = len(map)
# print(width, height)
map[y_s][x_s].on_path = True

# first set all paths
curr_x = x_s
curr_y = y_s + 1
coming_from = "u"  # u = up, l = left, r = right, d = down
while not (curr_x == x_s) or not (curr_y == y_s):
    map[curr_y][curr_x].on_path = True
    direction = map[curr_y][curr_x].char
    # print(direction)
    ret = travel(direction, coming_from)
    curr_x += ret[0]
    curr_y += ret[1]
    coming_from = ret[2]

count = 0
for y in range(height):
    parity = 0
    for x in range(width): 
        char = map[y][x].char
        if char in "|JLS":
            parity += 1
        
        # print(parity)
        if (parity % 2):
            if not map[y][x].on_path:
                count += 1
        # print(map[y][x].char,end="")
    # print()

print(count)
# map[y_s][x_s].inside_direction = "r"

# # loop over everything again, set inside direction
# curr_x = x_s
# curr_y = y_s + 1
# coming_from = "u"  # u = up, l = left, r = right, d = down
# inside_dir = "r"
# while not (curr_x == x_s) or not (curr_y == y_s):
#     direction = map[curr_y][curr_x].char

#     # print("at", curr_x, curr_y)
#     # print("direction", inside_dir)
#     inside_dir = change_dir(direction, inside_dir)
#     # print("new direction", inside_dir)
#     map[curr_y][curr_x].inside_direction = inside_dir

#     # print(direction)
#     ret = travel(direction, coming_from)
#     curr_x += ret[0]
#     curr_y += ret[1]
#     coming_from = ret[2]

# # then loop and count
# curr_x = x_s
# curr_y = y_s + 1
# test_x = x_s+1
# test_y = y_s
# count = 0
# while not (curr_x == x_s) or not (curr_y == y_s):
#     loc = map[curr_y][curr_x]
#     direction = loc.char
#     inside_dir = loc.inside_direction

    
#     if inside_dir == "r":
#         for i in range(curr_x+1, width):
#             new_loc = map[curr_y][i]
#             if new_loc.on_path:
#                 break
            
#             if new_loc.counted:
#                 pass
#             else:
#                 new_loc.counted = True
#                 count += 1
#     elif inside_dir == "l":
#         for i in range(curr_x-1, -1, -1):
#             new_loc = map[curr_y][i]
#             if new_loc.on_path:
#                 break
            
#             if new_loc.counted:
#                 pass
#             else:
#                 new_loc.counted = True
#                 count += 1
#     elif inside_dir == "d":
#         for i in range(curr_y+1, height):
#             new_loc = map[i][curr_x]
#             if new_loc.on_path:
#                 break
            
#             if new_loc.counted:
#                 pass
#             else:
#                 new_loc.counted = True
#                 count += 1
#     elif inside_dir == "u":
#         for i in range(curr_y-1, -1, -1):
#             new_loc = map[i][curr_x]
#             if new_loc.on_path:
#                 break
            
#             if new_loc.counted:
#                 pass
#             else:
#                 new_loc.counted = True
#                 count += 1

#     ret = travel(direction, coming_from)
#     curr_x += ret[0]
#     curr_y += ret[1]
#     coming_from = ret[2]


# print()
# for y in range(height):
#     for x in range(width):
#         if map[y][x].on_path:
#             print(map[y][x].char,end="")
#         else:
# #             print(" ",end="")
# #     print()
# print(map[test_y][test_x])
# print(count)


# part 1
# starting at S, loop around to count total steps, then divide by 2 (and ceil)
# start going down
# steps = 1
# curr_x = x_s
# curr_y = y_s + 1
# coming_from = "u"  # u = up, l = left, r = right, d = down

# # print(map[curr_y][curr_x])
# print(curr_x, curr_y, x_s, y_s)
# print(not (curr_x == x_s) or not (curr_y == y_s))

# while not (curr_x == x_s) or not (curr_y == y_s):
#     direction = map[curr_y][curr_x]
#     # print(direction)
#     if direction == "|":
#         if coming_from == "u":
#             curr_y += 1
#         else: curr_y -= 1

#     elif direction == "-":
#         if coming_from == "l":
#             curr_x += 1
#         else:
#             curr_x -= 1
    
#     elif direction == "L":
#         if coming_from == "u":
#             coming_from = "l"
#             curr_x += 1
#         else:
#             coming_from = "d"
#             curr_y -= 1

#     elif direction == "J":
#         if coming_from == "u":
#             coming_from = "r"
#             curr_x -= 1
#         else:
#             coming_from = "d"
#             curr_y -= 1
    
#     elif direction == "7":
#         if coming_from == "l":
#             coming_from = "u"
#             curr_y += 1
#         else:
#             coming_from = "r"
#             curr_x -= 1
    
#     elif direction == "F":
#         if coming_from == "r":
#             coming_from = "u"
#             curr_y += 1
#         else:
#             coming_from = "l"
#             curr_x += 1

#     else:
#         print("GOT ISSUES")

#     steps += 1

# print(ceil(steps / 2))