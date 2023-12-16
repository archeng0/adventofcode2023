'''
solve using merge sort function, requires creating comparison function
'''


from dataclasses import dataclass

input = open("input.txt")

HIGH_CARD = 0
ONE_PAIR = 1
TWO_PAIR = 2
THREE_KIND = 3
FULL_HOUSE = 4
FOUR_KIND = 5
FIVE_KIND = 6

RANKING_STRING = "AKQT98765432J"

@dataclass
class Hand:
    bet: int
    hand: str
    strength: int = -1

# returns true if hand 1 is stronger, false if hand 2 is stronger
def compare(hand1, hand2):

    h1_str = hand1.strength
    h2_str = hand2.strength

    if h1_str > h2_str:
        return True
    if h2_str > h1_str:
        return False

    # tied in strengh, compare card by card
    h1_cards = hand1.hand
    h2_cards = hand2.hand

    for i in range(5):
        c1 = h1_cards[i]
        c2 = h2_cards[i]

        if c1 == c2:
            continue

        for char in RANKING_STRING:
            if char == c1:
                return True
            if char == c2:
                return False    

def merge(left, right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0
    while len(result) < len(left) + len(right):

        if not compare(left[index_left], right[index_right]):
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break
    return result

def merge_sort(hand_list):
    if len(hand_list) < 2:
        return hand_list

    midpoint = len(hand_list) // 2

    return merge(merge_sort(hand_list[:midpoint]), merge_sort(hand_list[midpoint:]))
    

def find_strength(hand):
    cards = hand.hand
    data = []
    jokers = 0
    if cards == "JJJJJ":
        return FIVE_KIND

    for char in cards:
        if char == "J":
            jokers += 1
        found = False
        for pair in data:
            if char == pair[0]:
                pair[1] += 1
                found = True
        if not found:
            data.append([char, 1])

    sorted_data = sorted(data, key = lambda x:x[1], reverse = True)

    if sorted_data[0][0] == "J":
        num = sorted_data[1][1]
    else: 
        num = sorted_data[0][1]
    if num + jokers == 5:
        return FIVE_KIND
    elif num + jokers == 4:
        return FOUR_KIND
    elif num + jokers == 3:
        if sorted_data[1][1] == 2:
            return FULL_HOUSE
        else:
            return THREE_KIND
    elif num + jokers == 2:
        if sorted_data[1][1] == 2:
            return TWO_PAIR
        else:
            return ONE_PAIR
    else:
        return HIGH_CARD

hands = []

# first, init all hands
while True:
    line = input.readline().strip().split()

    if not line:
        break

    hands.append(Hand(line[1], line[0]))

# calculate strength of all hands
for h in hands:
    h.strength = find_strength(h)

# sort all hands
hands = merge_sort(hands)


# print(compare(hands[2], hands[3]))
# calculate final winnings
print(hands)
sum = 0
for i, hand in enumerate(hands):
    # print(i+1, int(hand.bet))
    sum += (i+1) * int(hand.bet)

print(sum)

#part 1
# # returns true if hand 1 is stronger, false if hand 2 is stronger
# def compare(hand1, hand2):

#     h1_str = hand1.strength
#     h2_str = hand2.strength

#     if h1_str > h2_str:
#         return True
#     if h2_str > h1_str:
#         return False

#     # tied in strengh, compare card by card
#     h1_cards = hand1.hand
#     h2_cards = hand2.hand

#     for i in range(5):
#         c1 = h1_cards[i]
#         c2 = h2_cards[i]

#         if c1 == c2:
#             continue

#         for char in RANKING_STRING:
#             if char == c1:
#                 return True
#             if char == c2:
#                 return False    

# def merge(left, right):
#     if len(left) == 0:
#         return right
#     if len(right) == 0:
#         return left

#     result = []
#     index_left = index_right = 0
#     while len(result) < len(left) + len(right):

#         if not compare(left[index_left], right[index_right]):
#             result.append(left[index_left])
#             index_left += 1
#         else:
#             result.append(right[index_right])
#             index_right += 1
#         if index_right == len(right):
#             result += left[index_left:]
#             break

#         if index_left == len(left):
#             result += right[index_right:]
#             break
#     return result

# def merge_sort(hand_list):
#     if len(hand_list) < 2:
#         return hand_list

#     midpoint = len(hand_list) // 2

#     return merge(merge_sort(hand_list[:midpoint]), merge_sort(hand_list[midpoint:]))
    

# def find_strength(hand):
#     cards = hand.hand
#     data = []

#     for char in cards:
#         found = False
#         for pair in data:
#             if char == pair[0]:
#                 pair[1] += 1
#                 found = True
#         if not found:
#             data.append([char, 1])

#     sorted_data = sorted(data, key = lambda x:x[1], reverse = True)

#     num = sorted_data[0][1]
#     if num == 5:
#         return FIVE_KIND
#     elif num == 4:
#         return FOUR_KIND
#     elif num == 3:
#         if sorted_data[1][1] == 2:
#             return FULL_HOUSE
#         else:
#             return THREE_KIND
#     elif num == 2:
#         if sorted_data[1][1] == 2:
#             return TWO_PAIR
#         else:
#             return ONE_PAIR
#     else:
#         return HIGH_CARD

# hands = []

# # first, init all hands
# while True:
#     line = input.readline().strip().split()

#     if not line:
#         break

#     hands.append(Hand(line[1], line[0]))

# # calculate strength of all hands
# for h in hands:
#     h.strength = find_strength(h)

# # sort all hands
# hands = merge_sort(hands)


# # print(compare(hands[2], hands[3]))
# # calculate final winnings
# print(hands)
# sum = 0
# for i, hand in enumerate(hands):
#     # print(i+1, int(hand.bet))
#     sum += (i+1) * int(hand.bet)

# print(sum)