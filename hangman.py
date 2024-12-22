from wordsList import wordsList
import random
import getpass
import gcommand as gcmd
class Hangman(gcmd.GamingCommand):
    wordsList: list[str]
    def __init__(self) -> None:
        super().__init__(name="hangman", description="hangman game", capitalName="Hangman", version=0.7)
        self.wordsList: list[str] = wordsList


    def listToString(self, s):

        # initialize an empty string
        str1 = ""

        # traverse in the string
        for ele in s:
            str1 += ele

        # return string
        return str1
    
    def draw(self, loss: int):
        match loss:
            case 6:
                print('   __________________')
                print('   |                |')
                print('   |                |')
                print('   |                |')
                print('   |               ( )')
                print('   |                |')
                print('   |            ----|---- ')
                print('   |                |')
                print('   |                |')
                print('   |               / \\')
                print('   |              /   \\')
                print('   |             /     \\')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('  / \\')
                print(' /   \\')
                print('/     \\')
            case 5:
                print('   __________________')
                print('   |                |')
                print('   |                |')
                print('   |                |')
                print('   |               ( )')
                print('   |                |')
                print('   |            ----|---- ')
                print('   |                |')
                print('   |                |')
                print('   |               / ')
                print('   |              /   ')
                print('   |             /     ')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('  / \\')
                print(' /   \\')
                print('/     \\')
            case 4:
                print('   __________________')
                print('   |                |')
                print('   |                |')
                print('   |                |')
                print('   |               ( )')
                print('   |                |')
                print('   |            ----|---- ')
                print('   |                |')
                print('   |                |')
                print('   |                ')
                print('   |                 ')
                print('   |                  ')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('  / \\')
                print(' /   \\')
                print('/     \\')
            case 3:
                print('   __________________')
                print('   |                |')
                print('   |                |')
                print('   |                |')
                print('   |               ( )')
                print('   |                |')
                print('   |                |---- ')
                print('   |                |')
                print('   |                |')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('  / \\')
                print(' /   \\')
                print('/     \\')
            case 2:
                print('   __________________')
                print('   |                |')
                print('   |                |')
                print('   |                |')
                print('   |               ( )')
                print('   |                |')
                print('   |                |')
                print('   |                |')
                print('   |                |')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('  / \\')
                print(' /   \\')
                print('/     \\')
            case 1:
                print('   __________________')
                print('   |                |')
                print('   |                |')
                print('   |                |')
                print('   |               ( )')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('  / \\')
                print(' /   \\')
                print('/     \\')
            case 0:
                print('   __________________')
                print('   |                |')
                print('   |                |')
                print('   |                |')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('   |')
                print('  / \\')
                print(' /   \\')
                print('/     \\')
    


    def play(self) -> bool:
        loss = 0
        word = ""
        win: bool
        wrongLetters = []
        correctWord = self.wordsList[random.randint(0, len(self.wordsList) - 1)]
        for i in range(0, len(correctWord)):
            word += "_"
        while True:
            self.draw(loss=loss)
            print(word)
            print("")
            for wrongLetter in wrongLetters:
                print(wrongLetter)
            
            if loss == 6:
                win = False
                break
            elif word == correctWord:
                win = True
                break
            letter = input("Enter a letter: ")
                    
            a = correctWord.find(letter)
            if a == -1:
                loss += 1
                wrongLetters += letter
            if a >= 0:
                s = list(word)
                s[a] = letter
                word = self.listToString(s)

                         


            
        return win
        
    def run(self, argv: list[str]):
        super().run(argv=argv)
        wins = 0
        losses = 0
        uinput = " "
        currentCash: float = 0.0
        while uinput != "exit":
            try:
                uinput = input()
            except EOFError:
                uinput = "exit"
            if uinput == "play":
                win = self.play()
                if win == True:
                    wins += 1
                    print(f"Congratulations {getpass.getuser()}! You won a game")
                    myCash = random.uniform(1.00, 100.00)
                    print(f"You will earn {myCash} cash.")
                    self.cash += myCash
                    currentCash += myCash
                else:
                    losses += 1
                    print("You snooze, you lose.")
            if uinput == "w":
                print(f"You won {wins} times.")
            if uinput == "l":
                print(f"You lost {losses} times.")
        self.currentCash = currentCash
        self.gamePlayed = True




if __name__ == "__main__":
    game = Hangman()
    game.run(argv=[])