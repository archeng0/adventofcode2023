"""
plan:
read input getting:
1. a list of seed numbers
2. lists of maps where each map is a list of [x,y,z]:
x is the lower bound for input, y is the upper bound, and z is the starting point for the output

then, pass all seeds through maps when appropriate, saving to a new list
then find the lowest in the new list, and return that


(enumerate?)
"""


input = open("input.txt")
#part 2
# first get seeds
seedLine = input.readline().strip().split(':')[1].split()
seedRange = []
for i in range (int(len(seedLine) / 2)):
    base = int(seedLine[2*i])
    seedRange.append([base, base+int(seedLine[2*i+1])-1])

# skip newline
line = input.readline().strip()

def makeList():
    #skip text
    line = input.readline().strip()

    tempList = []

    while True:
        line = input.readline().strip()

        if not line:
            # reading this section done
            break

        # add xyz for each line
        nums = line.split()
        # print(nums)
        for i,num in enumerate(nums):
            nums[i] = int(num)

        tempList.append([nums[1], nums[1]+nums[2]-1, nums[0]])
    
    return tempList

def checkRange(range, table):
    # print(table)
    newRange = []
    currTableIdx = 0

    # can optimize, not loop over all pairs with each entry, iterate over pairs and entries together
    for pair in range:
        # print("pair:", pair)
        # undealt with:
        low = pair[0]
        high = pair[1]

        for entry in table:
            # print("entry: ", entry)
            # first if min in pair less than min in entry
            if low < entry[0]:
                # print("low")
                
                # if max in pair also less, then go next
                if high < entry[0]:
                    newRange.append([low, high]) # no scaling needed
                    low = high + 1
                    break;
                else: # deal with the lower numbers, keep going with current pair
                    newRange.append([low, entry[0]-1]) # no scaling needed
                    low = entry[0]
            
            # print(low)
            # print(high)

            # now if low below higher entry
            if low < entry[1]:
                # print("not so low")
                #if max also less, go next
                if high < entry[1]:
                    # print("not high")
                    # for scaling
                    diff = low - entry[0]
                    diff2 = high - low
                    newRange.append([entry[2] + diff, entry[2] + diff + diff2]) # scale
                    low = high + 1
                    break;
                else: # add the entry, keep going with next entry
                    diff = low - entry[0]
                    diff2 = entry[1] - low
                    newRange.append([entry[2] + diff, entry[2] + diff + diff2]) # scale
                    low = entry[1] + 1
            
            # print(low)

        # now check if above:
        if low <= high:
            newRange.append([low, high])




        

        # go until min in pair is greater than x in current table entry

        #include case for not found?

        currTableIdx = 0
        
    # print(newRange)
    return newRange

# def passThrough(seed, tables):
#     inCheck = int(seed)

#     notFound = True
#     # go through all tables
#     for table in tables:
#         # go through each entry
#         for entry in table:
#             if entry[0] <= inCheck <= entry[1]:
#                 inCheck = entry[2] + inCheck - entry[0]
#                 # notFound = False
#                 break

#     return inCheck
            
tables = []
for i in range(7):
    tables.append(sorted(makeList()))

#seedrange: list of [l, h] where l and h are lowest and highest (inclusive) value for seeds
print(seedRange)

currRange = seedRange
# currRange = checkRange(currRange, tables[0])
# print(currRange)
for table in tables:
    currRange = checkRange(currRange, table)
    # print(currRange)

sort = sorted(currRange)
#then find lowest in curr range
print(sort)
print(sort[0][0])



# #part 1
# # first get seeds
# seedLine = input.readline().strip().split(':')[1].split()
# # print(seedLine)

# # skip newline
# line = input.readline().strip()

# def makeList():
#     #skip text
#     line = input.readline().strip()

#     tempList = []

#     while True:
#         line = input.readline().strip()

#         if not line:
#             # reading this section done
#             break

#         # add xyz for each line
#         nums = line.split()
#         # print(nums)
#         for i,num in enumerate(nums):
#             nums[i] = int(num)

#         tempList.append([nums[1], nums[1]+nums[2]-1, nums[0]])
    
#     return tempList

# def passThrough(seed, tables):
#     inCheck = int(seed)
#     # out = -1

#     notFound = True
#     # go through all tables
#     for table in tables:
#         # go through each entry
#         for entry in table:
#             if entry[0] <= inCheck <= entry[1]:
#                 inCheck = entry[2] + inCheck - entry[0]
#                 # notFound = False
#                 break

#     return inCheck
            
#         # print(table)
# # s2s = s2f = f2w = w2l = l2t = t2h = h2l = []
# # maybe make s2s, s2f... into a list of lists instead??
# # s2s = makeList()

# # s2f = makeList()

# # f2w = makeList()

# # w2l = makeList()

# # l2t = makeList()

# # t2h = makeList()

# # h2l = makeList()

# # tables = [s2s, s2f, f2w, w2l, l2t, t2h, h2l]
# tables = []

# for i in range(7):
#     tables.append(makeList())

# # print(tables)

# #check seed locations
# seedLoc = []
# for seed in seedLine:
#     seedLoc.append(passThrough(seed, tables))

# print(min(seedLoc))
# #return