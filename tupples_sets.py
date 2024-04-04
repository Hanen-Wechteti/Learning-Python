# # a tupples is a collection which is ordered and inchangeable. allows dupliacte members.

# #simple tuple
# fruit_tuple = ('apple', 'orange', 'mango')

# # print(fruit_tuple)

# #using constructor

# # fruit_tuple = tuple(('apple', 'orange', 'mango'))

# #get a simple value
# # print(fruit_tuple[1])

# #can not change value
# # fruit_tuple[1] = 'grape'
# # print(fruit_tuple)

# #tuplles with one value should have trailing coma
# fruit_tuple_2= ('apple',)
# print(fruit_tuple_2)

# #get length of tuple
# print(len(fruit_tuple))
# print(len(fruit_tuple_2))

# del fruit_tuple_2


# a set is a collection which is inordered and unindexed. No dupliacte members.

#creat set
fruit_set= {'Apple', 'Orange', 'Mango'}
            
#check if in set 
print('Apple' in fruit_set)

#add to set
fruit_set.add('banane')
print(fruit_set)

#remove from set
fruit_set.remove('banane')
print(fruit_set)

#clear set
fruit_set.clear()
print(fruit_set)

#delete set

del fruit_set
print(fruit_set)