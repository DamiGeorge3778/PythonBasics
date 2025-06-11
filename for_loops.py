# q) write a code to calculate sum of n numbers, n should be taken as input
# s1) using for loop
# s2) using while loop
# if n= 5
# sum = 1+2+3+4+5

answer = 0
n = int(input())
for i in range(n + 1):
    answer = answer + i
print("Answer is", answer)