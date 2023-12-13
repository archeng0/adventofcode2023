#part 1:
import re

input = open("input.txt")
sum = 0
pattern = r'\b\d+\b'

maxR = 0
maxB = 0
maxG = 0

def remax(r, b, g):
    global maxR; global maxB; global maxG;
    if r > maxR:
        maxR = r
    if b > maxB:
        maxB = b
    if g > maxG:
        maxG = g

while True:
    line = input.readline()

    if not line:
        break

    maxR = 0
    maxB = 0
    maxG = 0

    draws = line.split(":")
    draws = draws[1].split(";")

    for element in draws:
        red = 0
        blue = 0
        green = 0
        colors = element.split(",")
        for color in colors:
            if "red" in color:
                red = int(re.findall(pattern, color)[0])
            elif "green" in color:
                green = int(re.findall(pattern, color)[0])
            elif "blue" in color:
                blue = int(re.findall(pattern, color)[0])
        
        remax(red, green, blue)
    # print(maxR, maxB, maxG)
    sum += (maxR * maxB * maxG)



print(sum)
input.close()


























# import re

# input = open("input.txt")
# sum = 0
# pattern = r'\b\d+\b'

# while True:
#     line = input.readline()

#     if not line:
#         break

#     # print(line)
#     # split line into each draw
#     # print(line)
#     # gameNum = int(line[line.index(":") - 1])
#     # gameNum = 0
#     draws = line.split(":")
#     gameNum = int(re.findall(pattern, draws[0])[0])
#     # print(gameNum)
#     # print(draws)
#     draws = draws[1].split(";")
#     # print(draws)
#         # split draws into colors and numbers

#     valid = True
#     for element in draws:
#         red = 0
#         blue = 0
#         green = 0
#         colors = element.split(",")
#         for color in colors:
#             if "red" in color:
#                 red = int(re.findall(pattern, color)[0])
#                 # print(red)
#             elif "green" in color:
#                 green = int(re.findall(pattern, color)[0])
#             elif "blue" in color:
#                 blue = int(re.findall(pattern, color)[0])

#         if red > 12 or green > 13 or blue > 14:
#             valid = False
#             # print("false")
#             break

#         # print(colors)

#         # if "red" in element:
#         #     print("red", element[element.index("red") - 2])
#         #     if int(element[element.index("red") - 2]) > 12:
#         #         valid = False
#         # if "blue" in element:
#         #     if int(element[element.index("blue") - 2]) > 14:
#         #         valid = False
#         # if "green" in element:
#         #     if int(element[element.index("green") - 2]) > 13:
#         #         valid = False

#     if valid:
#         sum += gameNum
#         # print("game works", gameNum)


# print(sum)
# input.close()