import command as cmd
import getpass



class Legendary(cmd.Command):
    def __init__(self):
        super().__init__(name="+o", description="legendary passwords", capitalName="???", version=0.3, secret=True)


    
    def run(self, argv) -> bool:
        super().run(argv=argv)
        try:
            input1 = input()
        except EOFError:
            return
        if input1 == "qwerty":
            input2 = input()
            if input2 == "navilar":
                input3 = int(input("Now it has to be an integer: "))
                if input3 == 597:
                    input4 = float(input("Now it has to be a floating point number: "))
                    if input4 == 198.85:
                        input5 = input("And now a string again: ")
                        if input5 == "zziiyth":
                            print(f"Congratulations {getpass.getuser()} You got all the passwords correct. They are always the same. Remember these passwords.")
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False