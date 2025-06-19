l = [12, 10, 7, 30, 3, 5, 1]
r = []
while(len(l)>0):
    min = l[0]
    for i in range(len(l)):
        if l[i] < min:
            min = l[i]
    r.append(min)
    l.remove(min)

print(l)
print(r)
# write iterations for this sorting program


# Iteration 1
# l = [12, 10, 7, 30, 3, 5, 1]
# Smallest value: min = 1
# Append l to r
# Removes 1 from l
# r = [1], l = [12, 10, 7, 30, 3, 5]

# Iteration 2
# min = 3
# Appends 3 to r
# Removes 3 from l
# r = [1, 3], l = [12, 10, 7, 30, 5]

# Iteration 3
# min = 5
# Appends 5 to r
# Removes 5 from l
# r = [1, 3, 5], l = [12, 10, 7, 30]

# Iteration 4
# min = 7
# Appends 7 to r
# Removes 7 from l
# r = [1, 3, 5, 7], l = [12, 10, 30]

# Iteration 5
# min = 10
# Appends 10 to r
# Removes 10 from l
# r = [1, 3, 5, 7, 10], l = [12, 30]

# Iteration 6
# min = 12
# Appends 12 to r
# Removes 12 from l
# r = [1, 3, 5, 7, 10, 12], l = [30]

# Iteration 7
# min = 30
# Appends 30 to r
# Removes 30 from l
# r = [1, 3, 5, 7, 10, 12, 30], l = []
# Finished yesterday