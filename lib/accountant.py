import sys

class Command:


    def __init__(self):
        self.listOfSingleActions = []
        self.listOfCommands = []


    def readFromFile(self):
        try:
            with open(sys.argv[1]) as input_as_list:
                for row in input_as_list:
                    row = row.strip()
                    self.listOfSingleActions.append(row)
            return True
        except FileNotFoundError:
            print('Nie znaleziono pliku wejściowego!')
            return False


    def asSingleInstructionsToInputFile(self):
        with open(sys.argv[1], 'w') as output_file:
            for singleCommand in self.listOfCommands:
                for item in singleCommand:
                    output_file.write(str(item) + '\n')


    def fromSingleInstructions(self):
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


class Account:


    def __init__(self):
        self.balance = 0


    def add(self, priceForSingle, howMany = 1):
        self.balance += priceForSingle * howMany
        

    def substract(self, priceForSingle, howMany):
        self.balance -= priceForSingle * howMany


class Warehouse:


    def __init__(self):
        self.stock = {}

    
    def addToStock(self, name, howMany):
        if name not in self.stock:
            self.stock[name] = howMany
        else:
            self.stock[name] += howMany

    def substractFromStock(self, name, howMany):
        self.stock[name] -= howMany


def updateAccountAndWarehouse(command, account, warehouse):
    for singleCommand in command.listOfCommands:
        # singleCommand = [saldo, zmiana_na_koncie, komentarz]
        if singleCommand[0] == 'saldo':    
            account.add(singleCommand[1])
        # singleCommand = [zakup, identyfikator, cena_jednostkowa, ilość_sztuk]
        elif singleCommand[0] == 'zakup':
            account.substract(singleCommand[2], singleCommand[3])
            warehouse.addToStock(singleCommand[1], singleCommand[3])
        # singleCommand = [sprzedaz, identyfikator, cena_jednostkowa, ilość_sztuk]
        elif singleCommand[0] == 'sprzedaz':
            account.add(singleCommand[2], singleCommand[3])
            warehouse.substractFromStock(singleCommand[1], singleCommand[3])



