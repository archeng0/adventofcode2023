input = open("input.txt")
sum = 0

lastCard = 219
#day 2
numCards = [1 for i in range(lastCard)]
nextCardIdx = 1
while True:
    line = input.readline().strip()

    if not line:
        break

    # print(line)
    cardvsNums = line.split(':')
    # print(cardvsNums)

    # get card num
    card = cardvsNums[0]
    x = len(card) - 1

    cardNum = ''
    while card[x].isdigit():
        cardNum = cardNum + card[x]
        x -= 1
    
    allNums = cardvsNums[1].split('|')
    winningNums = allNums[0].split()
    ourNums = allNums[1].split()
    # print(winningNums)
    # print(ourNums)

    winCount = 0
    for num in ourNums:
        if num in winningNums:
            winCount += 1

    print(winCount)
    cardsWon = min(winCount, lastCard-nextCardIdx)
    idx = nextCardIdx
    currIdx = nextCardIdx - 1
    for i in range(cardsWon):
        numCards[idx] += numCards[currIdx]
        idx += 1

    nextCardIdx += 1
    


print(numCards)
for num in numCards:
    sum += num
print("final sum:",sum)



#day 1
# print(sum)

# while True:
#     line = input.readline().strip()

#     if not line:
#         break

#     # print(line)
#     cardvsNums = line.split(':')
#     # print(cardvsNums)

#     # get card num
#     card = cardvsNums[0]
#     x = len(card) - 1

#     cardNum = ''
#     while card[x].isdigit():
#         cardNum = cardNum + card[x]
#         x -= 1
    
#     allNums = cardvsNums[1].split('|')
#     winningNums = allNums[0].split()
#     ourNums = allNums[1].split()
#     print(winningNums)
#     print(ourNums)

#     winCount = 0
#     for num in ourNums:
#         if num in winningNums:
#             print("num in:", num)
#             winCount += 1
    

#     if winCount > 0:
#         score = 2 ** (winCount-1)
#     else:
#         score = 0
#     # print(winCount)
#     # print(score)
#     sum += score

# print(sum)

    
