username = ""

password = ""
password_check = ""

account_names = []
account_passwords = []

signed_in = False

# Creates the account and properly adds them to the list
def create_account():
    global username, password, password_check, account_passwords, account_names

    print("You are on account creation menu")

    while True:

        username = str(input("Please input a username: "))

        if not username:
            print('Please enter an actual username')

        elif username in account_names:
            print('That username is taken, please pick another one')

        else:
            account_names.append(username)

            print('Username successfully added')

            break

    password = str(input('Create a Password: '))

    password_check = str(input('Confirm Password: '))

    while password != password_check:
        print('Passwords did not match, try again')

        password = str(input('Create a Password: '))

        password_check = str(input('Confirm Password: '))

    account_passwords.append(password)

    print('Account creation successful')

# Checks to see if an account exists and checks the password
def sign_into_account():
    global username, password, password_check, account_passwords, account_names, signed_in

    while not signed_in:

        print("You are on Sign In menu")

        username = str(input("Please input a username: "))

        if username not in account_names:
            print("We dont have an account with your username")
            create_account()

        else:
            password = str(input('Please input a password: '))

            account_index = account_names.index(username)

            if password == account_passwords[account_index]:

                print('You have successfully signed into', str(username))

                signed_in = True

            else:
                print(password, account_index)
                print(account_passwords[account_index])

                print('Incorrect Password, try again')