#buat 3 objek orang, pelajar, pekerja
#orang = kelas induk
#pelajar , pekerja = kelas turunan

class orang:
    def __init__(self, nama, asal):
        self.nama = nama
        self.asal = asal

    def perkenalan(self):
        print("halo nama saya siapa",self.nama,"dari mana",self.asal)

class pelajar(orang):
    def __init__(self, nama, asal, sekolah):
        orang.__init__(self, nama, asal)
        self.sekolah = sekolah

class pekerja(orang):
    def __init__(self, nama, asal, kantor):
        super().__init__(nama, asal)
        self.kantor = kantor

andi = orang('andi','jakarta\n')
andi.perkenalan()

tito = pelajar('tito','subang','SMKJP1')
tito.perkenalan()
print(f'saya sekolah di{tito.sekolah}')

cahyo = pekerja('cahyo','bandung','SMKJP1')
cahyo.perkenalan()
print(f'saya kerja di{cahyo.asal}')