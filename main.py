import os
import random
from agent import InitAI
from testProjectCreation import CreateTestProject

def main():
    os.system("cls")
    print("Paste in the path of the sulution file\n")
    path = input()
    path = path.replace('"', "")
    solution = open(path, "r")
    lines = solution.readlines()
    solution.close()
    projects = []
    x = 0
    for project in lines:
        if project.find("Project(") != -1:
            if project.find(".csproj") != -1:
                project = project.split(",")[1].replace(" ", "").replace('"', "").replace("\n", "")
                projects.append(project)
                x += 1
                print(str(x) + ": " + project)
    print("\n\n")
    print("Select the project you want to create a test for")
    selection = input()
    selection = int(selection) - 1
    if selection < 0 or selection >= len(projects):
        print("Invalid selection")
        return
    project = projects[selection]
    print("You selected: " + project)
    CreateTestProject(os.path.dirname(path), os.path.basename(path), projects)
    folder = os.path.dirname(path) + "\\" + project.split("\\")[0]
    os.chdir(folder)
    csFiles = []
    for file in os.listdir():
        if (file.endswith(".cs")):
            csFile = open(f"{folder}\{file}", "r")
            csFileLines = csFile.readlines()
            notInterface = True
            for line in csFileLines:
                if (line.find("interface") != -1):
                    notInterface = False
            if (notInterface):
                csFiles.append(file)
                messageToAi = "\n".join(csFileLines)
                InitAI(messageToAi, os.path.join(os.path.dirname(path), "test/test.csproj"), f"TestingUnit{random.randint(0, 2000)}.cs", projects)
                print(file)
    #InitAI()
    print("Tests created for: " + project)


if __name__ == "__main__":
    main()