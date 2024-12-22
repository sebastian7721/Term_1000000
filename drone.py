import command as cmd
import random
import time



class Drone(cmd.Command):
    def __init__(self):
        super().__init__(name="drone", description="prints letters", capitalName="Drone", version=0.4)
    

    def run(self, argv):
        ints: list[int] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ":", ";", ",", ".", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "🍪", "🛝", "✅", "~", "[", "]", "|", "®", "*", "+", "-", "="]
        length = 0
        if len(argv) > 1:
            for char in argv[1]:
                if char in ints: 
                    length = int(argv[1]) + 1
        if "ao" in argv:
            chars = ["x", "o", "a", "e", "i", "n"]
        for i in range(1, random.randint(1, 100)):
            if length == 0:
                length = random.randint(1, 101)
            string = ""
            for i in range(1, length):
                char = chars[random.randint(0, len(chars) - 1)]
                string += char
            print(string)
            if length > 10000:
                print("Dronerror: Number was too high.")
            time.sleep(0.5)





if __name__ == "__main__":
    drone = Drone()
    drone.run(argv=[])