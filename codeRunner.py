import command as cmd  
from action import *
from codeclass import *


class Runner(cmd.Command):
    def __init__(self):
        super().__init__(name="code", description="runs codes", capitalName="Code Runner", version=0.7)



    def makeCode(self, listOcodes: list[Code], intiger: int):
        for code in listOcodes:
            if code.code == intiger:
                return code
        return Code(CodeInvalid(), 8765432)


    def run(self, argv: list[str] = []):
        super().run(argv=argv)
        listOcodes: list[Code] = [Code(action=BaBaGanoosh(), code=898756), Code(action=Exit(), code=-50), Code(action=ArrangeLetterWords(), code=10100101)]
        myInt = 0
        print(f"Enter (-50) to exit")
        while myInt != -50:
            try:
                myInt = int(input("Enter a code: "))
            except ValueError:
                myInt = 1
            except EOFError:
                myInt = -50
            code = self.makeCode(listOcodes, myInt)
            code.run()
            
