a = [1,2,3]
b = [2,4,5]
c = [1,3,6]

def union(a,b):
    diff = [x for x in a for y in b if x == y]
    newB = [x for x in b if x not in diff]
    var = [x for x in a + newB]
    return var

print union(a,b) # 1,2,3,4,5
print union(a,c) # 1,2,3,6


def intersection(a,b):
    var = [x for x in a for y in b if x == y]
    return var

print intersection(a,b) # 2
print intersection(c,b) # []
print intersection(a,c) # 1,3


def setDifference(a,b):
    var = [x for x in a if x not in b]
    return var

print setDifference(a,b) # 1,3
print setDifference(b,a) # 4,5

def symmetric(a,b):
    var = setDifference( union(a,b), intersection(a,b) )
    return var

print symmetric(a,b) # 1,3,4,5
print symmetric(c,b) # 1,2,3,4,5,6
print symmetric(a,c) # 2,6

def cartesian(a,b):
    var = [ [x, y] for x in a for y in b]
    return var

print cartesian(a,b) # [1,2], [1,4], [1,5], [2,2], [2,4], [2,5], [3,2], [3,4], [3,5]
