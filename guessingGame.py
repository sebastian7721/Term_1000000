import command as cmd
import random



class GuessingGame(cmd.Command):
    min_int: int
    max_int: int

    def __init__(self):
        super().__init__(name="guessingGame", description="runs a guessing game", capitalName="Guessing Game", version=0.1)
        self.min_int = random.randint(1, 30)
        self.max_int = random.randint(self.min_int, 50)
        self.correct_answer = random.randint(self.min_int, self.max_int)

    def run(self, argv):
        super().run(argv=argv)
        self.refresh()
        self.getRange()
        checkForCorrectAnswer = False
        tries = 0
        while checkForCorrectAnswer != True:
            guess = self.getUserGuess()
            checkForCorrectAnswer = self.checkForCorrectAnswer(guess=guess)
            tries += 1
        print(f"You did it in {tries} tries.")

    def getUserGuess(self):
        userInput = input("Guess the number: ")
        integerInput = int(userInput)
        return integerInput

    def checkForCorrectAnswer(self, guess: int) -> bool:
        if guess == self.correct_answer:
            print("You've got it")
            return True
        else:
            print("Try again")
            return False
        
    def getRange(self):
        print(f"I am thinking of a number between {self.min_int} and {self.max_int}.")



if __name__ == "__main__":
    guessingGame = GuessingGame()
    guessingGame.run(argv=[])