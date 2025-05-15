
import re
# s = "Hello!! This is 100% fun."
# # clean = re.sub(r'[^a-zA-Z0-9\s]', '', s)
# # print(clean)  # "Hello This is 100 fun"
#
# clean= re.sub(r'[^a-zA-Z0-9\s]','',s)
#
# print(clean)

#
# text = "Python is simple simple and powerful powerful"
# words = re.findall(r'\b\w+\b' , text.lower())
# #unique = set(words)
# unique = list(dict.fromkeys(words))
# print(unique)  # Removes duplicates in order

# text = "This is is a test test string"
# words = re.findall(r'\b(\w+)\s+\1\b' ,text.lower())
# print(words)
#
# text = "Contact us at test@example.com or fake@.com or john.doe@mail.org"
# # emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b',text)
# # emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)
# # print(emails)  # ['test@example.com', 'john.doe@mail.org']
#
# # text = "apple bananaaaaa apple apple grape banana apple apple "
# # matches = re.findall(r'\bapple\b', text)
# # if len(matches) >= 2:
# #     print("Second 'apple' found!")
# iter_matches =list( re.finditer(r'\b(\w+)\s\1\b', text))
# print(iter_matches)
#
# sorted_words = sorted( iter_matches, key=len , reverse=True)
# # if len(iter_matches) > 1:
# #     print(f'more than two matches {iter_matches[1].group()} at span{iter_matches[1].span()}')
# #
# # positions = [m.start() for m in iter_matches]
# # print("Second match at index:", positions[1])
# # s = "aaabbbccdaa"
# # cleaned = re.sub(r'(.)\1+' , r'\1', s)
# # print(cleaned)
#

lst = [0, 1, False, 2, '', 3, None]
cleaned  = [re.sub(r'[^\w\s]','',str(ls) )for ls in lst]
# cleaned = list(filter(bool, lst))
print(cleaned)  # Output: [1, 2, 3]


a = [10, 20, 30, 40, 50]
b = [1, 2, 3, 4, 5]
c= list[zip(a,b)]
print(c)
