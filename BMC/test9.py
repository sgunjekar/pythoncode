
people = ['mario', 'BOB', 'John', 'tesla', 'Ravi']
people.sort(key = lambda name: name.lower())
sorted_people = sorted(people)

#people.sort()
people
print(people)
people.sort()
print(sorted_people)


try:
    people.index('marioo')

except ValueError as e:
    print(e)


try:
    f = open('data.txt', 'r')
#    var = datadir


except FileNotFoundError as e:
    print(e)
except FileExistsError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("no matter what i will execute this code")