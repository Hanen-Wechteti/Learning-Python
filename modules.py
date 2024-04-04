# a module is a file containing a set of functions to include in your application. there are core pythn modules,
# modules can be installed by using th pip package manager( including Django) as well as custom modules
 

#core modules

import datetime
from datetime import date
import time 
from time import time


#pip module
import camelcase

# custom modules
import validator
from validator import validate_email



# today = datetime.date.today()
today = date.today()
#print(today)
timestamp=time()
# print(timestamp)

camel= camelcase.CamelCase()
text= 'hello there world'
print(camel.hump(text))

email = 'test@test.com'
if validate_email(email):
    print('email is valid')
else:
    print('not an email')