import sys

class Command:


    def __init__(self):
        self.listOfSingleActions = []
        self.listOfCommands = []


    def readFromFile(self):
        with open(sys.argv[1]) as input_as_list:
            for row in input_as_list:
                row = row.strip()
                self.listOfSingleActions.append(row)


    def checkForErrorsinCommand(self):
        pass


    def commandsFromSingleActions(self):
        for index, action in enumerate(self.listOfSingleActions):
            if action == 'saldo':
                self.listOfCommands.append(
                    [
                    self.listOfSingleActions[index], 
                    int(self.listOfSingleActions[index+1]), 
                    self.listOfSingleActions[index+2]
                    ]
                )
            elif action == 'zakup':
                self.listOfCommands.append(
                    [
                    self.listOfSingleActions[index], 
                    self.listOfSingleActions[index+1], 
                    int(self.listOfSingleActions[index+2]), 
                    int(self.listOfSingleActions[index+3])
                    ]
                )
            elif action == 'sprzedaz':
                self.listOfCommands.append(
                    [
                    self.listOfSingleActions[index], 
                    self.listOfSingleActions[index+1], 
                    int(self.listOfSingleActions[index+2]), 
                    int(self.listOfSingleActions[index+3])
                    ]
                )
            elif action == 'stop':
                self.listOfCommands.append(['stop'])


class Account:


    def __init__(self):
        self.balance = 0


    def add(self, howMuch, howMany = 1):
        self.balance += howMuch * howMany
        

    def substract(self, priceForSingle, howMany):
        self.balance -= priceForSingle * howMany
