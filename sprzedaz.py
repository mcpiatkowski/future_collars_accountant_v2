import sys
from lib.accountant import Command, Account, Warehouse
from lib.accountant import updateAccountAndWarehouse

command = Command()
account = Account()
warehouse = Warehouse()

command.readFromFile()
command.commandsFromSingleActions()

# sys.argv = [sprzedaz.py, in.txt, zakup, name, priceForSingle, howMany]
command.listOfCommands.insert(-1, ['sprzedaz', sys.argv[3], int(sys.argv[4]), int(sys.argv[5])])
updateAccountAndWarehouse(command, account, warehouse)

command.printSingleCommandsLikeInputFile()