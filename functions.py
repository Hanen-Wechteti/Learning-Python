# a function is a bock of code which only runs when it is called In python, we don't use parentheses and curly brackets, we use indentation with tabs or spaces

#create function

def sayHello(name = 'sam'):
    """""
    Prints Hello and then name
    """

    print('hello ' + name)
  
# sayHello('beth')

#return value
def getSum(num1, num2):
    total = num1 + num2
    return total

# print(getSum(4,5))

numSum= getSum(3,6)
print(numSum)


def addOneToNum(num):
    num +=1 
    return num

num = 5
new_num= addOneToNum(num)
print(new_num)


# a lumbda function is a small anonymous function, can take any number of arguments but can only have one expression

getSum = lambda num1, num2 : num1 + num2
print(getSum(9,2))

addOneToNum = lambda num : num + 1
print(addOneToNum(4))

