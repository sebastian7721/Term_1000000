from datetime import datetime
import command as cmd

class PrintWelcomeMessage(cmd.Command):
    myVersion: int
    message: str
    def __init__(self, version, shell, message: str = ""):
        super().__init__(name="printWelcomeMessage", description="prints the welcome message", capitalName="Print Welcome Message", version=0.1)
        self.myVersion = version
        self.message = message
        self.shell = shell


    
    def run(self, argv):
        message = self.getMessage
        underline = self.underline(message=message)
        print(message)
        print(underline)
        
    
    def underline(self, message: str):
        return "=" * len(message)
    

    @property
    def getMessage(self):
        w = datetime.now()
        sting = f"Magical Electronic City (MEC) Terminal 1000000 {self.shell} version {self.myVersion} launched {w.strftime("%Y-%m-%d at %H:%M:%S")}."
        stringes = [sting]
        if self.message != "":
            stringes.insert(0, self.message)
        string = " ".join(stringes)
        
        return string