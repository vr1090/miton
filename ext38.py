angka_asal = "1 2 3 4 5 6"
angka_tambah =["7","8","9","0"]


kurang_10 = angka_asal.split(" ")

while len(kurang_10) != 10:
    angka_baru = angka_tambah.pop()
    kurang_10.append( angka_baru )
    print "ich habe neu etwas %r"%(angka_baru)
    print "there is item: ", len(kurang_10)

apalah_lagi = " ".join(kurang_10)

#cupu.. ini mah apalah ga jelas
print "hahaha..",apalah_lagi

