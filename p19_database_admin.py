#simple password change request with a really bad methodology and code and many faults :D
username = ['Anon','Aero']
password = ['green','plane']

print("welcome to database admin program")
user = input("Please enter your username: ")
pass_user = input("Please enter your password: ")

def password_chck(user,pass_user):
    if(user not in username):
        print("Wrong Username")
    for i in username:
        if(i == user):
            for j in password:
                if(j == pass_user):
                    change_yes_no = input("would you like to change your password? Yes/No ")
                    if(change_yes_no.upper() == "YES"):
                        new_password = input("Enter new password: ")
                        if(len(new_password) < 8 ):
                            print("Password should be greater than 8 characters. Try again")
                            new_password = input("Enter new password: ")
                        
                        pass_user= new_password
                        print("Your new password is {}".format(pass_user))

    
password_chck(user,pass_user)