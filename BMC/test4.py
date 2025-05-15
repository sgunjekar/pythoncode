
duplicates =([1, 2, 2, 3, 1])
seen = list(set(duplicates))
print(seen)

seen1 =[]
#for x in duplicates:
#    if  x not in seen1:
#     seen1.append(x)

seen2 = [ seen1.append(x) for x in duplicates if x not in seen1]

print(seen1)
logs = ["INFO Start", "ERROR Disk full", "WARNING CPU high", "ERROR Timeout"]
error_logs = [ x for x in logs if "ERROR" not in x]
print(error_logs)

#Reverse a list without using [::-1] or reverse().
duplicates =([1, 2, 2, 3, 1])
reverse1= []
reverse= [ reverse1.append(duplicates[i]) for i in range(len(duplicates)-1,-1 ,-1 ) ]

print(reverse1)

duplicates =([1, 2, 2, 3, 1])
duplicates_uniq= set(duplicates)
freq= {i: duplicates.count(i) for i in duplicates_uniq}
print(duplicates_uniq)
print(freq)


num  ='hellohowareyou'
items = list(str(num))
#items = ["red", "blue", "red", "green", "blue", "blue"]
items_uniq= set(items)
freq2={i: items.count(i)  for i in items_uniq if items.count(i) >=1}
print(items_uniq)
print(freq2)
