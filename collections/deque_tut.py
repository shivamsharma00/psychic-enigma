#
#? A deque is a double-ended queue. 
#? It can be used to add or remove elements from both ends.
#? Deques support thread safe, memory efficient appends and 
#? pops from either side of the deque with approximately the 
#? same O(1) performance in either direction.
#! Created By : Shivam Sharma

from collections import deque

d = deque()
d.append(1)
print(f'After appending 1 : {d}')
d.appendleft(2)
print(d)
d.clear()
print(d)
d.extend('1')
print(d)
d.extendleft('234')
print(d)
d.count('1')
d.pop()
print(d)
d.popleft()
print(d)
d.extend('7896')
print(d)
d.remove('2')
print(d)
d.reverse()
print(d)
d.rotate(3)
print(d)


l2 = deque()
for _ in range(int(input())):
    # l1 = list(input().split(' '))
    cmd, *args = input().split()
    # command, val = input().split()
    # if len(l1) == 1:
    #     if l1[0] == 'pop':
    #         l2.pop()
    #     else:
    #         l2.popleft()
    # else:
    #     if l1[0] == 'append':
    #         l2.append(l1[1])
    #     else:
            # l2.appendleft(l1[1])
    getattr(l2, cmd)(*args)
# print(l2)
# for i in range(len(l2)):
#     print(l2[i], end=' ')
[print(x, end=' ') for x in l2]
print(*[item for item in l2])
# print(i for i in l2)