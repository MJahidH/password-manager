from  cryptography.fernet import fernet 



master_pwd = input("Please type your mster password : ")


def view():
    with open("passwords.txt","r") as f:
        for line in f.readlines():
            data =line.rstrip()
            user,passw = data.split("|")
            print(f"User : {user} | Password : {passw}")


def add():
    name = input("Account Name : ")
    pwd = input("Password : ")

    with open("passwords.txt","a") as f:
        f.write(f"{name}|{pwd}\n")


while True : 
    mode = input("Would you like to add a new password or add a new password (view,add), press q to quit? ").lower()

    if mode == "q":
        break 

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode")
        continue 

     





