import sys
from lib.accountant import Command, Account, Warehouse
from lib.accountant import updateAccountAndWarehouse

command = Command()
account = Account()
warehouse = Warehouse()

command.readFromFile()
command.commandsFromSingleActions()

updateAccountAndWarehouse(command, account, warehouse)

# sys.argv = [magazyn.py, plik_wejsciowy, ..., ostatni_element]
count = 0
while count < len(sys.argv) - 2:
    print('{}: {}'.format(
        sys.argv[count+2],
        warehouse.stock[sys.argv[count+2]]
        )
    )
    count +=1
    