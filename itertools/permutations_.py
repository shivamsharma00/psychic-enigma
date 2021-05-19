# This script contains tutorials of itertools.permutations
# which returns successive r length permutations.
# Also this script is solution to the problem of hackerrank problem.
# Created By : Shivam Sharma
# Created On : 6th May 2021

from itertools import permutations

# Here is tutorials of permutation
print(permutations(['1', '2', '3']))
print('Total Permutations-1 : ', list(permutations(['1', '2', '3'])))
# we will give r wihch means it return permutation of length 2
print('Total Permutations-2 : ', list(permutations(['1', '2', '3'], 2)))
# string as parameter in permutations
print('Total Permutations-3 :', list(permutations('abc', 3)))

# Below is the solution of hackerrank problem
# Give input HACK 2
obj = list(input().split())
permut = sorted(list(permutations(obj[0], int(obj[1]))))

for i in permut:
    for j in i:
        print(j, end='')
    print()

# Permutations care about ordering so it will include both 'AC' and 'CA'
# whereas combinations does not.

