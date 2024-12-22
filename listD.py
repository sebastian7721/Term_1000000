import os
import printWorkingDirectory as pwd
import command as cmd

class List(cmd.Command):
    def __init__(self):
        super().__init__(name="ls", description="lists all files in working directory", capitalName="List", version=0.1)


    def run(self, argv):
        # folder path
        if len(argv) > 1:
            dir_path = f"{os.getcwd()}/{argv[1]}"
                
        else:
            dir_path = os.getcwd()

        try:
            listedItems = os.listdir(dir_path)
        except FileNotFoundError:
            listedItems = os.listdir(os.getcwd())
        

        # Iterate directory
        for path in listedItems:
            print(path)
       