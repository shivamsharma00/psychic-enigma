#
#! Sets : unordered, mutable, and no duplicates

mySet = set("Hello")
print(mySet)

myS1 = set()

myS1.add(1)
myS1.add(2)
myS1.add(3)

print(myS1)

print(myS1.pop())
print(myS1)

for x in myS1:
    print(x)

#* UNIONS AND INTERSECION
even = {0, 2, 4, 6, 8}
odd = {1, 3, 5, 7, 9}
prime = {2, 3, 5, 7}

uni = odd.union(even)
print(uni)

inter = odd.intersection(prime)
print(inter)

#* DIFFERENCE
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 4, 10, 11, 12, 13, 14}

diff = setA.difference(setB)
print(diff)

s_diff = setB.symmetric_difference(setA)
print(s_diff)
#! Symmetric difference will give the difference from both the sets

setA.update(setB)
print(setA)
#? It will updata the setA with elements not present in A but in B

setA.intersection_update(setB)  #* only elements present in both the sets
print(setA)

setA.symmetric_difference_update(setB)  #* update the difference of A and B in A
print(setA)

print(setA.issubset(setB))  #* print True if set A is subset of B
print(setA.issuperset(setB))    #* print True if A is superset of B
print(setA.isdisjoint(setB))    #* print True if A does not contain element from B


setC = setA.copy()
#! or
setD = set(setB)
 
fset = frozenset([1, 2, 3, 4, 5])
fset.remove(1)  # give error 



