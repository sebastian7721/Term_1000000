import command as cmd


class Lesson:
    name: str
    def __init__(self, name: str):
        self.name = name
    

    def check(self) -> bool:
        return False
    


class Question(Lesson):
    question: str
    correctAnswer: str
    answer: str
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        super().__init__(name=f"q {self.question} - {self.answer}")
        self.correctAnswer = "a"
        self.correctAnswers: list[str] = ["Inside Out 2", "Press the petals.", "A hampster."]
        match self.question:
            case "What is Pixar's biggest success in 2024?":
                self.correctAnswer = self.correctAnswers[0]
            case "How do you drive?":
                self.correctAnswer = self.correctAnswers[1]
            case "What is the best pet to have in new hamsphire?":
                self.correctAnswer = self.correctAnswers[2]

    
    def check(self) -> bool:
        if self.answer == self.correctAnswer:
            return True
        else:
            return False
        
class Book:
    name: str
    story: str
    punctuations: str
    def __init__(self, name, story):
        self.name = name
        self.story = story
        self.punctuations: list[str] = [".", "!", "?"]
    def splitIt(self) -> list[str]:
        newArray: list[str] = []
        current = ""
        for char in self.story:
            current += char
            for punc in self.punctuations:
                if char == punc:
                    newArray.append(current)
                    current = ""
        for line in newArray:
            if line.startswith(" "):
                line.removeprefix(" ")
        return newArray
    def read(self) -> list[Question]:
        myStory = self.splitIt()
        questioned = False
        questions: list[Question] = []
        for line in myStory:
            print(line)
            if line.endswith("?"):
                questioned = True
                question = line
            if questioned:
                myQuestion = Question(question=question, answer=line)
                if myQuestion.answer in myQuestion.correctAnswers:
                    questions.append(myQuestion)
                    questioned = False
        return questions

            
            

class MathLesson(Lesson):
    equation: str
    answer: int
    def __init__(self, equation: str, answer: int) -> None:
        self.equation = equation
        self.answer = answer
        super().__init__(name=f"{self.equation} = {self.answer}")



    def check(self) -> bool:
        if eval(self.equation) == self.answer:
            return True
        else:
            return False



class Driving(Book):
    def __init__(self):
        super().__init__(name="driving", story="Hello. Do you know how to drive? I do. How do you drive? Do you spin the stering wheel? Because that is not how to drive. Can I teach you how? Can I teach you how? Can I teach you how? Can I teach you how? Okay. I wil teach you how to drive. How do you drive? Press the petals.")






class Student(cmd.Command):
    brain: list[Lesson]
    def __init__(self):
        super().__init__(name="student", description="a student", capitalName="Student", version=0.5)
        self.brain: list[Lesson] = []
        self.books: list[Book] = [Driving()]


    def run(self, argv: list[str]):
        super().run(argv=argv)
        userInput = ""
        while userInput != "exit":
            userInput = input("Hello. What do you want to do with me: ")
            match userInput:
                case "math":
                    equation = input("Enter the equation: ")
                    answer = int(input("Enter the answer: "))
                    self.brain.append(MathLesson(equation=equation, answer=answer))
                case "test":
                    correct = 0
                    for lesson in self.brain:
                        check = lesson.check()
                        myName = lesson.name
                        print(myName)
                        if check == True:
                            correct += 1
                    print(f"I got {correct} of {len(self.brain)} questions correct.")



                case "remove":
                    name = input("What is it's name: ")
                    for lesson in self.brain:
                        if lesson.name == name:
                            self.brain.remove(lesson)
            
                case "question":
                    question = input("Enter the question: ")
                    answer = input("Enter the answer: ")
                    self.brain.append(Question(question=question, answer=answer))
                case "read":
                    name = input("What name: ")
                    for book in self.books:
                        if book.name == name:
                           questions = book.read()
                           for question in question:
                               self.brain.append(question)







if __name__ == "__main__":
    student = Student()
    student.run(argv=[])