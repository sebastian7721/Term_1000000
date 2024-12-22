import command as cmd



class PackagedCommand(cmd.Command):
    path: str
    def __init__(self, name: str, description: str, capitalName: str, version: float, path: str):
        super().__init__(name=name, description=description, capitalName=capitalName, version=version)
        self.path = path