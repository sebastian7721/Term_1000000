


def getinput(prompt: str = "") :

        try :

                value = input(prompt)

        except EOFError :

                value = "exit"

        return(value)