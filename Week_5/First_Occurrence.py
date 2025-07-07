# Q:
# Write a function to find the first occurrence of a target number in a sorted list that may contain duplicates using binary search.

# Example:
# Input: [1, 2, 4, 4, 4, 5, 6], target = 4
# Output: 2  (index of first 4)
l = [1, 2, 4, 4, 4, 5, 6]
def binary_search(l, target):
    left = 0
    right = len(l) - 1
    result = -1
    while left <= right:
        mid = (left+right) // 2
        if l[mid] == target:
            result = mid
            right = mid - 1
        elif l[mid] < target:
            left = mid + 1
        else:
            right = mid - 1    
    return result

question = int(input('Search a number '))

print(binary_search(l, question))