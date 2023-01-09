class Player():
    def __init__(self, name, pac, dri, sho, pas, dff, phy):
        self.name = name
        self.pac = pac
        self.dri = dri
        self.sho = sho
        self.pas = pas
        self.dff = dff
        self.phy = phy
    def __str__(self):
        return self.name
    def overall(self):
        ovr = ((self.pac*5.2) + (self.dri*5.2) + (self.sho*2) + (self.dff*0.1) + (self.phy*1.5) + (self.pas*2))/16
        return int(ovr)

player1 = Player("Cristiano Ronaldo", 91, 91, 95, 85, 45, 90)
player2 = Player("Lionel Messi", 88, 97, 94, 94, 35, 70)
player3 = Player("Sadio Mane", 94, 89, 84, 78, 35, 76)

print(player1.overall())
print(player2.overall())
print(player3.overall())