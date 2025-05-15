# #Given a string s, find the length of the longest substring without repeating characters.
# s="geeksforgeeks"
# char_list = list(s)
# seen = set()
# substr_dict = {}
# temp_str = ""
# for i in range(len(char_list)):
#     char = char_list[i]
#     if char not in seen:
#         print ( 'not matching')
#         temp_str += char
#         seen.add(char)
#     else:
#         substr_dict[len(temp_str)] = temp_str
#         temp_str = ""
#         seen.clear()
#     print(substr_dict)
# max_val = max(substr_dict.values())
# max_len = max(substr_dict.keys())
# print(f'{max_len}:{max_val}')

s = "geeksforgeeks"
char_list = list(s)
seen = set()
substr_dict = {}
temp_str = ""
i = 0

while i < len(char_list):
    char = char_list[i]
    if char not in seen:
        # print('not matching')
        temp_str += char
        seen.add(char)
        i += 1
    else:
        substr_dict[len(temp_str)] = temp_str
        # Restart the scan just after first occurrence of repeated char
        i = i - len(temp_str) + temp_str.index(char) + 1
        temp_str = ""
        seen.clear()
#    print(substr_dict)

# Add the last collected substring if any
if temp_str:
    substr_dict[len(temp_str)] = temp_str

# Get max
max_len = max(substr_dict.keys())
max_val = substr_dict[max_len]
print(f'{max_len}: {max_val}')

