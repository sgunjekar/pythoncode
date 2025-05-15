greeting='hello world'
name = 'sushil'
print('{}, {}' .format(greeting,name))
print(f'{greeting.upper()},{name.upper()}')

person = {'name': 'sushil', 'age': 25}

#message= f'{person["name"] } is {person["age"]} years old'
message= '{0[name]} is {0[age]} years old'.format(person)
print(message)

cources = [ 'history' , 'science' , 'maths' , 'compsci' ]

cources.append('art')
cources.insert(0,'science')
cources2= [ 'art' , 'physics']
cources.extend(cources2)
popped = cources.pop()
print(popped)
print(cources[::-1])

print(cources.index('maths'))

final = { index : cource for index , cource in enumerate(cources)  }
print(len(final))

cource_str = '-'.join(cources)

print(cource_str)

cource_set = set(cources)
print(len(cource_set))

cource1_set= { 'history' , 'science' , 'arts' , 'compsci' }
cource2_set= { 'history' , 'hindi' , 'maths' , 'compsci' }
print(cource1_set.difference(cource2_set))