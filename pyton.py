class cal():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def tambah(self) :
        return self.a + self.b
    def kurang(self) :
        return self.a - self.b
a = int(input('silahkan masukkan angka pertama :'))
b = int(input('silahkan masukkan angaka kedua :'))
obj = cal (a, b)
while True : 
    def menu():
        x = ('1.tambah \ n2. kurang')
        print(x)
    pilihan = int(input('silahkan dipilih : ')) 
    if pilihan == 1 :
        print("hasilnya : ", obj.tambah ())
        break
    elif pilihan == 2:
        print ("hasilnya : ", obj.kurang())
        break