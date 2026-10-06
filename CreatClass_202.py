class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)

    def luas(self):
        return self.panjang * self.lebar

    def __str__(self):
        return f"persegi panjang dengan panjang {self.panjang} cm dan lebar {self.lebar} cm"


# main
persegi = PersegiPanjang(3, 2)

print("keliling:", persegi.keliling(), "cm")
print("luas:", persegi.luas(), "cm2")
print(persegi)