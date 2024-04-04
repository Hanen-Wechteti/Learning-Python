# Python has functions for creating, reading, updating, and deleting files

# open a file
myFile= open('myfile.txt', 'w')

# get some info

print('name: ', myFile.name)
print('is Closed: ', myFile.closed)
print('Opening mode: ', myFile.mode)

# write to file
myFile.write('I like python')
myFile.write(' and php')
myFile.close()

# Append to file
myFile= open('myfile.txt', 'a')
myFile.write (' I also like mysql')
myFile.close()

# Read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(10)
print(text)
