
'''
person = {'name':'Gabbar', 'salary': 1000000}
person['innam'] = 1567.777
#print(person['name'])

#print(person.keys())

#loop to get keys
for key in person.keys():
    print(key,person[key])

#loop to get only values
for value in person.values():
    print(value)    


print(sorted(person))

if 'address' in person.keys():
    print("hai")
else:
    print("nahi hai")

del person['innam']
print(person)

'''

list_of_people = [
    {'name':'Gabbar', 'salary': 1000000},
    {'name':'Raka', 'salary': 1000000},
    {'name':'Shaka', 'salary': 1000000}
]

#for item in list_of_people:
#    item['innam'] = str(input(str(item['name'])+"pe kitna innam rakhna hai? "))

print(list_of_people)

new_list = list_of_people.copy()
new_list[0]['name'] = 'Singh'

print(new_list)
print(list_of_people)
print(id(new_list), id(list_of_people))

