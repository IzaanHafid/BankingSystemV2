import random as rdm

accounts = {}

def generateCreditCard():
    cc = ''
    for i in range(1, 20):
        if i % 5 == 0: cc += '-'
        else: cc += str(rdm.randint(1, 9))
    return cc

def createAccount(name, accName, accPIN):
    if accounts.get(name) == None:
        accounts[name] = {}
    accounts[name].update({accName : {'Account Pin' : accPIN, 'Credit Card' : generateCreditCard(), 'Balance' : 0.0}})

def accessAccount(name, accName, accPIN, action, value, name2='', accName2=''):
    if accounts.get(name) == None: return "Error: Name Not Found"
    if accounts.get(name).get(accName) == None: return "Error: Account Name Not Found"
    if accounts.get(name).get(accName).get('Account Pin') != accPIN: return "Error: Account PIN Not Correct"

    account = accounts.get(name).get(accName)

    if action == 'withdraw':
        if account.get('Balance') < value: return "Error: Not Enough Balance"

        account['Balance'] -= value
        return f'${value} withdrawn from {accName}.\n{accName} has ${account.get('Balance')} left.'

    elif action == 'deposit':
        account['Balance'] += value
        return f'${value} deposited into {accName}.\n{accName} has ${account.get('Balance')} in total.'
    
    elif action == 'transfer':
        if accounts.get(name).get(accName).get('Balance') < value: return 'Error: Not Enough Balance'
        accounts.get(name).get(accName)['Balance'] -= value
        accounts.get(name2).get(accName2)['Balance'] += value
        return f'''${value} transferred from {accName} to {accName2}.
{accName}: ${accounts.get(name).get(accName).get('Balance')}
{accName2}: ${accounts.get(name2).get(accName2).get('Balance')}'''

    elif action == 'changeAccName':
        prevName = accName
        prevAcc = account

        accounts.get(name).pop(accName)
        accounts[name].update({value : prevAcc})

        return f'The Account {prevName} has been renamed to {value}.'
    
    elif action == 'changeAccPIN':
        prevPin = accPIN
        accounts.get(name).get(accName).update({'Account Pin' : value})
        return f'The PIN for the account {accName} has been changed from {prevPin} to {value}.'
    
    elif action == 'delete':
        accounts.get(name).pop(accName)
        return f'The Account {accName} has been deleted.'

    else: return f'Error: Invalid Action Specified'

def Accounts(pN='null', pAN='null', pN2='null', pAN2='null'):
    output = ""
    output += f"{'Name':15} {'Account':10} {'Pin':12} {'Credit Card':25} {'Balance':10}\n"
    output += "-" * 75 + "\n"
    
    if pN == 'null' or pAN == 'null':
        for name in accounts:
            for accountName in accounts[name]:
                details = accounts[name][accountName]
                output += f"{name:15}{accountName:10}"
                output += f"{details.get('Account Pin',''):12}"
                output += f"{details.get('Credit Card',''):25}"
                output += f"{details.get('Balance',0):10.2f}\n"
    elif pN2 == 'null':
        details = accounts[pN][pAN]
        output += f"{pN:15}{pAN:10}"
        output += f"{details.get('Account Pin',''):12}"
        output += f"{details.get('Credit Card',''):25}"
        output += f"{details.get('Balance',0):10.2f}\n"
    else:
        details = accounts[pN][pAN]
        output += f"{pN:15}{pAN:10}"
        output += f"{details.get('Account Pin',''):12}"
        output += f"{details.get('Credit Card',''):25}"
        output += f"{details.get('Balance',0):10.2f}\n"
        details = accounts[pN2][pAN2]
        output += f"{pN2:15}{pAN2:10}"
        output += f"{details.get('Account Pin',''):12}"
        output += f"{details.get('Credit Card',''):25}"
        output += f"{details.get('Balance',0):10.2f}\n"
    
    return output