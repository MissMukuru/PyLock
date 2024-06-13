'''PASSWORD STRENGTH CHECKER
--------------
------'''
import string
import getpass

def check_password_strength():
    password = getpass.getpass('Enter the password')
    strength = 0
    remarks = " "
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count +=1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            wspace_count += 1
        else:
            special_count += 1
    
    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if wspace_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1

    if strength == 1:
        remarks = ('That\'s a very bad password')
    elif strength == 2:
        remarks('Change this to a better password')
    elif strength == 3:
        remarks('We\'re getting there')
    elif strength == 4:
        remarks("Almost there")
    elif strength == 5:
        remarks('Thats it')

        print("your passsword has: - ")
        print(f'{lower_count} lower case letters')
        print(f'{upper_count} upper case letters')
        print(f'{num_count} digit')
        print(f'{wspace_count}  whitespaces')
        print(f'{special_count} special characters')
        print(f'password_score: {strength / 5}')
        print (f'Remarks: {remarks}')

        def check_password(another_pw = False):
            valid = False
            if another_pw:
                choice = input("Do you want to check another password (y/n): ")
            else:
                choice = input("Do you want to check your passwords strength(y/n): " )
            
            while not valid:
                if choice.lower() == 'y':
                    return True
                elif choice.lower() == 'n':
                    print('Exciting....')
                    return False
                else:
                    print('Invalid input....Please try again')
                    if __name__ == '__main__':
                        print('===== Welcome to Password Strength Checker =====')
                        check_password = check_password()
                        while check_password:
                            check_password_strength()
                            check_pw = check_password(True)





