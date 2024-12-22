import random
from time import time
from wordsList import *


class Action:
    def __init__(self):
        pass



    def run(self):
        pass







class BaBaGanoosh(Action):
    def __init__(self):
        pass
    
    def run(self):
        myInput = " "
        score = 0
        print("Welcome to Ba Ba Ganoosh. To exit, type :e")
        while myInput != ":e":
            try:
                myInput = input("Ba Ba Ganoosh: ")
            except EOFError:
                myInput = ":e"
            match myInput:
                case ":ba":
                    print("Welcome to banana mode. To exit, type ;e. To throw a banana, type the word 'throw'.")
                    binput = " "
                    while binput != ';e':
                        try:
                            binput = input("Bannana: ")
                        except EOFError:
                            binput = ";e"
                        if binput == "throw":
                            t  = random.randint(-50, 50)
                            x = random.randint(0, len(wordsList) - 1)
                            r = wordsList[x]
                            print(f"You are aiming at {r}")
                            gainedScore = 0
                            gainedScore += t
                            gainedScore += x
                            score += gainedScore
                            print(f"You earned {gainedScore} points")
                case ":bl":
                    allowedTime = random.randint(60, 180)
                    gainedScore = 0
                    print(f"Welcome to bluberry mode. In this game. You have to keep typing the letter e until time runs out.")
                    eclapsedTime = 0
                    startTime = time()
                    while eclapsedTime <= allowedTime:
                        try:
                            blinput = input("Bluberry: ")
                        except EOFError:
                            break
                        if blinput == "e":
                            gainedScore += 1000
                        endTime = time()
                        eclapsedTime = endTime - startTime
                    score += gainedScore
                    print(f"Game Over. You earned {gainedScore} points.")
        print(f"You earned {score} points this game.")

                            


class ArrangeLetterWords(Action):
    printedWordsLetterArranged: list[str]
    printedWords: list[list[str]]

    def __init__(self):
        self.printedWordsLetterArranged = []
        self.printedWords = wordsList

    def plant(self, letter):
        myArray = []
        for word in wordsList:
            if word.startswith(letter) == True:
                myArray.append(word)
        self.printedWordsLetterArranged.append(" ".join(myArray))
    def run(self):
        alphabet: list[str] = []
        e = int(input("How many prefixes will you put in your library? "))
        for i in range(1, e):
            alphabet.append(input("What letter do you want to add? "))
        for letter in alphabet:
            self.plant(letter)
        for letterWord in self.printedWordsLetterArranged:
            print(letterWord)
        self.printedWordsLetterArranged = []


class CodeInvalid(Action):
    def __init__(self):
        pass

    def run(self):
        print("Invalid Code")

    
class Exit(Action):
    def __init__(self):
        pass
    def run(self):
        print(f"Goodbye!")