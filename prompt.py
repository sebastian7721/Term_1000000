import getpass as gp
import socket
from typing import Callable, Dict
from printWorkingDirectory import PrintWorkingDirectory
import datetime as dt
import os
class Prompt:
    prompt_template: str
    keys: dict

    def __init__(self, user: str = gp.getuser(), hostname: str = socket.gethostname().removesuffix(".local")):
        workingDirectory = os.getcwd().split("/")[len(os.getcwd().split("/")) - 1]
        if workingDirectory == gp.getuser():
            workingDirectory = "~"
        if os.getcwd() == "/":
            workingDirectory = "/"
        self.prompt_template = f"{user}@{hostname} {workingDirectory} * "

    
    @property
    def prompt(self) -> str:
        return self.prompt_template
