L = [3, 1, 3, 1, 3]

count_dict = {}

for i in L:
    if i in count_dict:
        count_dict[i] += 1

    else:
        count_dict[i] = 1

print(count_dict)

#Problem 2: write iteration for this program
# 1st iteration
# count_dict = {}
# i = 3
# 3 in count_dict ? F
# count_dict[3] = 1

# 2nd iteration:
# count_dict = {3:1}
# i = 1
# is 1 in key of count_dict ? F
# count_dict[1] = 1

# 3rd iteration:
# count_dict = {3:1, 1:1}
# i = 3
# 3 in count_dict? T
# count_dict[3] += 1

# 4th iteration:
# count_dict = {3:2, 1:2}
# i = 1
# 1 in count_dict? T
# count_dict[1] += 1

# count_dict = {3:2, 1:2}

# 5th iteration:
# count_dict = {3:2, 1:2}
# i = 3
# 3 in count_dict ? T
# count_dict[3] += 1

# count_dict = {3:3, 1:2}