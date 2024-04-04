1# Json is commonly used with data APIS. Here how we ca, parse JSON in a python directory

import json

# sample JSON

userJSON = '{"first_name": "John", "last_name" :"Doe", "age":"30"}'

#parse json to dict
user = json.loads(userJSON)

print(user)
print(user['first_name'])


# parse a dict to  json
car = {"make": "ford", "model": "Mustang", "year": 1970}
carJson= json.dumps(car)
print(carJson)