input = open("input.txt", "r")
sum = 0
first = 0
second = 0

# PART 1:
# while True:
#     line = input.readline()

#     if not line:
#         break

#     # get first number
#     for char in line:
#         if char.isnumeric():
#             first = char
#             break

#     # get second number
#     rev = line [::-1]
#     for char in rev:
#         if char.isnumeric():
#             second = char
#             break
#     print(second)
#     print(first)
#     tSum = int(first + second)
#     print(tSum)
#     sum += tSum

# PART 2:
digitLetters = {"o", "t", "f", "s", "e", "n"}

def checkDigit(line, index):
    print("checking from", index)
    first = line[index]
    try:
        second = line[index+1]
    except:
        second = "z"
    try: 
        third = line[index+2]
    except:
        third = "z"
    try: 
        fourth = line[index+3]
    except:
        fourth = "z"
    try:
        fifth = line[index+4]
    except:
        fifth = "z"

    # print(first, second, third, fourth, fifth)

    if first == "o" and second == "n" and third == "e":
        return "1"
    elif first == "t":
        if second == "w" and third == "o":
            return "2"
        if second == "h" and third == "r" and fourth == "e" and fifth == "e":
            return "3"
    elif first == "f":
        if second == "o" and third == "u" and fourth == "r":
            return "4"
        if second == "i" and third == "v" and fourth == "e":
            return "5"
    elif first == "s":
        if second == "i" and third == "x":
            return "6"
        if second == "e" and third == "v" and fourth == "e" and fifth == "n":
            return "7"
    elif first == "e" and second == "i" and third == "g" and fourth == "h" and fifth == "t":
        return "8"
    elif first == "n" and second == "i" and third == "n" and fourth == "e":
        return "9"
    else:
        # print("fail")
        return False


while True:
    line = input.readline()

    if not line:
        break

    idx = -1
    # get first number
    # print("going forward")
    for char in line:
        idx += 1
        # print(idx)
        if char.isnumeric():
            first = char
            break
        if char in digitLetters:
            check = checkDigit(line, idx)
            if not check:
                # print("fail")
                pass
            else:
                # print("success")
                first = check
                break

    idx = -1
    length = len(line) - 1
    print("length: ",length)
    # get second number
    rev = line [::-1]
    print(rev)
    print("going backward")
    for char in rev:
        idx += 1
        print(idx)
        if char.isnumeric():
            second = char
            break
        if char in digitLetters:
            check = checkDigit(line, length - idx)
            if not check:
                print("bigfail")
                pass
            else:
                second = check
                print("success")
                break

    #     print("loop done")
    #     print("")

    # print("first: ",first)
    # print("second: ",second)

    # print(str(first) + (str(second)))
    tSum = int(str(first) + (str(second)))
    print(tSum)
    sum += tSum
    tSum = 0
    # print("sum: ", sum)




print(sum)

input.close