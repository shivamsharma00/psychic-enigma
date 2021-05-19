# The defaultdict tool is a container in the collections class of Python.
# It's similar to the usual dictionary (dict) container, but the only 
# difference is that a defaultdict will have a default value if that key
# has not been set yet. If you didn't use a defaultdict you'd have to 
# check to see if that key exists, and if it doesn't, set it to what you want.

from collections import defaultdict

d = defaultdict(list)
d['python'].append('awsome')
d['something-relevent'].append('Not relevent')
d['python'].append('language')

for i in d.items():
    print(i)

print(d['python'])

a_count, b_count = map(int, input().strip().split())
a_list = defaultdict(list)
b_list = []

for i in range(a_count):
    a_list[input()].append(i+1)

for i in range(b_count):
    b_list.append(input())

# print(a_list[b_obj])

for b_obj in b_list:
    if b_obj in a_list:
        print(str(a_list[b_obj]))
        # print(' '.join(map(str, a_list[b_obj])))



        