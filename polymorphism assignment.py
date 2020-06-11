class User:
    name = "Marcos"
    email = "yolo@gmail.com"
    password = "298ujs"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("welcome back, {}".format(entry_name))
        else:
            print("The password or email is incorrect.")

class Employee(User)
    base_pay = 30.25
    department = "General"
    pin_number = "89030"
    
    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        pin_number = input("Enter your pin: ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("welcome back, {}".format(entry_name))
        else:
            print("The password or email is incorrect.")


class Empolyee2(User)
    base_pay = 12.48
    company = "vending"
    access_pin = "92900"
    
    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        access_pin = input("Enter your pin: ")
        if (entry_email == self.email and access_pin == self.access_pin):
            print("welcome back, {}".format(entry_name))
        else:
            print("The password or email is incorrect.")






customer = User()
customer.getLoginInfo()

manager = Employee()
manger = getLoginInfo()

genator = Empoyee2()
genator = GetLoginInfo
    
