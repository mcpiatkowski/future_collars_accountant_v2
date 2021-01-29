import sys
from lib.accountant import Command, Account, Warehouse
from lib.accountant import updateAccountAndWarehouse

command = Command()
account = Account()
warehouse = Warehouse()


def main():
    
    if not command.readFromFile():
        return
    
    command.fromSingleInstructions()

    updateAccountAndWarehouse(command, account, warehouse)

    print('Stan konta wynosi: ', account.balance)


if __name__ == '__main__':

    main()