import sys
from lib.accountant import Command, Account, Warehouse
from lib.accountant import updateAccountAndWarehouse

command = Command()
account = Account()
warehouse = Warehouse()



# sys.argv = [magazyn.py, plik_wejsciowy, ..., ostatni_element]
def errorsInArgv():
    if len(sys.argv) - 2 == 0:
        print('Podaj czego szukasz w magazynie.')
        return True


def showStock():
    count = 0

    while count < len(sys.argv) - 2:
        try:
            print('{}: {}'.format(
                sys.argv[count+2],
                warehouse.stock[sys.argv[count+2]]
                )
            )
        except KeyError:
            print('{}: brak w magazynie'.format(sys.argv[count+2]))
        count +=1
        

def main():

    if not command.readFromFile():
        return
    
    command.fromSingleInstructions()

    updateAccountAndWarehouse(command, account, warehouse)

    if errorsInArgv():
        return

    showStock()


if __name__ == '__main__':

    main()