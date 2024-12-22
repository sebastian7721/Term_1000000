from gcommand import GamingCommand
from wordsList import wordsList
import random
import getpass

class Player:
    name: str
    health: int
    wins: int
    def __init__(self, name: str, wins: int = 0, playerHealth: int = 1000):
        self.name = name
        self.health = playerHealth
        self.minStrength = 1
        self.maxStrength = 100
        self.wins = wins
        

    @property
    def strength(self) -> int:
        return random.randint(self.minStrength, self.maxStrength)

    

    def gainHealth(self):
        health =  random.randint(1, 50)
        print(f"{self.name} is gaining {health} health.")
        self.health += health
    

    def getStronger(self):
        addedStrength = random.randint(1, 100)
        print(f"{self.name} is gaining {addedStrength} strength.")
        self.minStrength += addedStrength
        self.maxStrength += addedStrength
    

    def reinit(self, wins: int = 0):
        old = self
        self.__init__(name=old.name, wins=wins)
    







class Shooter(GamingCommand):
    players: list[Player]
    you: Player
    availibleStrings: list[str]
    cash: float
    currentCash: float
    def __init__(self, cash: float = 0.00, wordis: int = random.randint(2, 5), playerHealth: int = 1000) -> None:
        super().__init__("shooter", description="shooter gameo", capitalName="Shooter", version=0.7, cash=cash)
        names = wordsList
        self.players: list[Player] = []
        self.availibleStrings = ["gainHealth", "damage", "getStronger"]
        self.you = Player(name=getpass.getuser(), playerHealth=playerHealth)
        self.players.append(self.you)
        for i in range(1, wordis):
            self.players.append(Player(name=names[random.randint(a=0, b=len(names) - 1)], playerHealth=playerHealth))
    

    def damage(self, player: Player) -> Player:
        damplayer = self.players[random.randint(0, len(self.players) - 1)]
        while damplayer == player:
            damplayer = self.players[random.randint(0, len(self.players) - 1)]
        damage = player.strength
        print(f"{player.name} is attacking {damplayer.name} for {damage}.")
        damplayer.health -= damage
        return damplayer
    

    def play(self) -> Player:
        while len(self.players) != 1:
            for player in self.players:
                if player == self.you:
                    userInput = input("It's your turn! Enter something: ")
                else:
                    userInput = self.availibleStrings[random.randint(0, len(self.availibleStrings)-1)]
                    print(userInput)
                match userInput:
                    case "gainHealth":
                        player.gainHealth()
                    case "damage":
                        damplayer = self.damage(player=player)
                        if damplayer.health <= 0:
                            self.players.remove(damplayer)
                    case "getStronger":
                        player.getStronger()
                        winner = self.players[0]
        if winner == self.you:
            print(f"Congratulations {winner.name}! You win!")
        else:
            print(f"{winner.name} won.")
        return winner
    
    def ranint(self, cash: float = 0.00, amount: int = random.randint(2, 5), playerHealth: int = 1000):
        self.__init__(cash=cash, wordis=amount, playerHealth=playerHealth)



   
    def run(self, argv: list[str]):
        super().run(argv=argv)
        myInput = " "
        gainingCash = 0.0
        while myInput != "exit":
            try:
                myInput = input()
            except EOFError:
                myInput ="exit"
            match myInput:
                case "play":
                    winner = self.play()
                    winner.wins += 1
                    if winner == self.you:
                        gaining = random.uniform(100.00, 200.00)
                        gainingCash += gaining
                        self.cash += gaining
                        print(f"You earned {gaining} cash.")
                    for player in self.players:
                        player.reinit(wins=player.wins)
                    
                case "w":
                    for player in self.players:
                        print(f"{player.name} won {player.wins} times.")
                        

                case "getStronger":
                    approval = input(f"This costs $128.22. Do you want to by it?").casefold()
                    if approval == "yes":
                        if self.cash >= 128.22:
                            gainingCash -= 128.22
                            self.you.getStronger()
                            print(f"Purchased!")
                

                case "balance":
                    print(f"You current balance is {self.cash+gainingCash}.")
                
                
                case "help":
                    print('How to play: Type "play" to play. Type "exit" to exit. Type "damage" to damage a player. Type "getStronger" to get stronger. Type "gainHealth" to gain health. Defeat other players to win. The players are words.')
                
                case "custom":
                    health = int(input("Player health: "))
                    amount = int(input("Amount of players: "))
                    self.ranint(cash=self.cash, amount=amount, playerHealth=health)
            

            self.currentCash = gainingCash
            self.gamePlayed = True
        
                



            
        
        
        








                        
                                    
        


        
        
if __name__ == "__main__":
    shooter = Shooter()
    shooter.run(argv=[])