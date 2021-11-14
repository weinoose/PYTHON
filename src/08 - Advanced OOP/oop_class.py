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

player1 = Player("Cristiano Ronaldo", 91, 91, 95, 85, 45, 90)
print(player1)