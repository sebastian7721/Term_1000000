from typing import List
import command as cmd
import guessingGame as gg
from moonreward import MoonReward
import exit as e
import printWelcomeMessage as pwm
import printWorkingDirectory as pwd
import listD as ls
import prompt as p
import changePrompt
import runPythonFile as rpf
import chdir as cd
import redMarinara as redM
import getpass as gp
import socket as s
import os
import computerNumberGuessingGame as cngg
import random
from subprocess import call
import legendary
from simpleDir import simpleDir
import ipconfig as ipv4
import packagedCommand as pcmd
import student as st
from archery import Archery
from drone import Drone
from getpid import GetPid
from getpids import PID
import socket
from hangman import Hangman
from shooter import Shooter
from timedGuessingGame import GuessingGame2
from gcommand import GamingCommand
from change import *
from codeRunner import *
VERSION: float


class Shell(cmd.Command):
    workingCommands: list[cmd.Command]
    shared: list[cmd.Command]
    name: str
    myVer: float
    promptMessage: str
    gamingCommands: list[GamingCommand]
    istrin: str
    cash: float
    user: str
    usersName: str
    hostname: str
    def __init__(self, workingCommands, shared, name, myVer, promptMessage, istrin: str = "", gamingCommands: list[GamingCommand] = [], user: str = gp.getuser(), hostname: str = socket.gethostname().removesuffix(".local")):
        self.myVer = myVer
        self.user = user
        self.usersName = user
        self.workingCommands = workingCommands
        self.cash = 0.00
        self.hostname = hostname
        self.shared = shared
        self.promptMessage = promptMessage
        self.istrin = istrin
        self.gamingCommands = gamingCommands
        for command in self.gamingCommands:
            self.workingCommands.append(command)
            command.cash = self.cash
        for command in shared:
            self.workingCommands.append(command)
        
        super().__init__(name=name, description=f"runs a {name} shell", capitalName=pwm.PrintWelcomeMessage(version=self.myVer, shell=name, message=self.istrin).getMessage, version=0.1)
        self.workingCommands.insert(0, pwm.PrintWelcomeMessage(version=self.myVer, shell=self.name, message=self.istrin))
        self.workingCommands.insert(1, e.Exit(version=self.myVer, shell=self.name))

    def run(self, argv, dell: bool = False):
        if dell == True:
            super().run(argv=argv)
        elif dell == False:
            self.usersName = input("What is your name? ")
            terminal = Terminal(shell=self.name, realShell=self)
            terminal.run(argv=argv)
    
    def redun(self):
        self.promptMessage = self.promptMessage
    
  
class Ashell(Shell):
    def __init__(self, shared):
        super().__init__(workingCommands=[changePrompt.ChangePrompt(), ipv4.IPV4(), Drone(), GetPid(), PID(), Runner()], shared=shared, name="ash", myVer=0.7, promptMessage=p.Prompt(user=gp.getuser(), hostname=s.gethostname().removesuffix(".local")).prompt, istrin="Ashell rem 204 86. A confirmable user can use it. Nothing is good for everything if it has a bait. ASH, The a shell does not have a lot of games. You are welcome to use ash.")
        self.promptMessage = p.Prompt(user=self.user, hostname=self.hostname).prompt
    def redun(self):
        self.promptMessage = p.Prompt(user=self.user, hostname=self.hostname).prompt

class Oshell(Shell):
    def __init__(self, shared):
        super().__init__(workingCommands=[cngg.ComputerNumberGuessingGame(), st.Student(), Hangman()], shared=shared, name="osh", myVer=0.2, promptMessage=f"{os.getcwd()} - {gp.getuser()} on {s.gethostname().removesuffix(".local")} * ", istrin="Gaming O Shell with many games, and a student. You are welcome to use this shell. Play every game and test it out! This is the best OSHELL EVER!", gamingCommands=[Shooter(), Archery()])
        

    def redun(self):
        self.promptMessage = f"{os.getcwd()} - {self.user} on {self.hostname} * "


class Eggshell(Shell):
    def __init__(self, shared):
        super().__init__(workingCommands=[cngg.ComputerNumberGuessingGame(), Runner(), st.Student(), MoonReward()], shared=shared, name="eggshell", myVer=0.1, promptMessage=f"Egg {simpleDir()} at {s.gethostname().removesuffix(".local")} by {gp.getuser()} * ", istrin="EGGS ARE THE BEST FOOD IN THE WORLD! I HOPE YOU HAVE A GREAT TIME IN YOUR TERMINAL EXPIRIENCE. I AM GLAD TO HAVE YOU HERE. Egshell Moon 88", gamingCommands=[Shooter(), Archery()])
    
    def redun(self):
        self.promptMessage = f"Egg {simpleDir()} at {self.hostname} by {self.usersName} ({self.user}) * "





class Mshell(Shell):
    def __init__(self):
        super().__init__(workingCommands=[], shared=[], name="msh", myVer=0.1, promptMessage=f"{gp.getuser()}@{s.gethostname().removesuffix(".local")} {os.getcwd().split("/")[len(os.getcwd().split("/")) - 1]} %" )

    def redun(self):
        self.promptMessage = f"{gp.getuser()}@{s.gethostname().removesuffix(".local")} {os.getcwd().split("/")[len(os.getcwd().split("/")) - 1]} % "
class Terminal(cmd.Command):
    nonCommand: cmd.Command
    workingCommands: list[cmd.Command] = []
    shellName: str
    shared: list[cmd.Command]
    shell: Shell
    packagedCoommands: list[pcmd.PackagedCommand]

    def __init__(self, shell: str = "", realShell: Shell = Shell(workingCommands=[], shared=[], name="SHELL", myVer=0.1, promptMessage="atoe 445 ")) -> None:
        self.shellName = realShell.name
        self.shell = realShell
        self.shellCommands: list[cmd.Command] = [Shooter(cash=0.0), Hangman(), PID(), GetPid(), Drone(), Archery(), st.Student(), ipv4.IPV4(), cngg.ComputerNumberGuessingGame(), Runner()]
        self.nonCommand = cmd.Command(name="nonCommand", description="notta command", capitalName="Boops.", version=0.1)
        self.shared = [gg.GuessingGame(), self.nonCommand, rpf.RunPythonFile(), pwd.PrintWorkingDirectory(), ls.List(), cd.ChangeDirectory(), GuessingGame2()]
        super().__init__(name=self.shellName, description="This is the terminal.", capitalName="Terminal 1000000", version=0.1)
        self.packagedCoommands: list[pcmd.PackagedCommand] = []
        self.scope = False
        if self.shellName == "ash":
            self.shell = Ashell(shared=self.shared)
        if self.shellName == "osh":
            self.shell = Oshell(shared=self.shared)
        self.secretCommands: list[cmd.Command] = []

        if self.shellName == "msh":
            self.shell = Mshell()
        


    

    def printHelp(self, workingCommands: list[cmd.Command]):
        print("Welcome to Term 1000000 help! Here is the list of commands and their description:")
        helpCommands = workingCommands
        for command in helpCommands:
            message = f"- {command.name} - {command.description}"
            print(message)
        print("- install - installs a packaged command")
        print("adsh - adds a shell")
        print("vh - displays a version history")
        print("- login - logs in as a fake user")
    
    def printVersionHistory(self):
        print("Here are all the working commands and the version they were released on: ")
        vhCommands = self.shell.workingCommands
        for command in vhCommands:
            message = f"- {command.name} - {command.version}"
            print(message)

    
    def fullHelp(self):
        self.printHelp()
        print("MEC Terminal 1000000, a shell program by Sebastian Descy")
        print("Shooter game in eggshell. Eggshell egidore assistant.")
        print("Magical Electronic")
    def run(self, argv: list[str]):
        self.shell.run(argv=argv, dell=True)
        self.shell.workingCommands.append(Ashell(shared=self.shared))
        self.shell.workingCommands.append(Oshell(shared=self.shared))
        self.shell.workingCommands.append(Mshell())
        self.shell.workingCommands.append(Eggshell(shared=self.shared))
        if "+ya" in argv:
            self.shell.workingCommands.append(redM.RedMarinara())
        if "legendary" in argv:
            self.shell.workingCommands.append(legendary.Legendary())
        command: str = ""
        while command != "exit":
            oldArgv = self.getUserInput()
            commandArgv = self.parse_argv(argv=oldArgv)
            try:
                command = commandArgv[0]
            except IndexError:
                continue
            runnableCommand = self.turnInCommand(command=command, commands=self.shell.workingCommands)
            if command == "changePrompt":
                self.promptMessage = runnableCommand.run(argv=commandArgv)
            else:
                if runnableCommand == self.nonCommand and self.shellName == "msh":
                      call(argv)
                elif runnableCommand == legendary.Legendary():
                    self.scope = runnableCommand.run(argv=commandArgv)
                elif command == "help":
                    self.printHelp(workingCommands=self.shell.workingCommands)
                elif command == "vh":
                    self.printVersionHistory()
                elif command == "login":
                    at = commandArgv[1].split("@")
                    muser = at[0]
                    workingUsers = ["usir/fusire/xoxototo- ", "red/color/rinopass", "cluck/chickenfarm/jjkkoot"]
                    hostname = at[1]
                    password = " "
                    f = 0 
                    for user in workingUsers:
                        spliti = user.split("/")
                        if spliti[0] == muser and spliti[1] == hostname:
                            password = spliti[2]
                            for i in range(1, 10):
                                if f == 0:
                                    guess = gp.getpass()
                                    if guess == password:
                                        self.user = spliti[1]
                                        self.hostname = spliti[2]
                                        f = 1
                elif command == "pirate":
                    print(f"Aye! Aye! {self.shell.usersName}")
                elif command == "install":
                    if len(commandArgv) > 1:
                        installed = commandArgv[1]
                        for packagedCommand in self.packagedCoommands:
                            if packagedCommand.path == installed:
                                self.shell.workingCommands.append(packagedCommand)
                        
                elif command == "adsh":
                    name = input("Enter it's name: ")
                    workingCommandint = int(input("Enter the amount of working commands: "))
                    workingCommands = []
                    self.printHelp(workingCommands=self.shellCommands)
                    for i in range(0, workingCommandint):
                        workingCommands.append(self.turnInCommand(command=input("Enter a command to be in the working commands of your shell: "), commands=self.shellCommands))
                    istrin = input("Enter the first part of the message: ")
                    promptMessage = input("Enter the prompt: ")
                    self.shell.workingCommands.append(Shell(workingCommands, self.shared, name, 0.1, promptMessage, istrin))
                else:
                    runnableCommand.run(argv=commandArgv)
                self.shell.redun()
                
                for acommand in self.shell.gamingCommands:
                    myCommand = self.turnInCommand(command=acommand.name, commands=self.shell.workingCommands)
                    self.shell.gamingCommands = changeCommand(e=acommand,  b=myCommand, myList=self.shell.gamingCommands)
                    if myCommand in self.shell.workingCommands:
                        self.shell.workingCommands.remove(myCommand)
                for fcommand in self.shell.gamingCommands:
                    if fcommand.gamePlayed == True:
                        self.shell.cash += fcommand.currentCash
                        fcommand.cash = self.shell.cash
                    self.shell.workingCommands.append(fcommand)
    def getUserInput(self) -> List[str]:
        try:
            newInput = input(self.shell.promptMessage)
        except EOFError:
            newInput = "exit"
        argv = newInput.split(" ")
        return argv
                
    def turnInCommand(self, command: str, commands: list[cmd.Command]):
        for indexCommand in commands:
            if indexCommand.name == command:
                return indexCommand
        newCommand = self.nonCommand
        return newCommand
    
    



    



         
if __name__ == "__main__":
    terminal = Terminal()
    terminal.run(argv=[])