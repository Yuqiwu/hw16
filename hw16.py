a = [1,2,3,4]
b = [2,4,5]

def union(a,b):
    var = [x for x in a + b]
    return var

print union(a,b)

def intersection(a,b):
    var = [x for x in a for y in b if x == y]
    return var 

#print intersection(a,b)

def setDifference(a,b):
    var = [x for x in a if x not in b]
    return var


#print setDifference(a,b)

def symmetric(a,b):
    var = setDifference( union(a,b), intersection(a,b) )
    return var

def cartesian(a,b):
    var = [ [x, y] for x in a for y in b]
    return var

# print cartesian(a,b)
