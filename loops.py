# a for loop is used for iterating over a sequence (a list/tuple/a set/ a dictionary or a string)

people = ['John', 'Will', 'janet', 'karen']

# for person in people:
#     print('current person: ',person)

# break out

# for person in people:
#     print('current person: ',person)
#     if person == 'Janet': 
#         break

#continue
# for person in people:
#     if person == 'Janet': 
#         continue
#     print('current person: ',person)

#range
for i in range(len(people)):
    print('Current Person: ', people[i])

for i in range(0, 11):
    print('Number', i)

# While loops execute a set of statments as long as a condition is true

count = 0
while count <= 10:
    print('count: ', count)
    count += 1
