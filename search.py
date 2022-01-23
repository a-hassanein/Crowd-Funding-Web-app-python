class SearchProject:
    def __init__(self):
        pass

    def searchProject(self):
        projectsearch = input("Please enter project name or Start date: ")

        try:
            with open('projects.txt', 'r') as searchproj:
                lines = searchproj.readlines()
                for line in lines:
                    searchcol = line.split(":")

                    if searchcol[0].find(projectsearch) != -1:
                        print(line)
                    elif searchcol[3].find(projectsearch) != -1:
                        print(line)

        except:
            print("Oops! something error")