from random import randint, uniform
import getpass
from gcommand import GamingCommand


class Archery(GamingCommand):
    points: int
    minor: int
    def __init__(self):
        super().__init__(name="archery", description="picks a random number to shoot", capitalName="Archery", version=0.4)
        self.points = 0
        self.wins = 0
        self.minor = 0
    
    def sequencity(self, range: range) -> list[int]:
        ar: list[int] = []
        for i in range:
            ar.append(i)
        return ar
    def run(self, argv: list[str]):
        myInput = ""
        sequence = range(0, 105)
        availibleIndexes = self.sequencity(range=sequence)
        tries = 0
        currentCash: float = 0
        while myInput != "exit":
            try:
                myInput = input("What do you want to do? ")
            except EOFError:
                myInput = "exit"
            if myInput == "a":
                points = availibleIndexes[randint(self.minor, len(availibleIndexes) - 1)]
                availibleIndexes.remove(points)
                self.points += points
                tries += 1
                print(f"You just earned {points} points when shooting.")
                if points >= 100:
                    print(f"Congratulations {getpass.getuser()}. You got it in the middle. You won in {tries} tries. New game.")
                    self.wins += 1
                    self.cash += uniform(100.00, 200.00)
                    availibleIndexes = self.sequencity(range=sequence)
                    tries = 0
            if myInput == "p":
                print(f"You earned {self.points} in total.")
            if myInput == "w":
                print(f"You won {self.wins} times.")


            if myInput == "balance":
                print(f"Your balance is {self.cash+currentCash}.")
            
            if myInput == 'm':
                print("This costs 100.22")
                answer = input("BUY IT? ")
                if answer == "yes":
                    if self.cash >= 100.22:
                        currentCash -= 100.22
                        self.minor += 1
        self.currentCash = currentCash
        self.gamePlayed = True




if __name__ == "__main__":
    game = Archery()
    game.run(argv=[])

