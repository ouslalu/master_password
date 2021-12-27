# you can encrypt text using from cryptography.fernet import fernet
import getpass
import yagmail
import json

#Funtion to get the master password file
def master_pwd(master_file_name):
    with open(master_file_name) as f:
        master_passwords = f.readlines()
    for line in master_passwords:
        line = line.strip()
        master_gmail, master = line.split("|")
        #print(master_gmail)
        #print(master)
    return (master_gmail, master)

#master_pwd("master.txt")


#function to sned correct password as mail if the user initiate the forget password 
def password_mail(address, body_password):
    receiver = address
    mail_password=input("enter the sender mail password")
    body = body_password
    yag = yagmail.SMTP(user="lokousmanhas@gmail.com", password=mail_password)
    yag.send(
        to=receiver,
        subject="my password reset",
        contents=body
    )



def password(master_file):
    master_gmail, master = master_pwd(master_file)
    permission = int(input("To see your password, press 1 \n To add new passwords, press 2 "))
    trial=0
    while trial < 3:
        if permission  == 1:
            print("you have to enter your master password: ")
            master_password = getpass.getpass("Master Password: ")
            if master_password == master:
                with open("passwords_hub.txt") as f:
                    f_ = f.read()
                password_dict = json.loads(f_)
                print(password_dict)
            else:
                print("You entered a wrong Password: ")
            break
        elif permission == 2:
            print("you have to enter your master password: ")
            master_password = input("Master Password: ")
            if master_password == master:
                with open("passwords_hub.txt") as f:
                    f_ = f.read()
                password_dict = json.loads(f_)
                password_dict_2 = password_dict
                site = input("what is the website name: ")
                if site in password_dict_2.keys():
                    old_site_check = int(input("You have a password saved for this website already. To overwrite,press 1, and to quit press 2: "))
                    if old_site_check == 1:
                        new_password = input("what password do you want to use: ")
                        password_dict_2[site] = new_password
                        new_hub = open("passwords_hub_2.txt","w")
                        new_hub = new_hub.write(json.dumps(password_dict_2))
                        print("Password saved")
                    else:
                        print("Bye")
                        quit()
                else:
                    new_password = input("what password do you want to use: ")
                    password_dict_2[site] = new_password
                    new_hub = open("passwords_hub_2.txt","w")
                    new_hub = new_hub.write(json.dumps(password_dict_2))
                    print("Password saved")
            else:
                print("you entered a wrong password")
            
        else:
            print("You can only select 1 or 2")
        trial+=1
    else:
        retrieval = input("You have exhausted 3 trials. Retrieve password by pressing '1' or quit by pressing 'exit' ")# expand this code such that the user can get their password sent to them in the mail provided when they registered the account(use yagmail)
        if retrieval == "1":
            registered_mail = input("please enter the mail you registered with: ")
            if registered_mail == master_gmail:
                password_mail(registered_mail, master)
                print("Check you mail for the password")
            else:
                print("you do not have a registered account")
                print("************************************")
                print("Bye")
                quit()
        else:
            print("bye")
            quit()
password("master.txt")