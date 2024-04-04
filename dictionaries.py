# a dictionary is a collection which is unordered  changeable and indexed

#simple dict

person = {
    'first_name': 'John',
    'last_name' : 'Doe',
    'age': 30
}
# print(person)

#using a constructor
# person = dict(  first_name='John',last_name = 'Doe',age= 30)
# print(person)

#access value
print(person['first_name'])
print(person.get('last_name'))

#add key/value
person['phone'] = '396369'
print(person)

#get keys
print(person.keys())

#get items
print(person.items())

#make copy
person2= person.copy()
person2['city']= 'Boston'
print(person2)

#remove item
del(person['age'])
person.pop('phone')
print(person)

#clear
person.clear()
print(person)

#get length
print(len(person2))

#list dict
people = [
    {'name': 'martha','age':'30'},
    {'name': 'ariana','age':'40'}
]
print(people)