import sign_in_create_account, homepage

def directory(option):
    match option:
        case 'H':
            homepage.main()
        case 'S':
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

        if option in ['H', 'S']:
            directory(option)
        else:
            print("Please Enter Valid Option")

if __name__ == "__main__":
    main()
