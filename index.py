#belajar object dan class

from distutils.log import warn
from warnings import WarningMessage


class kocheng:
    Warna = None
    usia = None

class icikiwir:
    warna = None
    merk = None
    kecepatan = None

#membuat instance/variable sebagai "objek nyata"
#kocheng hitam menaiki icikiwir honda karbu dengan kecepatan 100km

pembalab_handal = kocheng
pembalab_handal = icikiwir()
pembalab_handal.warna = "black"
pembalab_handal.merk = "honda karbu"
pembalab_handal.kecepatan = "100km"

print("kocheng", pembalab_handal.warna, "menaiki icikiwir",pembalab_handal.merk, "dengan kecepatan",pembalab_handal.kecepatan )

kocheng1 = kocheng()
kocheng1.Warna = "black"
kocheng1.usia = "4 bulan"

kocheng2 = kocheng()
kocheng2.Warna = "white"
kocheng2.usia = "3 bulan"

print(kocheng1.Warna, kocheng1.usia)
print(kocheng2.Warna, kocheng2.usia)