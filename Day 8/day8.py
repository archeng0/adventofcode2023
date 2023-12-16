from math import gcd

input = open("input.txt")

def convert_to_num(string):
    # convert a 3 letter string to a 3 digit num, A = 0, B = 1 ... Z = 25

    ret = []
    for char in string:
        # convert to ascii, then subtract 65 for A
        ret.append((ord(char) - 65))
    return ret

# first all 3 letter combinations, then populate with directions.
paths = [[[0 for i in range(26)] for i in range(26)] for i in range(26)]
# paths[23][22][2] = [43,23,12]

directions = input.readline().strip()

#list of current locations:
current_locs = []
#skip newline
input.readline()
while True:
    line = input.readline().strip()

    if not line:
        break

    line = line.split("=")

    origin = line[0].strip()
    # print(origin)
    if origin[2] == "A":
        # print(origin)
        current_locs.append(convert_to_num(origin))
        # print("adding loc")

    destination = line[1].strip(" ()").split(', ')

    origin = convert_to_num(origin)
    destinationL = convert_to_num(destination[0])
    destinationR = convert_to_num(destination[1])

    # go to origin location, insert destination
    paths[origin[0]][origin[1]][origin[2]] = [destinationL, destinationR]
    
max_left_or_right = len(directions)
# print(max_left_or_right)


# print(current_locs)
#using lcm method
shortest_to_z = [0 for x in range(len(current_locs))]
print(paths[0][0][1])
for i, loc in enumerate(current_locs):
    temp_loc = loc
    # print("outer:",temp_loc)
    total_steps = 0
    left_or_right = 0
    test = 0
    while True:
        # print("inner",temp_loc)
        #check if got to Z
        if temp_loc[2] == 25:
            # print("breakING")
            shortest_to_z[i] = total_steps
            break

        # check if need to reset index
        if left_or_right == max_left_or_right:
            left_or_right = 0
        
        # if not at ZZZ go to direction and go either left or right for all locs
        if directions[left_or_right] == "L":
            # print("going left")
            temp_loc = paths[temp_loc[0]][temp_loc[1]][temp_loc[2]][0]
        else:
            # print("going right")
            temp_loc = paths[temp_loc[0]][temp_loc[1]][temp_loc[2]][1]

        left_or_right += 1
        total_steps += 1
        # test += 1
        # if test > 10:
        #     break
    # print(total_steps)
    # test_count+= 1
    
    # if test_count == 9:
    #     break

# print(paths[0][0][0])

# print(shortest_to_z)

lcm = 1
for i in shortest_to_z:
    print(i)
    lcm = lcm * i // gcd(lcm, i)
print(lcm)

#old
# print(current_locs)
# test_count = 0
# while True:
#     #check if all locs at ZZZ
#     done = True
#     for loc in current_locs:
#         # print(loc[2])
#         if not (loc[2] == 25):
#             done = False
#             break

#     if done:
#         # print("all done")
#         break

#     # check if need to reset index
#     if left_or_right == max_left_or_right:
#         left_or_right = 0
    
#     # if not at ZZZ go to direction and go either left or right for all locs
#     for i, loc in enumerate(current_locs):
#         if directions[left_or_right] == "L":
#             current_locs[i] = paths[loc[0]][loc[1]][loc[2]][0]
#         else:
#             current_locs[i] = paths[loc[0]][loc[1]][loc[2]][1]

#     # print(current_locs)

#     # print("new_loc", current_loc)
    

#     left_or_right += 1
#     total_steps += 1
#     # print(total_steps)
#     # test_count+= 1
    
#     # if test_count == 9:
#     #     break

# # print(paths[0][0][0])

# print(total_steps)



# #part 1
# # first all 3 letter combinations, then populate with directions.
# paths = [[[0 for i in range(26)] for i in range(26)] for i in range(26)]
# # paths[23][22][2] = [43,23,12]

# directions = input.readline().strip()

# #skip newline
# input.readline()
# while True:
#     line = input.readline().strip()

#     if not line:
#         break

#     line = line.split("=")

#     origin = line[0].strip()
#     destination = line[1].strip(" ()").split(', ')

#     origin = convert_to_num(origin)
#     destinationL = convert_to_num(destination[0])
#     destinationR = convert_to_num(destination[1])

#     # go to origin location, insert destination
#     paths[origin[0]][origin[1]][origin[2]] = [destinationL, destinationR]
    
# total_steps = 0
# left_or_right = 0  # index for directions
# max_left_or_right = len(directions)
# # print(max_left_or_right)

# current_loc = [0,0,0]

# while True:
#     #check if at ZZZ
#     if current_loc == [25,25,25]:
#         break

#     #check if need to reset index
#     if left_or_right == max_left_or_right:
#         left_or_right = 0
    
#     # if not at ZZZ go to direction and go either left or right
    
#     if directions[left_or_right] == "L":
#         current_loc = paths[current_loc[0]][current_loc[1]][current_loc[2]][0]
#     else:
#         current_loc = paths[current_loc[0]][current_loc[1]][current_loc[2]][1]

#     # print("new_loc", current_loc)
    

#     left_or_right += 1
#     total_steps += 1

# # print(paths[0][0][0])
# print(total_steps)