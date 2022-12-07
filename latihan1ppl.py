#membuat variabel atau box bernama buah
buah = ["apel" , "durian" , "kiwi" , "alpukat" , "mangga"]
sayur = ["pakcoy" , "seledri" , "kangkung" , "bayem" , "asem"]

#tampilkan data yang ada di variabel buah
#print(buah)

#tampilkan data berurutan kebawah dari awal sampai akhir
#for gerobak in buah:
#    print (gerobak)

#penampilan hanya beberapa saja
#print(buah[0], buah[2])

#untuk menambahkan buah pake append bagian belakang dan prepend di paling depan
#buah.append("anggur merah")
#buah.prepend("jeruk")
#print (buah)

#cara menghapus yang ada didalam buah
#buah.remove("kiwi")
#print(buah)
#cara memotong nilai yang ada di box buah
#print(buah[1:4])

#operasi aritmatika tipe data list
#dagang_hari_ini = buah + sayur

#for gerobak in dagang_hari_ini:
#    print(gerobak)

kasir = input("mau tambah buah apa lagi?")
buah.append(kasir)