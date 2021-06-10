#
#! lambda arguments : expression

from functools import reduce


def add10(x):
    return x + 10
#! OR
add10 = lambda x : x + 10
print(add10(5))


mult = lambda x, y : x * y
print(mult(5, 10))

points_2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points_2D_sorted = sorted(points_2D)

print(points_2D)
print(points_2D_sorted)

#TODO : Now we will use lambda function to sort according to second element
def sort_by_y(x):
    return x[1]
#! OR
p_2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
# TODO : p_2D_sorted = sorted(p_2D, key = sort_by_y)
p_2D_sorted = sorted(p_2D, key = lambda x : x [1]) 
print(p_2D_sorted)



#! map(func, seq)
a = [1, 2, 3, 4, 5, 6]
b = map(lambda x: x*2, a)
print(list(b))
#? Same thing with list comprehension
c = [x*2 for x in a]
print(c)


#! filter(func, seq)
b = filter(lambda x: x%2==0, a)
print(list(b))
#? same thing with list comprehension
c = [x for x in a if x%2==0]
print(c)


#! reduce(func, seq)
#? reduce function operate repeatedly with given operation 
b = reduce(lambda x, y:x*y, a)
#? above function will do product of elements of list
print(b)
