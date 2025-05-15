from collections import defaultdict
lst = ['a', 'b', 'a', 'c', 'b', 'd', 'e', 'a']
normal_dict= {}
for i ,val in enumerate(lst):
    if val not in normal_dict:
        normal_dict[val]=[]
    normal_dict[val].append(i)


print(normal_dict)

d = defaultdict(list)
for i ,val in enumerate(lst):
    d[val].append(i)

print(d)