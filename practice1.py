#tugas praktek enkapsulasi

#public

class siswa :
    def __init__(self, siswa):
        self.siswa = siswa

siswa_JP1 = siswa('Euroski')

print(f'1.siswa kami bernama : {siswa_JP1.siswa}\n')

#protected
class guru :
    def __init__(self, guru):
        self._guru = guru

class gurujp(guru) :
    def __init__(self, guru):
        super().__init__(guru)
        self._guru_kami = guru

    def lihat(self) :
        print(f'guru kami bernama {self._guru}\n')

guru1 = gurujp('bu anita')
guru1.lihat()

#private
class kepsek :
    def __init__(self, kepsek):
        self.__kepsek = kepsek

    def tampilkan_kepsek(self):
        print(f'nama kepsek : {self.__kepsek}\n')

keplah = kepsek('lilik')
keplah.tampilkan_kepsek()
