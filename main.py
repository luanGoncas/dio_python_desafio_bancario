menu = """

[1] Deposit
[2] Withdraw
[3] Statement
[4] Quit

=> """

balance = 0 # Saldo atual
limit = 500 # Limite diário
statement = "" # Extrato bancário
withdraws_num = 0 # Quantidade de saques realizados
WITHDRAWS_LIMIT = 3 # Limite diário de saques

# Função para retornar o extrato bancário com as operações realizadas
def bank_statement():
    
    # Chamando as variáveis que estão em escopo global
    global balance
    global statement

    current_statement = "\nCurrent Balance: R$ %.2f" % balance

    return statement + current_statement

# Função para depositar o valor
def deposit(value):

    # Chamando as variáveis que estão em escopo global
    global balance
    global statement
    value = round(value, 2)
    previous_result = balance + value

    try:
        if balance > previous_result:
            raise ValueError("Invalid deposit! It must be positive and non-zero.")
        else:
            balance += value
            deposit_message = f"Deposit: R$ {value}\n"
            statement += deposit_message
            return deposit_message
    except:
        return "Invalid operation! The deposit must be positive and non-zero."

# Função para realizar um saque
def withdraw(value):

    # Chamando as variáveis que estão em escopo global
    global balance
    global statement
    global limit
    global withdraws_num
    global WITHDRAWS_LIMIT
    
    value = round(value, 2)
    previous_result = balance - value

    try:
        if value > 0 and previous_result >= 0 and value <= limit:
            balance -= value
            withdraw_message = f"Withdraw: R$ {value}\n"
            statement += withdraw_message
            withdraws_num += 1
            return withdraw_message
        else:
            raise ValueError("Invalid withdraw! Exceeded single withdraw limit, number of daily withdraws reached, or insufficient balance.")
    except:
        return "Invalid operation! Exceeded single withdraw limit, number of daily withdraw limit reached, or insufficient balance."
    
while True:
    option = input(menu)

    if option == "1":
        print("DEPOSIT - Type your deposit value => ", end='')
        try:
            deposit_value = float(input())
            print(deposit(deposit_value))
        except:
            print("Invalid value! Please try again..")
    elif option == "2":
        if withdraws_num == 3:
            print("Daily withdrawal limit reached! Try again tomorrow")
        else:
            print("WITHDRAW - Type your withdraw value => ", end='')
            try:
                withdraw_value = float(input())
                print(withdraw(withdraw_value))
            except:
                print("Invalid value! Please try again...")
    elif option == "3":
        print("STATEMENT - Below is the bank statement:\n")
        print(bank_statement())
    elif option == "4":
        break