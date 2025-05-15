lst = ['abc', 2, 3, 'bcd']

# for item in lst:
#     if isinstance(item, str):
#         (lst[lst.index(item)]) = (list(lst[lst.index(item)]))
#         #print(list(lst[lst.index(item)]))
#     else:
#         pass
# print(lst)
c=[]
for i , item in enumerate(lst):
    if isinstance(item, str):
        lst[i] = list(item)
        c.extend(item)
    else:
        c.append(item)
        pass

print(c)
