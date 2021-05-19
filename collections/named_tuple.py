# Basically, namedtuples are easy to create, lightweight object types.
# They turn tuples into convenient containers for simple tasks.
# With namedtuples, you don’t have to use integer indices for accessing members of a tuple.

from collections import namedtuple

Point = namedtuple('Point', 'x, y')
pt1 = Point(1, 2)
pt2 = Point(3, 4)
dot_product = (pt1.x * pt2.x) + (pt1.y * pt2.y)

print(dot_product)

Car = namedtuple('Car', 'Price Mileage Colour Class')
xyz = Car(Price = 100000, Mileage=12, Class='Y', Colour='Cyan')
print(xyz.Class)


# DJ = namedtuple('DJ', 'ID MARKS CLASS NAME')
count = int(input())
sum = 0
fields = input().split()
DJ = namedtuple('DJ', fields)
# a, b, c, d = list(map(str, input().strip().split()))
for i in range(count):
    a1, b1, c1, d1 = map(str, input().strip().split())
    temp = DJ(a1, b1, c1, d1)
    sum += int(temp.MARKS)
    
print('{:.2f}'.format(sum/count))

# print(a)
# print(b)
# print(c)
# print(d)