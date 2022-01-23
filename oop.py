import re

from projectlist import ProjectList
from register import Register
from project import Projects
from delete import DeleteProject
from search import SearchProject


# redister function
registerform = Register()


# projects function
projectcall = Projects()


# projects list function
projectlistcall = ProjectList()


# login function
class Login:
    def __init__(self):
        pass

    def login(self):
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
            projectmenucall.project_menu()
        else:
            print("This password dosn't correct")
            mainmenucall.Main_menu()

loginform = Login()

# delete project
deletecall = DeleteProject()

# search project
searchcall = SearchProject()

# Main menu
class Main_menu:
    def choose_menu(self):
        cond = True
        while cond:
            select_menu = input("Pleas Enter 1 for login or 2 for register: ")
            if select_menu == "1":
                loginform.login()
            elif select_menu == "2":
                registerform.register()
            else:
                print("Error input ,Pleas Enter 1 for login or 2 for register")

mainmenucall = Main_menu()



class Project_menu:

    def project_menu(self):
        cond = True
        while cond:
            select_menu = input("Pleas Enter 1 to create project 2 for display current projects and 3 for search project and 4 to delete project: ")
            if select_menu == "1":
                projectcall.projects()
            elif select_menu == "2":
                projectlistcall.projectlist()
            elif select_menu == "3":
                searchcall.searchProject()
            elif select_menu == "4":
                deletecall.deleteProject()
            else:
                print("Error input ,Pleas Enter 1 for display current projects and 2 for search project and 3 to delete project: ")

projectmenucall = Project_menu()




mainmenucall.choose_menu()