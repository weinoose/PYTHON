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
    selection = int(input("\n\nWelcome to the CitiBank, What would you like to do?\n1 - Bakiye Sorgula\n2 - Para Çek\n3 - Para Yatır\n4 - Kartın İade\nSeçim Yapınız: "))
    if selection == 4:
        print("Çıkış Yapılıyor...")
        break
    elif selection == 1:
        print(f"Bakiyeniz: {(atm[user]['Main']) + (atm[user]['Sub'])}$")
        break
    elif selection == 2:
        money_out = int(input("Ne kadar para çekmek istiyorsun: "))
        if money_out <= (atm[user]['Main']):
            atm[user]["Main"] -= money_out
            print("Paranızı çekebilirsiniz...")
            print(f"Ana hesap bakiyeniz: {(atm[user]['Main']) + (atm[user]['Sub'])}$")
            break
        else:
            quest = input("Ana hesapta yeterli bakiye yok. Yedek hesap sorgulansın mı? (y/n): ")
            if quest == "y":
                atm[user]["Main"] += atm[user]["Sub"]
                if atm[user]["Main"] >= money_out:
                    print("Paranızı alabilirsiniz.")
                    atm[user]["Main"] -= money_out
                    print(f"Ana hesap bakiyeniz: {atm[user]['Main']}$")
                    break
                else:
                    print("Yeterli bakiye sağlanamadı. işlem iptal edildi.")
                    print(f"Ana hesap bakiyeniz: {atm[user]['Main']}$")
                    break
            elif quest == "n":
                print("Para çekme işlemi gerçekleştirilmemiştir...")
                break
            else:
                print("Seçiminiz yanlıştır...")
                break
    elif selection == 3:
        money_in = int(input("Ne kadar para yatırmak istiyorsunuz: "))
        atm[user]["Main"] += money_in
        print(f"Bakiyeniz: {(atm[user]['Main']) + (atm[user]['Sub'])}$")
        break
    else:
        print("Yanlış seçim...")
        print("Çıkış Yapılıyor...")
        break