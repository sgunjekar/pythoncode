
def find_longest_unique_substring(s: str):
    char_list = list(s)
    seen = set()
    substr_dict = {}
    temp_str = ""

    i = 0
    while i < len(char_list):
        char = char_list[i]

        if char not in seen:
            temp_str += char
            seen.add(char)
            i += 1
        else:
            # Store current substring in dict
            substr_dict[len(temp_str)] = temp_str
            # Reset for next substring
            # Start from the next character after first occurrence of repeated char
            first_index = temp_str.index(char)
            i = i - len(temp_str) + first_index + 1
            temp_str = ""
            seen.clear()

    # Handle the last collected substring
    if len(temp_str) > 0:
        substr_dict[len(temp_str)] = temp_str

    # Find max key (longest substring length)
    if substr_dict:
        print(substr_dict)
        max_len = max(substr_dict.keys())
        return max_len, substr_dict[max_len]
    else:
        return 0, ""


# Example
s = "geeksforgeeks"
length, longest = find_longest_unique_substring(s)
print(f"Longest substring: '{longest}' with length: {length}")