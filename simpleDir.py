import os
import getpass as gp


def simpleDir():
    workingDirectory = os.getcwd().split("/")[len(os.getcwd().split("/")) - 1]
    if workingDirectory == gp.getuser():
        workingDirectory = "~"
    if os.getcwd() == "/":
        workingDirectory = "/"
    return workingDirectory