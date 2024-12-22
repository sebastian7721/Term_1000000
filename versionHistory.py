import command as cmd
import terminal as term



class VersionHistory(cmd.Command):
    def __init__(self, terminal: term.Terminal):
        super().__init__(name="vh", description="displays a version history", capitalName="Version History", version=0.3)
        self.terminal = terminal

    
    def run(self, argv):
        super().run(argv=argv)
        print("Here are all the working commands and the version they were released on: ")
        vhCommands = self.workingCommands
        for command in vhCommands:
            if command.secret == False and self.scope == False:
                vhCommands.remove(command)
        for command in vhCommands:
            message = f"- {command.name} - {command.version}"
            print(message)