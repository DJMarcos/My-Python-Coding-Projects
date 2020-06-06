class User:
    name = "No Name Provided'
    email = ''
    password = '123abcd'
    account_number = 0

class EMployee(User):
    base_pay = 23.00
    department = 'General'

class Customer(User):
    mailing_address = ''
    mailing_list = True
