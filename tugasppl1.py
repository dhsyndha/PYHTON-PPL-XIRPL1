class agama:
    def __init__(self, nama, agama):
        self.nama = nama
        self.agama = agama

    def perkenalan(self):
        print("halo nama saya", self.nama, "agama saya", self.agama)

class islam(agama):
    def __init__(self, nama, agama, sholat):
        agama.__init__(self, nama, agama)
        self.sholat = sholat
    
class kristen(agama):
    def __init__(self, nama, agama, sembayang):
        agama.__init__(self, nama, agama)
        self.sembayang = sembayang

hisyam = islam('hisyam', 'islam', 'sholat')
hisyam.perkenalan()
print(f'saya beribadah dengan melakukan {hisyam.beribadah}')

abraham = kristen('abraham', 'kristen', 'sembayang')
abraham.perkenalan()
print(f'saya beribadah dengan melakukan {abraham.beribadah}')