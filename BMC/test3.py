keys = ['a', 'b', 'c']
values = [1, 2, 30]

zip ={ k:v for k,v in zip(keys,values) if v >20}

print(zip)
nums = range(10)

grouped= {x:('even' if x% 2 == 0 else 'odd') for x in nums}
print(grouped)