a = {'x': 1, 'y': 2, 'z': 3}
b = {'x': 1, 'y': 9, 'z': 3}

match = { k:v for k,v in a.items() if v in b.values()}

#print(match)



d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
print(sorted(list(d.keys())))
print(sorted(list(d.values())))


# Output: {'i': 3, 'o': 2, 'a': 2, 'e': 2}
text = "Dictionary operations are interesting"
test_list = text.strip().split()
# Output: {'i': 3, 'o': 2, 'a': 2, 'e': 2}
test_list_split = list(str(test_list))


print(test_list_split)
#test_list_split.count('k')
dict_test = [k  for k in test_list_split if k in 'aeiou']
print(dict_test)
dict_test_count = { k: dict_test.count(k) for k in dict_test if k in 'aeiou' }
print(dict_test_count)