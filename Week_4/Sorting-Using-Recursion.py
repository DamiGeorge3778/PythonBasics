def mini(L):
    mini = L[0]
    for x in L:
        if x<mini:
            mini = x
    return mini

def sort(L):
    if L == [] or (len(L)) == 1:
        return L
    m = mini(L)
    L.remove(m)
    return [m]+sort(l)

l = [3,1,5,7,2]
print(sort(l))