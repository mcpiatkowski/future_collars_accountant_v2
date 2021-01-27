import sys
from lib.accountant import Command, Account, Warehouse
from lib.accountant import updateAccountAndWarehouse

command = Command()
account = Account()
warehouse = Warehouse()

# sys.argv = [saldo.py, in.txt, howMuch, comment]
def errorsInArgv():
    try:
        if len(sys.argv) < 3:
            print('Za mało argumentów!')
            return True
    except IndexError:
        print('Niepoprawnie podane argumenty!')
        return True


def appendArgvToCommands():
    command.listOfCommands.append(
        [
        'saldo', 
        int(sys.argv[2]), 
        sys.argv[3]
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