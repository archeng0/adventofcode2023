input = open("input.txt")
inputArray = []
yLastIdx = -1
sum = 0
while True:
    line = input.readline()

    if not line:
        break

    inputArray.append(line)
    # print(line)
    xLastIdx = len(line) - 1
    yLastIdx += 1
check = False
def checkAround(x, y, len):
    # print("checking with ", x, y, len)
    global inputArray; xLastIdx; yLastIdx; check;

    if check:
        print("checking with ", x, y, len)
        
    # check = False

    x = int(x)
    y = int(y)
    len = int(len)
    top = max(0, y-1)
    bot = min(yLastIdx, y+1)
    left = max(0, x-1)
    right = min(xLastIdx, left+len+1)
    # print(left, right)
    # print(top, bot)
    valid = False
    for y in range (top, bot + 1):
        for x in range(left, right + 1):
            if check:
                print(inputArray[y][x])
            if not (inputArray[y][x].isdigit() or inputArray[y][x] == '.' or inputArray[y][x] == '\n'):
                valid = True

    return valid

    
    # print("checking")

# print(xLastIdx, yLastIdx)
numlist = []
check = False
y = 0
for line in inputArray:
    x = 0
    for char in line:
        if x > xLastIdx:
            break
        # print(line[x])
        # check if number, if it is then check around

        if line[x].isdigit():
            len = 0
            start = x
            # temp = x
            # find length
            num = ''
            while line[x].isdigit():
                # print(line[x])
                num = num + line[x]
                # print(num)
                x += 1
                len += 1
                if num == '618':
                    print("FOUND")
                    print()
                    check = True
            # print(num)
            # print("l", len)
            # print(start, y, len)
            if checkAround(start, y, len):
                check = False
                # print("pass:",num)
                numlist.append(int(num))
                sum += int(num)

        else:
            x+= 1
    y += 1
            
        # print("idx", x)




# print(numlist)
print(sum)
# print(inputArray[0][6]    )
