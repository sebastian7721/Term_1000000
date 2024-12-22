import command as cmd



class GamingCommand(cmd.Command):
    currentCash: int
    cash: float
    gamePlayed: bool
    def __init__(self, name: str, description: str, capitalName: str, version: float, secret: bool = False, cash: float = 0.0) -> None:
        super().__init__(name, description, capitalName, version, secret)
        self.currentCash = 0.0
        self.cash = cash
        self.gamePlayed = False
    





