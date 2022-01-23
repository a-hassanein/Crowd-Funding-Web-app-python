import datetime


class Projects:
    def __init__(self):
        pass
    def projects(self):
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