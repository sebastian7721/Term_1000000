import command as cmd
import random



class MoonReward(cmd.Command):
    books: int
    cards: int
    shells: int
    rocks: int
    rewards: list[str]
    def __init__(self):
        super().__init__(name="moonreward", description="grants rewards that are displayed in a collection. The collection is stored inside this command.", capitalName="moonReward", version=0.1)
        self.rewards = ["books", "cards", "shells", "rocks"]
        self.books = 0
        self.cards = 0
        self.shells = 0
        self.rocks = 0
    

    def run(self, argv: list[str]):
        paramus = argv[1]
        print(f"Welcome to Moon Reward {paramus}.")
        reward = self.rewards[random.randint(0, len(self.rewards)-1)]
        print(f"You earned {paramus} {reward}.")
        match reward:
            case "books":
                self.books += paramus
            case "cards":
                self.cards += paramus
            case "shells":
                self.shells += paramus
            case "rocks":
                self.rocks += paramus


