import sys
from lib.accountant import Command, Account, Warehouse
from lib.accountant import updateAccountAndWarehouse

command = Command()
account = Account()
warehouse = Warehouse()

command.readFromFile()
command.commandsFromSingleActions()

# sys.argv = [zakup.py, in.txt, name, priceForSingle, howMany]
command.listOfCommands.append(
    [
    'zakup', 
    sys.argv[2],
    int(sys.argv[3]), 
    int(sys.argv[4])
    ]
)

updateAccountAndWarehouse(command, account, warehouse)

command.writeSingleCommandsToInputFile()