

master_pwd = input("Please type your mster password : ")


def view():
    pass

def add():
    name = input("Account Name : ")
    pwd = input("Password : ")

    with open("passwords.txt","a") as f:
        f.write(f"{name} | {pwd}")


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

     





