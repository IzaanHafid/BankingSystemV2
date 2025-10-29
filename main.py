import bank
import string

print("Welcome To The Bank")
error = 1

while True:
    print("Actions:\n1. Create Account\n2. Access Account\n3. Leave Bank\n")
    try:
        mmChoice = int(input('> '))
        if mmChoice not in range(1, 4): print("Error: Invalid Option")
        else: error = 0
    except ValueError: print("Error: Invalid Option")

    if mmChoice == 1:
        error = 1
        while error == 1:
            caN = input("Enter Your Name ('back' to go back): ")
            if caN == 'back':
                error = 2
                break
            caNC = input(f"Is your name {caN}?(y/n)\n> ").lower()
            if caNC == 'y': error = 0
            else: print("Try Again")
        if error == 2: continue
        error = 1
        while error == 1:
            caAN = input("Enter Your Account Name ('back' to go back): ")
            if caAN == 'back':
                error = 2
                break
            if len(caAN) >= 16:
                print(f"Error: Account Name is too long (16 characters min. {len(caAN)} characters used.)")
                continue
            if any(ch.isupper() for ch in caAN):
                print(f"Error: Account Name Includes Capital Letters")
                continue
            if any(ch in string.punctuation for ch in caAN):
                print(f'Error: Account Name Includes Special Characters')
                continue
            if ' ' in caAN:
                print(f'Error: Account Name Includes Spaces')
                continue
            caANC = input(f"Is your account name {caAN}?(y/n)\n> ").lower()
            if caANC == 'y': error = 0
            else: print("Try Again")
        if error == 2: continue
        error = 1
        while error == 1:
            caAP = input("Enter Your Account Pin ('back' to go back): ")
            if caAP == 'back':
                error = 2
                break
            if len(caAP) != 4: print("Account PIN must be 4 digits")
            elif any(ch not in [str(x) for x in range(0, 10)] for ch in caAP):
                print("Error: Only Numbers Allowed")
            else: error = 0
        if error == 2: continue
        bank.createAccount(caN, caAN, caAP)
        print(bank.Accounts())
    elif mmChoice == 2:
        accountActions = ['withdraw', 'deposit', 'transfer', 'change account name', 'change account pin', 'delete account']
        error = 1
        while error == 1:
            print("type 'back' to cancel")
            acN = input("Name: ")
            if acN == "back":
                error = 0
                continue
            acAN = input("Account Name: ").lower()
            if acAN == "back": 
                error = 0
                continue
            acAP = input("Account PIN: ")
            if acAP == "back": 
                error = 0
                continue
            if bank.accounts.get(acN, None) == None : print("Invalid Name")
            elif bank.accounts.get(acN, None).get(acAN) == None: print("Invalid Account Name")
            elif bank.accounts.get(acN, None).get(acAN).get("Account Pin") != acAP: print("Invalid Account PIN")
            else: error = 0
        account = bank.accounts.get(acN).get(acAN)
        error = 1
        while error == 1:
            acA = input("Action (help to view actions, finish to go back): ").lower()
            if acA == "finish": 
                error = 0
                continue
            elif acA == "help": print('\n'.join(accountActions))
            else:
                if acA in accountActions: error = 0
                else: print("Invalid Action Choice")
            if acA == 'withdraw':
                error = 1
                while error == 1:
                    try:
                        value = float(input(f"Account Balance: ${account.get('Balance', 0)}\nEnter Withdraw Amount: "))
                    except ValueError:
                        print("Invalid Value")
                        continue
                    if value > account.get('Balance', 0): print("Not Enough Balance")
                    else: error = 0
                print(bank.accessAccount(acN, acAN, acAP, 'withdraw', value))
                print(bank.Accounts(acN, acAN))
            elif acA == 'deposit':
                error = 1
                while error == 1:
                    try:
                        value = float(input(f"Account Balance: ${account.get('Balance', 0)}\nEnter Deposit Amount: "))
                    except ValueError:
                        print("Invalid Value")
                        continue
                    error = 0
                print(bank.accessAccount(acN, acAN, acAP, 'deposit', value))
                print(bank.Accounts(acN, acAN))
            elif acA == 'transfer':
                error = 1
                while error == 1:
                    acN2 = input('Receiving Name: ')
                    acAN2 = input('Receving Account Name: ')
                    try:
                        value = value = float(input(f"Account Balance: ${account.get('Balance', 0)}\nEnter Transfer Amount: "))
                    except ValueError:
                        print("Invalid Amount")
                        continue
                    error = 0
                print(bank.accessAccount(acN, acAN, acAP, 'transfer', value, acN2, acAN2))
                print(bank.Accounts(acN, acAN, acN2, acAN2))
            elif acA == 'change account name':
                error = 1
                while error == 1:
                    nAN = input('Enter New Account Name: ')
                    if len(nAN) >= 16:
                        print(f"Error: New Account Name is too long (16 characters min. {len(nAN)} characters used.)")
                        continue
                    elif any(ch.isupper() for ch in nAN):
                        print(f"Error: New Account Name Includes Capital Letters")
                        continue
                    elif any(ch in string.punctuation for ch in nAN):
                        print(f'Error: New Account Name Includes Special Characters')
                        continue
                    elif ' ' in nAN:
                        print(f'Error: New Account Name Includes Spaces')
                        continue
                    else: error = 0
                print(bank.accessAccount(acN, acAN, acAP, 'changeAccName', nAN))
                acN = nAN
                print(bank.Accounts(acN, acAN))
            elif acA == 'change account PIN':
                error = 1
                while error == 1:
                    nAP = input('Enter New Account PIN: ')
                    if len(nAP) != 4:
                        print("New Account PIN must be 4 digits")
                    elif any(ch not in [str(x) for x in range(0, 10)] for ch in nAP):
                        print("Error: Only Numbers Allowed")
                    else: error = 0
                print(bank.accessAccount(acN, acAN, acAP, 'changeAccPIN', nAP))
                print(bank.Accounts(acN, acAN))
            elif acA == 'delete account':
                DC = input(f"Are you sure you want to delete the account '{acAN}'(y/n): ").lower()
                if DC == 'y': print(bank.accessAccount(acN, acAN, acAP, 'delete'))
        
    elif mmChoice == 3: quit()
