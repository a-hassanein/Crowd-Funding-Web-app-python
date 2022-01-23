import datetime

class ProjectList:
    def __init__(self):
        pass

    def projectlist(self):
        projects = open("projects.txt", 'r').readlines()
        projectdata = []


        for prg in projects:
            projectdata = prg.strip()
            projectdata = projectdata.split(":")
            enddatecheck = (datetime.datetime.strptime(projectdata[4], "%Y-%m-%d").date())

            if enddatecheck > datetime.date.today():
                print((prg.strip()).split(":"))