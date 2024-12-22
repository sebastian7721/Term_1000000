import subprocess
import command



class PID(command.Command):
    def __init__(self) -> None:
        super().__init__(name="pids", description="p i d", capitalName="PID im a kid", version=0.6)


    def run(self, argv: list[str]):
        data = subprocess.Popen(['ps'], stdout=subprocess.PIPE).stdout.readlines()
        for dat in data:
            print(dat)



if __name__ == "__main__":
    data = PID()
    data.run(argv=[])