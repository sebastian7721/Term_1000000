import command as cmd
import random

class RedMarinara(cmd.Command):
    def __init__(self) -> None:
        super().__init__(name="redMarinara", description="inputs 10 diffrent inputs rolling the correct answer from 1 to 5", capitalName="Red Marinara", version=0.2)

    def run(self, argv):
        score = 0
        super().run(argv=argv)
        for i in range(1, 10):
            correctAnswer = random.randint(1, 5)
            guess = int(input("Guess a  number between 1 and 5: "))
            if guess == correctAnswer:
                score += 1
        print(f"Goodbye! Your score was {score}.")
       
