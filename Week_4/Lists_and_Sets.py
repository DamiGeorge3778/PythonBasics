# Question 1: Lists and Sets
# Write a Python function that takes a list of integers as input and returns a list containing only the unique elements, preserving their original order.

# Example Input:

# [4, 5, 6, 4, 2, 5, 7]  

# Expected Output:

# [4, 5, 6, 2, 7]

def get_unique_elements(L):
    unique_list = []
    seen = set()
    for num in L:
        if num not in seen:
            seen.add(num)
            unique_list.append(num)
    return unique_list        
l = [4, 5, 6, 4, 2, 5, 7] 
print(get_unique_elements(l))

# 1st iteration
# unique_list = []
# seen = ()
# num = 4
# if 4 exists in seen? F
# seen = (4)
# unique_list = [4]

# 2nd iteration
# unique_list = [4]
# seen = (4)
# num = 5
# if 5 exists in seen? F
# seen = (4, 5)
# unique_list = [4, 5]

# 3rd iteration
# unique_list = [4, 5]
# seen = (4, 5)
# num = 6
# if 6 exists in seen? F
# seen = (4, 5, 6)
# unique_list = [4, 5, 6]

# 4th iteration
# unique_list = [4, 5, 6]
# seen = (4, 5, 6)
# num = 4
# if 4 exists in seen? T

# 5th iteration
# unique_list = [4, 5, 6]
# seen = (4, 5, 6)
# num = 2
# if 2 exists in seen? F
# seen = (4, 5, 6, 2)
# unique_list = [4, 5, 6, 2]

# 6th iteration
# unique_list = [4, 5, 6, 2]
# seen = (4, 5, 6, 2)
# num = 5
# if 5 exists in seen? T

# 7th iteration
# unique_list = [4, 5, 6, 2]
# seen = (4, 5, 6, 2)
# num = 7
# if 7 exists in seen? F
# seen = (4, 5, 6, 2, 7)
# unique_list = [4, 5, 6, 2, 7]