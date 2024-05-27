import re

# Criar usuário (cliente) - O programa deve armazenar os usuários em uma lista, um usuário
# é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com o
# formato: logradouro - número - bairro - cidade/sigla estado. Deve ser armazenado somente
# os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.

def create_user(name, birth_date, cpf, address, users_added, /):
    try:
        for user in users_added:
            for key, value in user.items():
                if value == cpf:
                    raise Exception('Invalid Operation! User already added!')
        new_user = {
            'Name': name,
            'Birth Date': birth_date,
            'CPF': cpf,
            'Address': address
        }

        users_added.append(new_user)

        return users_added
    except Exception as e:
        print(e.args)
        return users_added

# Criar conta corrente - O programa deve armazenar contas em uma lista. Uma conta é composta
# por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O
# número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence
# somente a um usuário.

def create_current_account(agency, user, existing_accounts, /):
    try:
        for account in existing_accounts:
            if account['Name'] == user:
                raise Exception('Invalid Operation! User already has an account!')
        new_account_number = len(existing_accounts) + 1

        new_account = {
            'Agency': agency,
            'Account Number': str(new_account_number),
            'Name': user
        }

        existing_accounts.append(new_account)

        return existing_accounts
    except Exception as e:
        print(e.args)
        return existing_accounts

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
[4] Create Client
[5] Create Current Account
[6] List Clients
[7] List Current Accounts
[8] Quit

=> """

current_balance = 0 # Saldo atual
LIMIT = 500 # Limite diário
current_statement = "" # Extrato bancário
withdraws_made = 0 # Quantidade de saques realizados
WITHDRAWS_LIMIT = 3 # Limite diário de saques
users_list = [] # Usuários cadastrados
accounts_list = [] # Contas criadas
AGENCY = "0001"

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
        print("CREATE CLIENT ------------ Insert the new client data\n")
        try:
            client_name = input("Insert client's full name: ")

            client_birth_date = input("Insert client's birthdate: (dd/mm/yyyy) ")
            date_regex = re.compile(r'(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}')
            valid_date = date_regex.search(client_birth_date)
            if valid_date == None:
                raise Exception('Invalid Date!')
            
            client_cpf = input("Insert client's CPF: ")
            if len(client_cpf) != 11 and not client_cpf.isdecimal():
                raise Exception('Invalid CPF!')
            
            client_address = input("Now insert the client's address: (Street - Number - Neighborhood - City/State Acronym) ")
            users_list = create_user(client_name, client_birth_date, client_cpf, client_address, users_list)
            print(users_list)
        except Exception as e:
            print(e.args)
    elif option == "5":
        print("CREATE CURRENT ACCOUNT -------------- Inform the new account's owner CPF:\n")
        client_account_cpf = input("We'll check if the user exists: ")
        for user in users_list:
            if client_account_cpf == user['CPF']:
                accounts_list = create_current_account(AGENCY, user['CPF'], accounts_list)
        print(accounts_list)
    elif option == "6":
        print('ALL CLIENTS RELATION:')
        print(users_list)
    elif option == "7":
        print('ALL CURRENT ACCOUNTS RELATION:')
        print(accounts_list)
    elif option == "8":
        break