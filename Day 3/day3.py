input = open("input.txt")

inputArray = []
yLastIdx = -1
sum = 0

# read the input, convert to a 2D array
while True:
    line = input.readline()

    if not line:
        break

    inputArray.append(line)
    # print(line)
    xLastIdx = len(line) - 1
    yLastIdx += 1


def getNum(loc):
    global inputArray; xLastIdx;
    x = loc[0]
    y = loc[1]
    # print(inputArray[loc[1]][loc[0]])

    ret = inputArray[y][x]
    while x > 0 and inputArray[y][x-1].isdigit():
        ret = inputArray[y][x-1] + ret
        x-=1
    x = loc[0]
    while x < xLastIdx and inputArray[y][x+1].isdigit():
        ret = ret + inputArray[y][x+1]
        x+=1


    print("ret",ret)
    
    return int(ret)

# check around a gear and calculates gear ratio if relevant
# takes index of gear in the array as input, returns gear ratio if it should, False otherwise
def checkGear(x, y):
    global inputArray; xLastIdx; yLastIdx;
    # print(inputArray[y][x])
    print("checking at", x, y)
    x = int(x)
    y = int(y)
    top = max(0, y-1)
    bot = min(yLastIdx, y+1)
    left = max(0, x-1)
    right = min(xLastIdx, x+1)

    # print(left, right)
    # print(top, bot)

    row = 0
    numTouch = 0
    num1 = [-1,-1]
    num2 = [-1,-1]

    for y in range (top, bot + 1):
        l = False
        m = False
        r = False
        lmr = 0

        for x in range(left, right + 1):
            # lmr = 0
            if inputArray[y][x].isdigit():
                # print(inputArray[y][x])

                if row == 1:
                    numTouch += 1
                    if num1 == [-1,-1]:
                        num1 = [x,y]
                    elif num2 == [-1,-1]:
                        num2 = [x,y]
                    else: break
                else:
                    if lmr == 0:
                        l = True
                    elif lmr == 1:
                        m = True
                    else:
                        r = True

            lmr += 1

        row += 1
        if row == 1 or row == 3:
            # check cases
            if l and m and r:
                # print("all", row)
                numTouch += 1
                if num1 == [-1,-1]:
                    num1 = [x,y]
                elif num2 == [-1,-1]:
                    num2 = [x,y]
                else: break

            elif not (l or m or r):
                pass
                # print("none", row)

            elif l:
                if m:
                    numTouch+= 1
                    # print("l,m")
                    if num1 == [-1,-1]:
                        num1 = [x-1,y]
                    elif num2 == [-1,-1]:
                        num2 = [x-1,y]
                    else: break
                elif r:
                    numTouch += 2
                    # print("l, r")
                    if not (num1 == [-1,-1]):
                        break;
                    else:
                        num1 = [x-2,y]
                        num2 = [x,y]
                else:
                    numTouch += 1
                    # print("l")
                    if num1 == [-1,-1]:
                        num1 = [x-2,y]
                    elif num2 == [-1,-1]:
                        num2 = [x-2,y]
                    else: break
            elif m:
                if r:
                    numTouch += 1
                    # print("m,r")
                    if num1 == [-1,-1]:
                        num1 = [x,y]
                    elif num2 == [-1,-1]:
                        num2 = [x,y]
                    else: break
                else:
                    numTouch += 1
                    # print("m")
                    if num1 == [-1,-1]:
                        num1 = [x-1,y]
                    elif num2 == [-1,-1]:
                        num2 = [x-1,y]
                    else: break
            elif r:
                numTouch += 1
                if num1 == [-1,-1]:
                    num1 = [x,y]
                elif num2 == [-1,-1]:
                    num2 = [x,y]
                else: break
            



            # print("lmr:" ,l, m, r, row) 
    # print("numt",numTouch)
    print(num1, num2)

    if numTouch == 2:
        return getNum(num1) * getNum(num2)
    else: return False

y = 0
for line in inputArray:
    x = 0
    for char in line:

        # if gone too far
        if x > xLastIdx:
            break

        # first check if char is a gear
        if line[x] == '*':
            # print("found gear")
            ret = checkGear(x, y)
            if ret: # check gear returns number
                sum += int(ret)
            x+= 1
        #     len = 0
        #     start = x
        #     # temp = x
        #     # find length
        #     num = ''
        #     while line[x].isdigit():
        #         # print(line[x])
        #         num = num + line[x]
        #         # print(num)
        #         x += 1
        #         len += 1
        #         if num == '618':
        #             print("FOUND")
        #             print()
        #             check = True
        #     # print(num)
        #     # print("l", len)
        #     # print(start, y, len)
        #     if checkAround(start, y, len):
        #         check = False
        #         # print("pass:",num)
        #         numlist.append(int(num))
        #         sum += int(num)

        else:
            x+= 1
    y += 1


print(sum)

#part 1
# inputArray = []
# yLastIdx = -1
# sum = 0
# while True:
#     line = input.readline()

#     if not line:
#         break

#     inputArray.append(line)
#     # print(line)
#     xLastIdx = len(line) - 1
#     yLastIdx += 1

# check = False
# def checkAround(x, y, len):
#     # print("checking with ", x, y, len)
#     global inputArray; xLastIdx; yLastIdx; check;

#     if check:
#         print("checking with ", x, y, len)
        
#     # check = False

#     x = int(x)
#     y = int(y)
#     len = int(len)
#     top = max(0, y-1)
#     bot = min(yLastIdx, y+1)
#     left = max(0, x-1)
#     right = min(xLastIdx, left+len+1)
#     # print(left, right)
#     # print(top, bot)
#     valid = False
#     for y in range (top, bot + 1):
#         for x in range(left, right + 1):
#             if check:
#                 print(inputArray[y][x])
#             if not (inputArray[y][x].isdigit() or inputArray[y][x] == '.' or inputArray[y][x] == '\n'):
#                 valid = True

#     return valid

    
#     # print("checking")

# # print(xLastIdx, yLastIdx)
# numlist = []
# check = False
# y = 0
# for line in inputArray:
#     x = 0
#     for char in line:
#         if x > xLastIdx:
#             break
#         # print(line[x])
#         # check if number, if it is then check around

#         if line[x].isdigit():
#             len = 0
#             start = x
#             # temp = x
#             # find length
#             num = ''
#             while line[x].isdigit():
#                 # print(line[x])
#                 num = num + line[x]
#                 # print(num)
#                 x += 1
#                 len += 1
#                 if num == '618':
#                     print("FOUND")
#                     print()
#                     check = True
#             # print(num)
#             # print("l", len)
#             # print(start, y, len)
#             if checkAround(start, y, len):
#                 check = False
#                 # print("pass:",num)
#                 numlist.append(int(num))
#                 sum += int(num)

#         else:
#             x+= 1
#     y += 1
            
#         # print("idx", x)




# # print(numlist)
# print(sum)
# # print(inputArray[0][6]    )
