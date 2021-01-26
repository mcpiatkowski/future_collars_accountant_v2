import sys
from lib.accountant import Command, Account, Warehouse
from lib.accountant import updateAccountAndWarehouse

command = Command()
account = Account()
warehouse = Warehouse()

command.readFromFile()
command.commandsFromSingleActions()

updateAccountAndWarehouse(command, account, warehouse)

# sys.argv = [przeglad.py, in.txt, index_od, index_do]
for index in range(int(sys.argv[2]), int(sys.argv[3])+1):
    print(command.listOfCommands[index])
