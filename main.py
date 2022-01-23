import re
import datetime


# redister function
def register():

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



# login function
def login():
    # aya@yahoo.com ,Aya@12345
    userdata = []
    users = open("users.txt", 'r').readlines()

    email = input("Please Enter your email: ")
    while re.fullmatch('[a-zA-Z_.0-9]+\@[a-zA-Z]+\.[a-zA-Z]+', email) == None:
        email = input("Please Enter your email again: ")

    for line in users:
        if email in line:
            userdata = line.split(":")
            break
    # print(userdata)

    password = input("Please Enter your Password: ")
    while re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', password) == None:
        password = input("Please Enter your Password again: ")

    # for pas in userdata:
    if userdata[3] == password:
        project_menu()
    else:
        print("This password dosn't correct")
        choose_menu()



# projects function
def projects():
    projects = open("projects.txt", 'a')

    title = input("Please Enter Project Title: ")
    details = input("Please Enter Project Details: ")
    total_target = input("Please Enter Project Total target: ")

    startyear = int(input('Enter a year'))
    startmonth = int(input('Enter a month'))
    startday = int(input('Enter a day'))
    startdate = datetime.date(startyear, startmonth, startday)

    endyear = int(input('Enter a end year'))
    endmonth = int(input('Enter a end month'))
    endday = int(input('Enter a end day'))
    enddate = datetime.date(endyear, endmonth, endday)



    print(startdate)
    while enddate < startdate or enddate < datetime.date.today():
        endyear = int(input('Enter a year'))
        endmonth = int(input('Enter a month'))
        endday = int(input('Enter a day'))
        enddate = datetime.date(endyear, endmonth, endday)

    # append
    project = [title, details, total_target, str(startdate), str(enddate)]
    print(project)
    projects.write(":".join(project) + "\n")






def projectlist():
    projects = open("projects.txt", 'r').readlines()
    projectdata = []


    for prg in projects:
        projectdata = prg.strip()
        projectdata = projectdata.split(":")
        enddatecheck = (datetime.datetime.strptime(projectdata[4], "%Y-%m-%d").date())

        if enddatecheck > datetime.date.today():
            print((prg.strip()).split(":"))




# Main menu
def choose_menu():
    cond = True
    while cond:
        select_menu = input("Pleas Enter 1 for login or 2 for register: ")
        if select_menu == "1":
            login()
        elif select_menu == "2":
            register()
        else:
            print("Error input ,Pleas Enter 1 for login or 2 for register")

def project_menu():
    cond = True
    while cond:
        select_menu = input("Pleas Enter 1 to create project 2 for display current projects and 3 for search project and 4 to delete project: ")
        if select_menu == "1":
            projects()
        elif select_menu == "2":
            projectlist()
        elif select_menu == "3":
            pass
        elif select_menu == "4":
            pass
        else:
            print("Error input ,Pleas Enter 1 for display current projects and 2 for search project and 3 to delete project: ")

choose_menu()



