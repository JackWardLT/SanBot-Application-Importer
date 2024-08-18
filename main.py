import subprocess


projectPath = input("Path to your projects: ")
print("Your new project folder is " + projectPath)

# Remember: Variable will return a CompletedProcess, handle it in the future!
currentProjects = subprocess.run("dir", capture_output=True, text=True, shell=True, cwd=projectPath)

if currentProjects.stdout:
    print("Select application you want to import to Sanbot: ")
    print(currentProjects.stdout)

if currentProjects.stderr:
    print("The command was unsuccsesfull\nError:")
    print(currentProjects.stderr)


