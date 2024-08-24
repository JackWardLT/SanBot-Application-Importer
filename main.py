import subprocess
from utils import * 


projectPath = input("Path to your projects: ")
print(f"Your new project folder is {projectPath}")

# Remember: Variable will return a CompletedProcess, handle it in the future!
try:
    currentProjects = subprocess.run("dir", capture_output=True, text=True, shell=True, cwd=projectPath)
    print("Select application you want to import to Sanbot: ")
    print(currentProjects.stdout)
    choice = chooseFromList(parseProjectFile(currentProjects.stdout))
    upload(projectPath + "\\" + choice)
except Exception as e: 
    print(f"error: {e}")