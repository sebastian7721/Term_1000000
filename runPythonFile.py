import os
import command as cmd


class RunPythonFile(cmd.Command):
    def __init__(self) -> None:
        super().__init__(name="python3", description="runs a python file", capitalName="Python File", version=0.1)
    

    def run(self, argv: list[str]):
        pythonFilePath = argv[1]
        with open(pythonFilePath) as pythonFile:
            pythonCode = pythonFile.read()
            exec(pythonCode)