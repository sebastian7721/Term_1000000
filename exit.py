import command as cmd
from printWelcomeMessage import datetime



class Exit(cmd.Command):
    myVersion: int
    def __init__(self, version, shell) -> None:
        super().__init__(name="exit", description="exits the terminal", capitalName="Exit", version=0.1)
        self.myVersion = version
        self.shell = shell
    def run(self, argv):
        print("Goodbye! Have a great time!")
        message = f"Terminal 1000000 {self.shell} version {self.myVersion} exited {datetime.now().strftime("%Y-%m-%d at %H:%M:%S")}"
        underline = "=" * len(message)
        print(message)
        print(underline)