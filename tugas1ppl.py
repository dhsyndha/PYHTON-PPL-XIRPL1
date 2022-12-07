class Agama:
    def _init_(self,nama,agama):
        self.nama = nama
        self.agama = agama
        
    def perkenalan(self):
        print("Halo nama saya", self.nama, "agama saya", self.agama)
        
class Islam(Agama):
    def _init_(self,nama,agama,sholat):
        Agama.__init__(self, nama, agama)
        self.sholat = sholat
        
class Kristen(Agama):
    def _init_(self,nama,agama,sembhayang):
        Agama.__init__(self, nama, agama)
        self.sembhayang = sembhayang

hisyam = Islam('Hisyam', 'Islam', 'Sholat')
hisyam.perkenalan()
print(f'Saya beribadah dengan melakukan {hisyam.sholat}\n')

abraham = Kristen('Abraham', 'Kristen', 'Sembahyang')
abraham.perkenalan()
print(f'Saya beribadah dengan melakukan {abraham.sembhayang}')