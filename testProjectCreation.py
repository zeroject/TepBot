import subprocess
import os

def CreateTestProject(path, solutionName, otherProjects):
    projectName = "test"
    os.chdir(path)
    if os.path.exists(os.path.join(path, projectName)):
        print("A test project allready exists")
        for project in otherProjects:
            giveRefrencestoTestProject = subprocess.run(["dotnet", "add", os.path.join(path, f"{projectName}/{projectName}.csproj"), "reference", project])
        return

    os.mkdir(projectName)
    testProjectProcess = subprocess.run(["dotnet", "new", "xunit", "-n", projectName, "-o", os.path.join(path, projectName)], capture_output=True)
    if testProjectProcess.returncode != 0:
        print(f"Failed to create testProject: {testProjectProcess.stderr.decode()}")
    else:
        print("Test project was created")
        for project in otherProjects:
            giveRefrencestoTestProject = subprocess.run(["dotnet", "add", os.path.join(path, f"{projectName}/{projectName}.csproj"), "reference", project])
        addNuggetPackage = subprocess.run(["dotnet", "add", os.path.join(path, f"{projectName}/{projectName}.csproj"), "package", "Moq"])
        addTestPToSlnProcess = subprocess.run(["dotnet", "sln", os.path.join(path, solutionName), "add", os.path.join(path, f"{projectName}/{projectName}.csproj")], capture_output=True)
        if addTestPToSlnProcess.returncode != 0:
            print(f"Failed to attach Test project to solution: {addTestPToSlnProcess.stderr.decode()}")
        else:
            print("Test project added to solution file")
        