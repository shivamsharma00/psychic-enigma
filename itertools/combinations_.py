# This script have tutorials about itertools.combinations.
# This library returns list of all the combinations possible.
# Also this script solve the hackerrank challenge of iertools.combinations.
# Created By : Shivam Sharma
# Created On : 6th May 2021

from itertools import combinations

# Here parameter 2 ensures that no combination should be greater than 2
print("Combinations-1 :", list(combinations('12345', 2)))
# Another way to give input
A = [1, 1, 3, 3, 3]
print("Combinations-2 :", list(combinations(A, 4)))

# Here is the HackerRank Problem
# We have to take a string and a number and print sorted combinations 
# upto the number given.
# give input HACK 2
s, num = input().split()
for i in range(int(num)):
    for j in list(combinations(sorted(s), i+1)):
        print("".join(j))
        