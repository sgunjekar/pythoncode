# s = "hello world"
#
# # Use a list comprehension to create a new string by joining
# # characters that are not 'o' from original string 's'
# s = [c for c in s if c != "o"]
# print(s)
# s= ''.join(s)
# print(s)
# a = ['gfg', 'is', 'best', 'for', 'geeks']
#
# # List of characters to check for
# b = ['g', 'e']
# c=[]
# seen= set()
# # for j in range(len(a)):
#     for i in range(len(b)):
#         print(b[i] , a[j] )
#         if b[i] not in (a[j])  :
#             print('no match found appending c now')
#             c.append(a[j])
#             seen.add(a[i])
#         else:
#             print('match found')
#
# print(c)

# for word in a:
# #    for char in b:
#         if all(char not in word for char in b) and word not in seen:
#             print(f'no match found appending c now {word}')
#             c.append(word)
#             seen.add(word)
#
# print(seen)

#
# list1 =  [ word for word in a if all(char not in word for  char in b) ]
# print (list1)
#
# for word in a:
#     for char in b:
#         if char in word:
#             return False
#
# a = ["apple", "banana", "cherry", "date"]
#
# res = []
#
# # for s in a:
# #     res=s[::-1]
# # print(res)
#
#
# res= [ word[::-1] for word in  a]
# print(res)

# a = [[1, 2], [3, 4], [5, 6]]
# b = [[3, 4], [5, 7], [1, 2]]
#
# c = [ word for word in a+b  if char not in word for char in b]
# print(c)
