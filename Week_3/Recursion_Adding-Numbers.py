answer = 0
n = int(input())
for i in range(n + 1):
    answer = answer + i
print("The answer is", answer)
# Function Version
def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)
    
n = int(input())
print(sum(n))

# 5 + sum(4)
# 5 + 4 + sum(3)
# 5 + 4 + 3 + sum(2)
# 5 + 4 + 3 + 2 + sum(1)
# 5 + 4 + 3 + 2 + 1 = 15