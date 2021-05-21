# Created By : Shivam Sharma
#? This script contains the tutorial of OrderedDict() of collections
#* An OrderedDict is a dictionary that remembers the order of the keys
#* that were inserted first. If a new entry overwrites an existing entry,
#* the original insertion position is left unchanged. 

from collections import OrderedDict

ordinary_dict = {}
ordinary_dict['a'] = 1
ordinary_dict['d'] = 4
ordinary_dict['c'] = 3
ordinary_dict['b'] = 2
ordinary_dict['a'] = 5

for key, value in ordinary_dict.items():
    print(key, value)

ordered_dict = OrderedDict()

ordered_dict['a'] = 1
ordered_dict['c'] = 3
ordered_dict['b'] = 2
ordered_dict['d'] = 4

print(ordered_dict)

ordered_dict['a'] = 5

print(ordered_dict)

item_dict = OrderedDict()
for _ in range(int(input())):

    l_list = input().split(" ")
    cost = int(l_list[-1])
    name = ' '.join(l_list[:-1])

    item_dict[name] = item_dict.get(name, 0) + cost

    # item_dict[name] += int(cost) if name in item_dict.keys() else item_dict[name] = int(cost)
    #  if name in item_dict.keys():
    #     item_dict[name] += int(cost)
    # else:
    #     item_dict[name] = int(cost)
    
# for k, v in item_dict.items():
print(f'{k} {v}' for k, v in item_dict.items())