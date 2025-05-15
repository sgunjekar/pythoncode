my_list = [1,2,3,4,5,6,7,8,9,10,'abc']

#reverse_list = my_list[::-1]

split_variable = list(my_list[-1] )
#print(split_variable)
new_list= my_list[:-1]
new_list.extend(split_variable)
#print(new_list)
print(dir(new_list))
concat_list=my_list.__add__(new_list)

my_list.extend(new_list)
my_list.__getitem__(1)
my_list.__setitem__(1,100)
my_list.__len__()
my_list.append('abc')
my_list.pop()
my_list.__iter__()
my_list.__contains__('abc')
#my_list.sort()
x=my_list[:]
print(my_list)
print(x)
a = [1, 2, 3]
b = a
c = a[:]

b.append(4)
c.append(5)

print(a)
print(b)
print(c)
a = [[]] * 3
a[2].append(100)
print(a)
a = ['x', 'y']
a[0] =  'Z'
print(a)
s = "one,two,three"
print(s.split(',')[1][::-1])
line = "  Hello, Python!  "
print(line.strip().split()[1])

lst = ['a', 'b', 'c', 'd', 'e']
print(lst[1:4:2])
data = "a-b-c-d"
print(data.split('-',2))
s = "  spaced   text "
print("-".join(s.strip()))
print("version6")
