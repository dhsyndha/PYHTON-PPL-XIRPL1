#proctected class

class perhiasan:
    def __init__(self, nama):
        self._nama = nama

class perhiasansaya(perhiasan):
    def __init__(self, nama, total_per):
        super().__init__(nama)
        self._total_per = total_per

    def jumlah(self):
        print(f'ini adalah perhiasan {self._nama} jumlah {self._total_per}\n')

print('ini adalah perhiasan saya')
punyaku = perhiasansaya('kalung', 2)
punyaku.jumlah() 