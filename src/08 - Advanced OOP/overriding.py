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
    def __init__(self, username, email, password, api):
        super().__init__(username, email, password)
        self.api = api
    def panel(self):
        input1 = int(input("Insert your API Key to access to the Admin Panel: "))
        if input1 == self.api:
            print("Access Granted.")
            return 1
        else:
            print("Acess Denied.")
            return 0
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

mod1 = Moderator("istanbul34", "example34@gmail.com", 12345, 100120023003)

if mod1.login() == 1:
    if mod1.panel() == 1:
        mod1.quit()