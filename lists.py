# a list is a collection which is ordered and changeable. allows dupliacte membeers.

# creat list
numbers = [1, 2 , 3, 4, 5]

# print (type(numbers))
#using constructor
# numbers = list((1, 2, 3, 4, 5))

# print(numbers)
fruits = ['apples', 'oranges', 'grapes', 'pears', 12]

#get values
# print ( fruits[2])

# #get len
# print(len(fruits))

# #append or add something to list
# fruits.append('mangos')
# print(fruits)

# #remove from list
# fruits.remove('grapes')
# print(fruits)

# #insert into specefic position
# fruits.insert(2, 'strawberries')
# print(fruits)

# #remove from specific position
# fruits.pop(3)
# print(fruits)

# #reverse list
# fruits.reverse()
# print(fruits)

# fruits.remove(12)
# print(fruits)

#sort list
fruits.sort()
print(fruits)

#reverse sort
fruits.sort(reverse=True)
print(fruits)
