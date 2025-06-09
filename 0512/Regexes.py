import re

emailForm = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$')
phoneForm = re.compile(r'^.*?(0\d{1,2}-\d{3,4}-\d{4}).*$')

class Regex:
    def isEmail(email : str):
        return emailForm.match(email)

    def isPhone(phone : str):
        return phoneForm.match(phone)