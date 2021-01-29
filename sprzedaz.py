import sys
from lib.accountant import Command, Account, Warehouse
from lib.accountant import updateAccountAndWarehouse

command = Command()
account = Account()
warehouse = Warehouse()

# sys.argv = [sprzedaz.py, in.txt, name, priceForSingle, howMany]
def errorsInArgv():
    try:
        if len(sys.argv) < 5:
            print('Za mało argumentów!')
            return True
        if sys.argv[2] not in warehouse.stock:
            print('Brak w magazynie!')
            return True
        if int(sys.argv[3]) < 0:
            print('Cena musi być dodatnia!')
            return True
        if int(sys.argv[4]) <= 0:
            print('Sprzedawana ilość musi być dodatnia!')
            return True
    except IndexError:
        print('Niepoprawnie podane argumenty!')
        return True

def appendArgvToCommands():
 
    command.listOfCommands.append(
        [
        'sprzedaz', 
        sys.argv[2], 
        int(sys.argv[3]), 
        int(sys.argv[4])
        ]
    )


def main():

    if  not command.readFromFile():
        return

    command.fromSingleInstructions()

    updateAccountAndWarehouse(command, account, warehouse)

    if errorsInArgv():
        return

    appendArgvToCommands()

    command.asSingleInstructionsToInputFile()


if __name__ == '__main__':

    main()