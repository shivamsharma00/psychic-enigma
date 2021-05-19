# This script is gives tutorials of combinations with replacement 
# It will let elements repeat themselves.
# Created By : Shivam Sharma
# Created on : 10th May 2021

from itertools import combinations_with_replacement

print(list(combinations_with_replacement('12345', 2)))

s, num = input().split()
for j in list(combinations_with_replacement(sorted(s), int(num))):
    print("".join(j))