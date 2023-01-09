atm = {
    100 : {
        "Name" : "Lewis Hamilton",
        "Main" : 1425000,
        "Sub" : 625000,
    },

    101 : {
        "Name" : "Andy Murray",
        "Main" : 427000,
        "Sub" : 0
    },

    102 : {
        "Name" : "Mike Tyson",
        "Main" : 4,
        "Sub" : 52
    }
}

while True:
    user = int(input("Insert your ID: "))
    selection = int(input("\n\nWelcome to the CitiBank, What would you like to do?\n1 - Cash Request\n2 - Withdraw\n3 - Deposit\n4 - Card Back\nChoice: "))
    if selection == 4:
        print("Quitting...")
        break
    elif selection == 1:
        print(f"Your total cash: {(atm[user]['Main']) + (atm[user]['Sub'])}$")
        break
    elif selection == 2:
        money_out = int(input("How much amount would you like to withdraw: "))
        if money_out <= (atm[user]['Main']):
            atm[user]["Main"] -= money_out
            print("You can get your money.")
            print(f"Your total cash: {(atm[user]['Main']) + (atm[user]['Sub'])}$")
            break
        else:
            quest = input("There is not enough balance in the main account. Query the backup account? (y/n): ")
            if quest == "y":
                atm[user]["Main"] += atm[user]["Sub"]
                if atm[user]["Main"] >= money_out:
                    print("You can get your money.")
                    atm[user]["Main"] -= money_out
                    print(f"Your total cash: {atm[user]['Main']}$")
                    break
                else:
                    print("Sufficient balance could not be obtained. The transaction has been cancelled.")
                    print(f"Your total cash: {atm[user]['Main']}$")
                    break
            elif quest == "n":
                print("Para çekme işlemi gerçekleştirilmemiştir...")
                break
            else:
                print("Your choice is wrong.")
                break
    elif selection == 3:
        money_in = int(input("How much money do you want to deposit: "))
        atm[user]["Main"] += money_in
        print(f"Your total: {(atm[user]['Main']) + (atm[user]['Sub'])}$")
        break
    else:
        print("Wrong choice.")
        print("Quitting.")
        break