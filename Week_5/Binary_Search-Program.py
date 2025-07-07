l = [2, 4, 7, 10, 15, 18, 21]

def binary_search(l, target):
    left = 0
    right = len(l) - 1

    while left <= right:
        mid = (left+right) // 2
        if l[mid] == target:
            return f"Found at index {mid}"
        elif l[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return "Not Found"

question = int(input('Search a number '))

print(binary_search(l, question))

# Start Iterations
# ---------------------
# Iteration 1
# question = 18
# l = [2, 4, 7, 10, 15, 18, 21]
# target = 18
# binary_search([2, 4, 7, 10, 15, 18, 21], 18)
# ---------------------------------------------
# left = 0
# right = len(l) - 1
#       = 7-1
#       = 6
# ----------------------------------------------------
# while 0 <= 6 True
# mid = 0+6 // 2
#       = 3
# if l[mid] == target
# l[3] == 18
# 10 == 18 False
# -----------------------------------
# elif l[mid] < target
# l[3] < 18
# 10 < 18 True
# left = mid + 1
# left = 3 + 1
# left 4
# ---------------------------------------------------------

# Iteration 2

# while left <= right
# left = 4
# right = 6
# 4 <= 6 True
# mid = 4+6 // 2
# mid = 5
# ---------------------------------
# if l[mid] == target
# l[5] == 18
# 18 == 18 True/Found
# --------------------
# Found at index 5