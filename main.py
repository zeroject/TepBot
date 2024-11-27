import curses
from os import system
from agent import InitAI

def main():
    system("cls")
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
    InitAI()
    print("Tests created for: " + project)


if __name__ == "__main__":
    main()