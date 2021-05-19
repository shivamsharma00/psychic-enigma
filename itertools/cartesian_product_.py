# This script contains tutorial of itertools.product.
# It returns the cartesian product of list inserted.
# It also include Hackerrank problem.
# Created By : Shivam Sharma
# Created On : 6th May 2021

from itertools import product

# repeat parameter ensures the repeatation of numbers in list
print("Simple with repeat 1: ", list(product([1, 2, 3], repeat=1)))
print("Simple with repeat 2: ", list(product([1, 2, 3], repeat=2)))
print("Simple with repeat 3: ", list(product([1, 2, 3], repeat=3)))
# Following line will return cartesian product between these two lists
print("Between two lists: ", list(product([1, 2, 3], [3, 4])))
# Another method to do cartesian product between two lists
A = [[1, 2, 3], [4, 5, 6]]
# *A provides value at first position and than it takes all other elements
print("Between two lists another method: ", list(product(*A)))

B = [[1, 2], [3, 4], [5, 6]]
print('Between Three lists: ', list(product(*B)))


#* Here is the HackerRank problem, which takes two list and print their
#* their cartesian product
a = list(map(int, input().split()))
b = list(map(int, input().split()))
# print(a)
res = list(product(a, b))
for i in res:
    print(i, end=" ")



