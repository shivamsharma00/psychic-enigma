# collections.Counter()
# A counter is a container that stores elements as dictionary keys,
# and their counts are stored as dictionary values.

from collections import Counter

MyList = [1, 1, 1, 4, 4, 5, 5, 7, 7, 7, 4, 4, 2, 2]
print('Output of Counter() - ', Counter(MyList))
print('Output of Counter(list).items() - ', Counter(MyList).items())
print('Output of Counter(list).keys() - ', Counter(MyList).keys())
print('Output of Counter(list).values() - ', Counter(MyList).values())


total_shoe = input()
s_list = Counter(list(map(int, input().strip().split())))
total_money = 0

for i in range(int(input())):
    shoe_size, money = map(int, input().strip().split())
    if shoe_size in s_list.keys() and s_list[shoe_size] > 0:
        total_money = total_money + money
        s_list[shoe_size] -= 1

print(total_money)
