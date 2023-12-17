input = open("input.txt")

# recursive function that extrapolates data
def extrapolate(data):
    print("extrapolating:", data)

    # base case
    if all(d == 0 for d in data):
        # print("base")
        return 0

    # if not base case, calculate differences
    differences = [x - data[i - 1] for i, x in enumerate(data) if i > 0]

    # print("returning:", data[0] - extrapolate(differences))
    return data[0] - extrapolate(differences)

next_val = []

while True:
    line = input.readline().strip().split()

    if not line:
        break

    data = []
    for l in line:
        data.append(int(l))

    # print(data)
    next_val.append(extrapolate(data))

print(sum(next_val))




# # part 1
# # recursive function that extrapolates data
# def extrapolate(data):
#     # print("extrapolating:", data)

#     # base case
#     if all(d == 0 for d in data):
#         # print("base")
#         return 0

#     # if not base case, calculate differences
#     differences = [x - data[i - 1] for i, x in enumerate(data) if i > 0]

#     # print("returning:", data[-1] + extrapolate(differences))
#     return data[-1] + extrapolate(differences)




# next_val = []

# while True:
#     line = input.readline().strip().split()

#     if not line:
#         break

#     data = []
#     for l in line:
#         data.append(int(l))

#     # print(data)
#     next_val.append(extrapolate(data))

# print(sum(next_val))