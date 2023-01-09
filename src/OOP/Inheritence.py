class User():
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    def login(self):
        username_input = input("Username: ")
        password_input = int(input("Password: "))
        if (username_input == self.username) and (password_input == self.password):
            print("Your account informations are true")
            return 1
        else:
            print("Your account informations are wrong.")
            return 0

member1 = User("antalya07", "example07@gmail.com", 12345)
member2 = User("ankara06", "example06@gmail.com", 12345)

class Moderator(User):
    def quit(self):
        quest = input("Do you want to log out of the system? (y/h): ")
        if quest == "y":
            passwd = int(input("Verify your password to log out of the system: "))
            if passwd == self.password:
                print("Logged out ...")
            else:
                print("Your password is incorrect, no logout ...")
        elif quest == "h":
            print("You are stuck in the system ...")
        else:
            print("Wrong choice...")

mod1 = Moderator("istanbul34", "example34@gmail.com", 12345)
result = mod1.login()

if result == 1:
    mod1.quit()
else:
    pass