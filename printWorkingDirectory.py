import os
import command as cmd

class PrintWorkingDirectory(cmd.Command):
    def __init__(self):
        super().__init__(name="pwd", description="prints the working directory", capitalName="Print Working Directory", version=0.1)

    def run(self, argv):
        print(os.getcwd())