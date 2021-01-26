import sys
from lib.accountant import Command, Account

command = Command()
command.readFromFile()
command.commandsFromSingleActions()
account = Account()

for command in command.listOfCommands:
    # command = [saldo, zmiana_na_koncie, komentarz]
    if command[0] == 'saldo':    
        account.add(command[1])
        print('Stan konta: ', account.balance)
    # command = [zakup, identyfikator, cena_jednostkowa, ilość_sztuk]
    elif command[0] == 'zakup':
        account.substract(command[2], command[3])
        print('Stan konta (zakup): ', account.balance)
    # command = [sprzedaz, identyfikator, cena_jednostkowa, ilość_sztuk]
    elif command[0] == 'sprzedaz':
        account.add(command[2], command[3])
        print('Stan konta (sprzedaz): ', account.balance)


account.add(int(sys.argv[2]))
print('Stan konta (argv): ', account.balance)