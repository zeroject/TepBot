import subprocess
import os

def CreateTestProject(path, solutionName):
    projectName = "test"
    os.chdir(path)
    os.mkdir(projectName)
    testProjectProcess = subprocess.run(["dotnet", "new", "xunit", "-n", projectName, "-o", os.path.join(path, projectName)], capture_output=True)
    if testProjectProcess.returncode != 0:
        print(f"Failed to create testProject: {testProjectProcess.stderr.decode()}")
    else:
        print("Test project was created")
        giveRefrencestoTestProject = subprocess.run(["dotnet", "add", os.path.join(path, f"{projectName}/{projectName}.csproj"), "reference"])
        addTestPToSlnProcess = subprocess.run(["dotnet", "sln", os.path.join(path, solutionName), "add", os.path.join(path, f"{projectName}/{projectName}.csproj")], capture_output=True)
        if addTestPToSlnProcess.returncode != 0:
            print(f"Failed to attach Test project to solution: {addTestPToSlnProcess.stderr.decode()}")
        else:
            print("Test project added to solution file")
        