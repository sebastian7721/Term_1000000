from action import *




class Code:
    code: int
    action: Action
    def __init__(self, action: Action, code: int):
        self.action = action
        self.code = code


    def run(self):
        self.action.run()