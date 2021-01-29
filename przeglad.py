import sys
from lib.accountant import Command, Account, Warehouse
from lib.accountant import updateAccountAndWarehouse

command = Command()
account = Account()
warehouse = Warehouse()

# sys.argv = [przeglad.py, in.txt, index_od, index_do]
def errorsInArgv():
    if len(sys.argv) < 4:
        print('Za mało argumentów!')
        return True
    if int(sys.argv[2]) < 0 or int(sys.argv[3]) < 0:
        print('Indeksy komend muszą być dodatnie!')
        return True


def whichIsGreater():
    if int(sys.argv[2]) < int(sys.argv[3]):
        scope = range(int(sys.argv[2]), int(sys.argv[3])+1)
    else:
        scope = range(int(sys.argv[3]), int(sys.argv[2])+1)
    return scope


def printHistory(scope):
    try:
        for index in scope:
            print(command.listOfCommands[index])
    except IndexError:
        print('Wprowadzono zbyt szeroki zakres!')


def main():

    if not command.readFromFile():
        return
    
    command.fromSingleInstructions()

    if errorsInArgv():
        return

    scope = whichIsGreater()

    printHistory(scope)
    

if __name__ == '__main__':

    main()