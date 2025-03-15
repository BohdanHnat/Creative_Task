import sign_in_create_account, homepage

def directory(option):
    match option:
        case '1':
            homepage.main()
        case '2':
            print("Successfully signed out.")
            print('')
            sign_in_create_account.sign_in = False
            sign_in_create_account.sign_into_account()

def main():

    sign_in_create_account.sign_into_account()

    while True:
        print('Welcome to the directory')
        print('')
        print('H -- Homepage')
        print('S -- Sign Out')

        option = str(input('Input: '))

        try:
            directory(option)
        except ValueError:
            print("Please Enter Valid Number")

if __name__ == "__main__":
    main()
