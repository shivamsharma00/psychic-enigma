# This script contains tutorials of group by module of itertools.
# It also contains HackerRank question
# Created By : Shivam Sharma
# Created On : 11th May 2021
#* https://docs.python.org/2/library/itertools.html#itertools.groupby


from itertools import groupby

groups = []
uniquekeys= []
data = 'ZZDDFGGJHSSUHHS'
data = sorted(data)

print(f'Data after sorting - {data}')

for k, g in groupby(data):
    groups.append(list(g))
    uniquekeys.append(k)
#* Above loop will help to understand groupby
#* It returns groups which we have to convert to list
#* If we will sort list beforehand than all the same element will
#* grouped as an element.
print(f'Groups are : {groups}')
print(f'Unique Key are : {uniquekeys}')


#* HackerRank Problems
#* Sample Input : 1222311
#* Sample Output : (1, 1) (3, 2) (1, 3) (2, 1)
for k, g in groupby(input()):
    this_tuple = (len(list(g)), int(k))
    print(this_tuple, end=" ")
