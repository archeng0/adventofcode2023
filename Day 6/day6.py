from math import floor
from math import ceil
import cmath

input = open("input.txt")


sum = 1
timeL = input.readline().strip().split(':')[1]
distanceL = input.readline().strip().split(':')[1]
print(timeL)

time = ""
for char in timeL:
    if char.isdigit():
        time = time + char

distance = ""
for char in distanceL:
    if char.isdigit():
        distance = distance + char

print(time)
print(distance)

# imported polynomial solver
# calculating  the discriminant
def solvPoly(b,c):
    #a = -1, simplified already
    dis = (b**2) - (-4*c)
    
    # find two results
    ans1 = (-b-cmath.sqrt(dis))/(-2)
    ans2 = (-b + cmath.sqrt(dis))/(-2)
    
    return[ans1.real, ans2.real]

ans = solvPoly(int(time), -1 * int(distance))
print(ans)
ans = sorted(ans)
if ceil(ans[0]) == ans[0]:
    a1 = int(ans[0] + 1)
else: a1 = ceil(ans[0])
if floor(ans[1]) == ans[1]:
    a2 = int(ans[1] - 1)
else: a2 = floor(ans[1])

print(a2-a1+1)

# #part 1
# sum = 1
# times = input.readline().strip().split(':')[1].split()
# distances = input.readline().strip().split(':')[1].split()

# # print(times, distances)

# # formula for how long to hold is (t - x) * x = d where t is total time, x is time to hold and d is record distance
# # same as -x^2+tx-d=0 (remember horner's rule, not applicable but interesting)

# # imported polynomial solver
# # calculating  the discriminant
# def solvPoly(b,c):
#     #a = -1, simplified already
#     dis = (b**2) - (-4*c)
    
#     # find two results
#     ans1 = (-b-cmath.sqrt(dis))/(-2)
#     ans2 = (-b + cmath.sqrt(dis))/(-2)
    
#     return[ans1.real, ans2.real]

# answers = []
# for i, time in enumerate(times):
#     ans = solvPoly(int(time), -1 * int(distances[i]))
#     ans = sorted(ans)

#     if ceil(ans[0]) == ans[0]:
#         a1 = int(ans[0] + 1)
#     else: a1 = ceil(ans[0])

#     if floor(ans[1]) == ans[1]:
#         a2 = int(ans[1] - 1)
#     else: a2 = floor(ans[1])

#     # print(ans[1], floor(ans[1]), a2)
#     answers.append([a1, a2])

# # print(answers)

# for pair in answers:
#     sum *= pair[1] - pair[0] + 1

# print(sum)
