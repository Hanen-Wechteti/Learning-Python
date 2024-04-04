#exp of a custom module to be imported (this custom function will walidate an email adress)
# re: is a rgular expression

import re

def validate_email(email):
    if len(email) > 7:
        return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email))
