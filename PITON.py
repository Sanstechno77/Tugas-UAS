class BentukTas():
    kotak = 40
    bulat = 30
    persegipanjang = 70

    def turun(self, x):
        if x <= self.kotak:
            return 0
        elif x >= self.bulat:
            return 1
        else:
            return bawah(x, self.bulat, self.kotak)

    def pas(self, x):
        if self.kotak < x < self.bulat:
            return atas(x, self.kotak, self.bulat)
        elif self.bulat < x < self.persegipanjang:
            return bawah(x, self.bulat, self.persegipanjang)
        elif x == self.bulat:
            return 1
        else:
            return 0

    def naik(self, x):
        if x >= self.bulat:
            return 1
        elif x <= self.persegipanjang:
            return 0
        else:
            return up(x, self.persegipanjang, self.bulat)

class MerkTas():
    Eiger = 50
    Consina = 30
    Adidas = 40

    def sedikit(self, x):
        if x >= self.Consina:
            return 0
        elif x <= self.Eiger:
            return 1
        else:
            return down(x, self.Eiger, self.Consina)
    
    def cukup(self, x):
        if self.Consina < x < self.Eiger:
            return up(x, self.Consina, self.Eiger)
        elif self.Eiger < x < self.Adidas:
            return down(x, self.Eiger, self.Adidas)
        elif x == self.Eiger:
            return 1
        else:
            return 0

    def banyak(self, x):
        if x >= self.Adidas:
            return 1
        elif x <= self.Eiger:
            return 0
        else:
            return up(x, self.Eiger, self.Adidas)

class ModelTas():
    Carrier = 80
    Ransel = 60
    Waistbag = 70

    def sedikit(self, x):
        if x >= self.Ransel:
            return 0
        elif x <= self.Carrier:
            return 1
        else:
            return down(x, self.Carrier, self.Ransel)
    
    def cukup(self, x):
        if self.Waistbag < x < self.Ransel:
            return up(x, self.Ransel, self.Waistbag)
        elif self.Waistbag < x < self.Carrier:
            return down(x, self.Waistbag, self.Carrier)
        elif x == self.Waistbag:
            return 1
        else:
            return 0

    def banyak(self, x):
        if x >= self.Carrier:
            return 1
        elif x <= self.Waistbag:
            return 0
        else:
            return up(x, self.Waistbag, self.Carrier)

class BahanTas():
    Kulit = 40
    Parasut = 60
    Kanvas = 80
   
    def sedikit(self, x):
        if x >= self.Parasut:
            return 0
        elif x <= self.Kulit:
            return 1
        else:
            return down(x, self.Kulit, self.Parasut)
    
    def cukup(self, x):
        if self.Kulit < x < self.Parasut:
            return up(x, self.Kulit, self.Parasut)
        elif self.Kulit < x < self.Kanvas:
            return down(x, self.Parasut, self.Kanvas)
        elif x == self.Parasut:
            return 1
        else:
            return 0

    def banyak(self, x):
        if x >= self.Kanvas:
            return 1
        elif x <= self.Parasut:
            return 0
        else:
            return up(x, self.Parasut, self.Kanvas)