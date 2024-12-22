import os
import command as cmd



class GetPid(cmd.Command):
    def __init__(self):
        super().__init__(name="getpid", description="get process id", capitalName="Get PID", version=0.5)
    

    def run(self, argv: list[str]):
        print(os.getpid())

