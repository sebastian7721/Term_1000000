import random
from time import sleep
import command as cmd
import sys


class ComputerNumberGuessingGame(cmd.Command):
    def __init__(self) -> None:
        super().__init__(name="cngg", description="runs a guessing game where the user selects the correct answer and the range", capitalName="Computer Number Guessing Game", version=0.1)


    def run(self, argv):
        super().run(argv=argv)
        eliminatedGuesses: list[int] = []
        startInt: int
        endInt: int
        correctAnswer: int
        tries = 0
        while True:
            vail = False
            try:
                correctAnswer = int(input("Enter the correct answer: "))
            except ValueError:
                print("Value Error: You typed in a not allowed number.")
                correctAnswer = 0
                vail = True
            except EOFError:
                return
            try:
                startInt = int(input("Enter the first number in the range: "))
            except ValueError:
                print("Value Error: You typed in a not allowed number.")
                startInt = random.randint(0, 100)
                print(f"The starting int is {startInt}")
            except EOFError:
                return
            try:
                endInt = int(input("Enter the last number in the range: "))
            except ValueError:
                print("Value Error: You typed in a not allowed number.")
                endInt = random.randint(startInt, 200)
                print(f"The ending int is {endInt}.")
            except EOFError:
                return
            if vail == True:
                correctAnswer = random.randint(startInt, endInt)
                print(f"The correct answer is {correctAnswer}")
            if correctAnswer in range(startInt, endInt):
                break

        guess = startInt
        while guess != correctAnswer:
            guess = random.randint(startInt, endInt)
            print(f"I guessed {guess}")
            eliminatedGuesses.append(guess)
            tries += 1
            sleep(1.0)
        print(f"I did it in {tries} tries")


if __name__ == "__main__":
    cngg = ComputerNumberGuessingGame()
    cngg.run(argv=sys.argv)