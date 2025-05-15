from collections import defaultdict
import re
# dict = { "name": 'sushil' , "age":'35' , "company":'bmc' , "dept":'computers'}
#
# # print (dict["name"])
#
# x= dict.get("name")
# # print(x)
#
# keys = dict.keys()
# # print(keys)
#
# values = dict.values()
# # print(values)
#
# # for key in dict:
#     # print( key , dict[key])
# #
# # for key , value in dict.items():
# #      print(f"{key} ,{value}")
#
# # for i in range(len(dict)):
# #      print ( list(dict.items())[i][0] ,list(dict.items())[i][1])
#
# # keys : are like (0,0) , (1,0) , (2,0)
# #values are like (0,1) , (1,1)  , (2,1)
#
# # d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
# #
# # # Adding a new key-value pair
# # d['age'] = '22'
# # # Updating an existing value
# # d['age'] = '25'
# # d[1] = 'truGeeks'
# #
# # print(d)
#
# a = [('a',1),('b',2), ('c',3), ('a',4)]
# # d = defaultdict(list)
# # for k , v in a:
# #           d[k].append(v)
# #           print(f"{k} : {v}")
# d={}
# for k ,v in a:
#      d.setdefault(k , []).append(v)
#
# # print(d)

# keys = ["name", "age", "city"]
# values = ["Alice", 25, "New York"]
#
# # d = zip(keys, values)
# #
# # for k, v in d:
# #      print(k,v)
# # print(d)
#
#
# #d = dict([(k,v) for k,v in zip(keys,values)])
# d= dict(zip(keys,values))
# print(d)\

# d = { key: set() for key in["student" , "teacher"]}
# d["student"] ={1,1,2,3,4,5}
# d["teacher"] = {2,2,4,5,6,7,8}
# print(d)
#
#
# d = defaultdict(set)
# d["student"] |= {1,1,2,3,4,5}
# d["student"] |= {8,9}
# d["teacher"] |= {2,2,4,5,6,7,8}
# print(d)


# Create and write to input.txt
# with open('input.txt', 'w') as f:
#     f.write("name: shakshi\nage: 23\ncountry: India")
#
# # Read the file and create dictionary
# with open('input.txt', 'r') as file:
#     res = {key.strip(): value.strip() for key, value in (line.split(':',1) for line in file)}
#
# print(res)


# text_string = "name: shakshi\nage: 23\ncountry: India"

# text_str_list=re.split(r'[\n]',text_string)
# final_list= []
# for item in text_str_list:
#    lst= re.split(r'[:]', item)
#    final_list.append(lst)
# print(final_list)


# flat_list = []

# for sublist in final_list:
#     for x in sublist:
#         flat_list.append(x)
#
# print(flat_list)

# flat_list = [ x.strip() for item in re.split(r'[\n]',text_string) for x in  re.split(r'[:]', item) ]



# flat_list= [x.strip()  for x in re.split(r'[:]',text_string)]
# print(flat_list)
text_string = "name: shakshi\nage: 23\ncountry: India"
#
# res = {}
# key, value = text_string.split(':',1)
# res[key.strip()] = value.strip()
# # print (f'key {key} value {value}')
# print(res.values())

res = {} # initialize empty dictionary

# Create and write to input.txt
# with open('input.txt', 'w') as f:
#     f.write("name: shakshi\nage: 23\ncountry: India")
#
# # Read and process the file into a dictionary
# with open('input.txt', 'r') as file:
#     for line in file:
#         # print(f' line:{line}')
#         key, value = line.strip().split(':', 1)
#         res[key.strip()] = value.strip()
#
# print(res.keys())

# text_list = [ x.strip() for item in ( re.split(r'[\n]',text_string)) for x in re.split(r'[:]',item)]
# text_list = [ x for item in ( re.split(r'[\n]',text_string)) for x in re.split(r'[:]',item)]
# print(text_list)
# text_dist =dict( zip(text_list[::2] , text_list[1::2]))
# #
# print(text_dist)
# a = ['Bobby', 'Ojaswi']  # name
# b = [('chapathi', 'roti'), ('Paraota', 'Idly', 'Dosa')]  # food
#
# d = { name: food for name,food in zip(a,b)}
# print(d)

# t = "hello word"
#
# res = defaultdict(list)
#
# for w in t.split():
#  res[w[0]].append(w)
#
# print(dict(res))
# a = {'Gfg': 4, 'is': 5, 'best': 9}
# b = [8, 3, 2]
# d =  { keys: {k:v} for keys , (k,v)  in zip(b , a.items())}
#
# c = { keys: {k:v} for keys , (k,v) in zip (b,a.items())}
# print(c)
# ##{8: {‘Gfg’: 4}, 3: {‘is’: 5}, 2: {‘best’: 9}}
d = {"a": 1, "b": 2}

res = d | {"c" : 3}
res = d | {"c": 4}
res = d.update({"c": 6})
print(res)

