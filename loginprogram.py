# this is a log in program
# created by xyznsw, on 12-11-2023
# version 1.0


import random
import string
import time
import os

# set file path
os.chdir('C:/Coding/pythonproject/tafe_soa')

# define variables
username=''
password=''
first_reply=''
new_password=''

# define system administration username and password
admin_username='admin1'
admin_password='admin1'

# get the program start time
time_start=time.time()


# a - log in function
def login_fn():
    global first_reply
    print("Your menu choice was - ", first_reply)
    print("Welcome to login function\n")

    # read accounts information and store it in acc_info
    acc_info = open('accounts.txt')
    acc_info = acc_info.read()
    acc_info = acc_info.split('\n')

    # user input username and password
    username=input('please enter your username:')

    # define the initial status of login
    login = 0

    # define the number of times of wrong password input
    tries = 0

    while tries<3:
        password=input('please enter your password:')

        # validate username and password, print welcome if log in is successful
        for item in acc_info:
            if username==item.split(',')[0] and password==item.split(',')[1]:
                # if username and password are correct, login status set to 1, tries set to 3, exit to main menu
                login=1
                tries=3
                print('welcome, you are successfully logged in as: '+username+'\n')

        # print error if wrong username or password, maximum 3 chances
        if login==0:
            tries+=1

            # if 3 chances of wrong passwords, exit to main menu
            if tries==3:
                print('you have had 3 wrong passwords, contact administration\n')
            else:
                print('password is incorrect, try again\n')


# b - register function
def reg_fn():
    global first_reply
    print("Your menu choice was - ", first_reply)
    print("Welcome to register new account function\n")

    # enter username and validate

    while True:

        # read accounts information and store it in acc_info
        acc_info = open('accounts.txt')
        acc_info = acc_info.read()
        acc_info = acc_info.split('\n')

        # check if username already exists
        exist_user = 0
        new_username = input('please enter your username to register:')

        for item in acc_info:
            if new_username == item.split(',')[0]:
                exist_user = 1
                break

        if exist_user == 0:
            # check if username between 6 - 12 characters
            if len(new_username)<6 or len(new_username)>12:
                print('username must contain 6 - 12 characters, try again\n')
            else:
                print('your username will be: ' + new_username+'\n')
                break

        else:
            print('the username already exists, please choose another one\n')

    # choose or generate password and validate
    set_password()

    # enter secret question and answer

    print('now you need to set up your secret question and answer, which are used to reset your password')
    sec_que=input('enter your secret question: ')
    sec_ans=input('enter your secret answer: ')

    print('\nyou have successfully registered\n')

    # update accounts file
    acc_info = open('accounts.txt','a') # a - for append and write
    new_account=(new_username+','+new_password+','+sec_que+','+sec_ans+'\n')
    acc_info.write(new_account)
    acc_info.close()


# c - change password function
def chgpw_fn():
    global first_reply
    print("Your menu choice was - ", first_reply)
    print("Welcome to change password function\n")

    # validate username and password
    username = input('please enter your username to change password:')
    password = input('please enter your current password:')

    validate=0

    # read accounts information and store it in acc_info
    acc_info = open('accounts.txt')
    acc_info = acc_info.read()
    acc_info = acc_info.split('\n')

    for item in acc_info:
        if username == item.split(',')[0] and password==item.split(',')[1]:
            validate=1
            break

    # change password
    if validate==1:

        set_password()
        print('your password has been changed\n')

        # update accounts file
        item_new=''
        for item in acc_info:
            item_split=item.split(',')
            if item_split[0]==username:
                item_split[1]=new_password
            item_new += ','.join(item_split)
            item_new += '\n'
        item_new = item_new[:-1]

        acc_info = open('accounts.txt', 'w') # w for delete all the current contents then write
        acc_info.write(item_new)
        acc_info.close()

    else:
        print('error username or password, try again\n')


# d - reset password function
def respw_fn():
    global first_reply
    print("Your menu choice was - ", first_reply)
    print("Welcome to reset password function\n")

    # enter username and check if registered
    acc_info = open('accounts.txt')
    acc_info = acc_info.read()
    acc_info = acc_info.split('\n')

    exist_user = 0
    res_sec_que = ''
    res_sec_ans = ''

    res_username = input('please enter your username for reset password:')
    for item in acc_info:
        if res_username == item.split(',')[0]:
            exist_user = 1
            res_sec_que = item.split(',')[2]
            res_sec_ans = item.split(',')[3]
            break

    # if registered display secret question and ask for answer
    if exist_user == 1:
        print('your secret question is:', res_sec_que, '\n')
        sec_answer=input('please input your secret answer:')

        # if secret answer is correct, run the password function
        if sec_answer==res_sec_ans:
            print('your secret answer is correct\n')
            set_password()
            print('your password has been changed\n')

            # update accounts file
            item_new=''
            for item in acc_info:
                item_split=item.split(',')
                if item_split[0]==res_username:
                    item_split[1]=new_password
                item_new += ','.join(item_split)
                item_new += '\n'
            item_new=item_new[:-1]

            acc_info = open('accounts.txt', 'w') # w for delete all the current contents then write
            acc_info.write(item_new)
            acc_info.close()

        # if secret answer is wrong, exit to main menu
        else:
            print('your secret answer is wrong, try again\n')

    # if not registered display message and exit to main menu
    else:
        print('error, the user does not exist\n')


# e - view accounts function
def acc_fn():
    global first_reply
    print("Your menu choice was - ", first_reply)
    print("Welcome to view accounts function\n")

    username=input('to view all account details, please enter your username for the admin: ')
    password=input('please enter your password for the admin: ')

    if username==admin_username and password==admin_password:
        print('\nwelcome, registered accounts are as follows:\n')
        acc_info = open('accounts.txt')
        acc_info = acc_info.read()
        print(acc_info,'\n')

    else:
        print('invalid log in, access denied\n')


# f - exit function
def exit_fn():
    global first_reply
    print("Your menu choice was - ", first_reply)

    time_exit=time.time()
    time_minute,time_second=divmod(time_exit-time_start,60)
    print('you have been using this system for', round(time_minute,1), 'minutes and',round(time_second,1),'seconds')
    print("You are about to exit in 2 seconds\n")
    time.sleep(2)


# define the password function
def set_password():
    global new_password

    while True:

        # choose between own password or random generation
        gen_password = input('please choose to:\n'
                             'a - use your own password\n'
                             'b - generate random password\n')

        if gen_password.lower() == 'a':
            new_password = input('please enter your password:\n')

            # validate new password
            has_digits = 0
            has_upper = 0
            has_lower = 0
            has_punc = 0

            for char in new_password:
                if char in string.digits:
                    has_digits = 1
            for char in new_password:
                if char in string.ascii_uppercase:
                    has_upper = 1
            for char in new_password:
                if char in string.ascii_lowercase:
                    has_lower = 1
            for char in new_password:
                if char in string.punctuation:
                    has_punc = 1

            if len(new_password)<8:
                print('error, password should be minimum 8 characters\n')

            elif has_digits + has_upper + has_lower + has_punc < 3:
                print('error, password must contain at least 3 categories from 0-9, a-z, A-Z, and non-alphanumerics\n')

            else:
                break

        # generate random password
        elif gen_password.lower() == 'b':
            passwordlength = 10
            new_password = ''.join(
                random.choice(string.digits + string.ascii_uppercase + string.ascii_lowercase + string.punctuation) for
                index in range(passwordlength))
            print('your password is:',new_password,'\n')
            break

        else:
            print('error choice, please choose a or b\n')


# define the main menu function
def menu_main(first_reply):
    if first_reply.lower() == "a":
        login_fn()
    elif first_reply.lower() == "b":
        reg_fn()
    elif first_reply.lower() == "c":
        chgpw_fn()
    elif first_reply.lower() == "d":
        respw_fn()
    elif first_reply.lower() == "e":
        acc_fn()
    elif first_reply.lower() == "f":
        exit_fn()
    else:
        print('error, please choose from above options\n')


# start the program

# displays a welcome screen with the date and time at top
print('Welcome to Gelos login program, the current time is', time.ctime())

# start the main menu
while True:
    first_reply = input("Gelos Login Menu - Enter: \n"
                        "a to LOGIN\n"
                        "b to REGISTER NEW ACCOUNT\n"
                        "c to CHANGE PASSWORD\n"
                        "d to RESET PASSWORD\n"
                        "e to VIEW ACCOUNTS\n"
                        "f to EXIT\n")
    menu_main(first_reply)

    if first_reply.lower() == 'f':
        break
