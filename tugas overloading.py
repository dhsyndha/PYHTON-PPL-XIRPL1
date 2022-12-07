#overloading
def garis():
    print("-------------------------------------")

class angka :
    def __init__(self, angka):
        self.angka = angka

    def __gt__(self, objek):
        return self.angka > objek.angka

    def __It__(self, objek):
        return self.angka < objek.angka

    def __eq__(self, objek):
        return self.angka == objek.angka

x1 = angka(15)
x2 = angka(25)

print(x1 > x2)
print(x1 < x2)
print(x1 == x2)
garis()

#coba tugas

class angka :
    def __init__(self, angka):
        self.angka = angka
    
    def __sub__(self, objek):
        return self.angka - objek.angka

    def __mul__(self, objek):
        return self.angka * objek.angka

x1 = angka(50)
x2 = angka(15)
print(x1 - x2)

x3 = angka(15)
x4 = angka(8)
print(x3 * x4)