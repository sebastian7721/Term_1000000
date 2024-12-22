import command as cmd
import getpass as gp
import socket
from datetime import datetime
from typing import Any
import os


class ChangePrompt(cmd.Command):
    def __init__(self) -> None:
        super().__init__(name="changePrompt", description="changes the command line prompt", capitalName="Change Prompt", version=0.1)
        self.symbol = "*"
        splitArray = os.getcwd().split("/")
        workingDirectory = splitArray[len(splitArray) - 1]
        if workingDirectory == gp.getuser():
            workingDirectory = "~"
        if os.getcwd() == "/":
            workingDirectory = "/"
        self.array: list[str] = [f"{gp.getuser()}@{socket.gethostname().removesuffix(".local")}", {workingDirectory}]
        self.array.append(self.symbol)


    def run(self, argv: list[str]):
        self.array.remove(self.symbol)
        if "%" in argv:
            self.symbol = "%"
        if "*" in argv:
            self.symbol = "*"
        if "<" in argv:
            self.symbol = "<"
        if ">" in argv:
            self.symbol = ">"
        self.array.append("")
        self.array.append(self.symbol)
        prompt_message: str = ""
        for string in self.array:
            for char in string:
                prompt_message += char

            prompt_message += " "
        return prompt_message
