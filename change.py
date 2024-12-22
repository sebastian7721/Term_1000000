import command as cmd

def namesList(commandList: list[cmd.Command]) -> list[str]:
    myList = []
    for command in commandList:
        myList.append(command.name)
    return myList
def changeCommand(e: cmd.Command, b: cmd.Command, myList: list[cmd.Command]) -> list[cmd.Command]:
    commandNames = namesList(myList)
    markedIndex = 0
    for command in commandNames:
        if command == e.name:
            myList[markedIndex] = b
    return myList
            

    