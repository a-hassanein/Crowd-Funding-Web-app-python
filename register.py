import re


class Register:

    def __init__(self):
        pass

    def register(self):

        users = open("users.txt", 'a')

        first_name = input("Please Enter your first name: ")
        while re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})?', first_name) == None:
            first_name = input("Please Enter your first name again: ")

        last_name = input("Please Enter your last name: ")
        while re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})?', last_name) == None:
            last_name = input("Please Enter your last name again: ")

        email = input("Please Enter your email: ")
        # while re.fullmatch('([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', email) == None:
        while re.fullmatch('[a-zA-Z_.0-9]+\@[a-zA-Z]+\.[a-zA-Z]+', email) == None:
            email = input("Please Enter your email again: ")

        password = input("Please Enter your Password: ")
        while re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', password) == None:
            password = input("Please Enter your Password again: ")

        confirm_password = input("Please Enter your confirm Password : ")
        while confirm_password != password:
            confirm_password = input("Dosn't match ,Please Enter your confirm Password again: ")

        mobile_phone = input("Please Enter your Mobile_phone: ")
        if re.fullmatch(r"^\+201[0125][0-9]{13}$", mobile_phone) == None:
            mobile_phone = input("Please Enter your egyption Mobile_phone: ")

        # appand
        user = [first_name, last_name, email, password, mobile_phone]
        users.write(":".join(user)+"\n")