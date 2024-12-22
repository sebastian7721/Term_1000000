import os
import getpass as gp
import command as cmd

class ChangeDirectory(cmd.Command):
    def __init__(self):
        super().__init__(name="cd", description="changes the working directory", capitalName="Change Directory", version=0.1)
    

    def run(self, argv):
        filePath = argv[1]
        if filePath[0] == "/":
            try:
                os.chdir(filePath)
            except FileNotFoundError:
                print("File not found.")
        elif filePath[0] == "~":
            filePath.removeprefix("~/")
            try:
                os.chdir(f"Users/{gp.getuser()}/{filePath}")
            except FileNotFoundError:
                print("File not found")
        else:
            try:    
                os.chdir(f"{os.getcwd()}/{filePath}")
            except FileNotFoundError:
                print("File not found.")

















