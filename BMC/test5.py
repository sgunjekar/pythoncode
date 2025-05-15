d = {'a': 1, 'b': 2, 'c': 3}

swap = { b : a for a ,b in  d.items()}
#print(swap)

merge = {**d, **swap}
#print(merge)

e = {'x': 1, 'y': 2, 'z': 4}

even = {a : b  for a ,b in e.items() if b%2==0}
#print(even)


d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
merge = {**d1,**d2}
add = {a : b  for a ,b in d1.items() if b%2==0}


scores = {'Alice': 50, 'Bob': 75, 'Charlie': 60}

score_keys = list(scores.keys())
score_values= list(scores.values())
score_values=sorted(score_values)
length = len(score_keys)
max_value= (score_values[length-1])
#max ={k: v for k, v in scores.items() if scores.get(k) == sorted(list(scores.values()))[-1]}
max ={k: v for k, v in scores.items() if scores.get(k) == max(list(scores.values()))}

print(max)

swapped = {k: v for k, v in scores.items() if scores.get(k) == max_value}
#print(swapped)

#print(sorted(list(scores.values()))[-1])