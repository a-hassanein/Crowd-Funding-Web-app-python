
class DeleteProject:
    def __init__(self):
        pass

    def deleteProject(self):
        projectdel = input("Please enter project name: ")
        try:
            with open('projects.txt', 'r') as delproj:
                lines = delproj.readlines()

                with open('projects.txt', 'w') as fw:
                    for line in lines:
                        delcol=line.split(":")
                        if delcol[0].find(projectdel) == -1:
                            fw.write(line)
            print("Deleted")

        except:
            print("Oops! something error")