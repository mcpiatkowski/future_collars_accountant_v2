import sys
from lib.accountant import Command, Account

command = Command()
command.readFromFile()
command.commandsFromSingleActions()
account = Account()

for singleCommand in command.listOfCommands:
    # singleCommand = [saldo, zmiana_na_koncie, komentarz]
    if singleCommand[0] == 'saldo':    
        account.add(singleCommand[1])
        print('Stan konta: ', account.balance)
    # singleCommand = [zakup, identyfikator, cena_jednostkowa, ilość_sztuk]
    elif singleCommand[0] == 'zakup':
        account.substract(singleCommand[2], singleCommand[3])
        print('Stan konta (zakup): ', account.balance)
    # singleCommand = [sprzedaz, identyfikator, cena_jednostkowa, ilość_sztuk]
    elif singleCommand[0] == 'sprzedaz':
        account.add(singleCommand[2], singleCommand[3])
        print('Stan konta (sprzedaz): ', account.balance)


account.add(int(sys.argv[2]))
print('Stan konta (argv): ', account.balance)
command.listOfCommands.insert(-1, ['saldo', sys.argv[2], sys.argv[3]])
print(command.listOfCommands)

for singleCommand in command.listOfCommands:
    for item in singleCommand:
        print(item)