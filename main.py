# Função para realizar um saque. TODOS os parâmetros devem ter seus nomes especificados
def withdraw(*, balance, value, statement, limit, withdraws_num, withdraws_limit):
    value = round(value, 2)
    balance -= value

    try:
        if value <= 0:
            raise ValueError("Invalid withdraw! The number must be positive and non-zero!")
        elif balance < 0:
            raise ValueError("Invalid withdraw! Insufficient balance!")
        elif value > limit:
            raise ValueError("Invalid withdraw! Exceeded single withdraw limit!")
        elif withdraws_num >= withdraws_limit:
            raise ValueError("Invalid withdraw! Number of daily withdraws reached!")
        else:
            statement += f'Withdraw: R$ {value}\n'
            return balance, statement
    except Exception as e:
        return f"Error! {e}"

# Função para depositar o valor. Os parâmetros devem estar na ordem correta
def deposit(balance, value, statement, /):
    value = round(value, 2)

    try:
        if value > 0:
            balance += value
            statement += f"Deposit: R$ {value}\n"
            return balance, statement
        else:
            raise ValueError("Invalid deposit! It must be positive and non-zero.")
    except Exception as e:
        return f"Invalid operation! Missing some parameters or something else! {e}"

# Função para retornar o extrato bancário com as operações realizadas. O saldo deve estar
# na ordem correta.
# O extrato deve ser nomeado.
def bank_statement(balance, /, *, statement):
    return statement + "\n\nCurrent Balance: R$ %.2f" % balance

menu = """

[1] Deposit
[2] Withdraw
[3] Statement
[4] Quit

=> """

current_balance = 0 # Saldo atual
LIMIT = 500 # Limite diário
current_statement = "" # Extrato bancário
withdraws_made = 0 # Quantidade de saques realizados
WITHDRAWS_LIMIT = 3 # Limite diário de saques

while True:
    option = input(menu)

    if option == "1":
        print("DEPOSIT ------- Type your deposit value => ", end='')
        deposit_value = float(input())
        current_balance, current_statement = deposit(current_balance, deposit_value, current_statement)
        print('Current Balance: R$ %.2f' % current_balance)
        print(current_statement)
    elif option == "2":
        if withdraws_made == 3:
            print("Daily withdrawal limit reached! Try again tomorrow.")
        else:
            print("WITHDRAW -------- Type your withdraw value => ", end='')
            withdraw_value = float(input())
            try:
                current_balance, current_statement = withdraw(
                    balance=current_balance,
                    value=withdraw_value,
                    statement=current_statement,
                    limit=LIMIT,
                    withdraws_num=withdraws_made,
                    withdraws_limit=WITHDRAWS_LIMIT
                )
                print('Current Balance: R$ %.2f' % current_balance)
                print(current_statement)
                withdraws_made += 1
            except:
                error = withdraw(
                    balance=current_balance,
                    value=withdraw_value,
                    statement=current_statement,
                    limit=LIMIT,
                    withdraws_num=withdraws_made,
                    withdraws_limit=WITHDRAWS_LIMIT
                )
                print(error)
    elif option == "3":
        print("STATEMENT - Below is the bank statement:\n")
        print(bank_statement(current_balance, statement=current_statement))
    elif option == "4":
        break