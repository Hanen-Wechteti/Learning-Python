# a class is like a blueprint for creatng bjects. An object has properties and methods (functions) associated with it. Almost everything in python is an object

class User:
    # constructor
    def __init__(self, name, email, age) :
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} ,and I am {self.age}'
    
    def has_birthday(self):
        self.age += 1


# to extend class User
class Customer(User):
    def __init__(self, name, email, age, balance) :
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

        super().__init__(name, email, age)  # Appel du constructeur de la classe parente User
        self.balance = balance

    def set_balance(self, balance):
            self.balance = balance

    def greeting(self):
            return f'My name is {self.name} , I am {self.age} and I owe a balane of {self.balance}'
#init user Object
brad = User('Brad smith', 'brad@gmail.com', 37)  
Janet = User('Janet williams', 'janet@gmail.com', 35 )

#edit property
brad.age = 32

print(brad.age)
print(Janet.email)
#  call method hasbirthday

Janet.has_birthday()

# call method
print(Janet.greeting())

#init customer
john = Customer('john Noe', 'john@gmail.com', 40, 0)
john.set_balance(500)

print(john.balance)

print(john.greeting())

# print(john.greeting())