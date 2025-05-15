# Input : [[0, 7, 11], [2, 8, 12], [4, 9, 13], [5, 10, 14]]
# Output: [0, 2, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14])


def merge_sorted_list(lists):
    merged =[]
    # track current index of each list
    point_index = [0] * len(lists)

    while True:
        min_val= None
        min_list_index = -1

        #find the smallest current element from all lists
        for i in range(len(lists)):
            if point_index[i] < len(lists[i]):
                current_val = lists[i][point_index[i]]
                if min_val is None or current_val < min_val:
                    min_val =current_val
                    min_list_index = i


        if min_list_index == -1:
           break
        #add smallest val to result and move point_index frwd
        merged.append(min_val)
        point_index[min_list_index] +=1
    return merged

lists=[[1, 7, 11], [2, 8, 12], [4, 9, 13], [5, 10, 14]]
result = merge_sorted_list(lists)
print(result)

