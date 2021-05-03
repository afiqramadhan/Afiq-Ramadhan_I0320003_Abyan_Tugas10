# membaca isi file per baris
print("============================================")
# buka file
file_puisi=open("puisi.txt","r")

# baca isi file
print(file_puisi.readlines())

# tutup file
file_puisi.close()

# membaca semua teks dalam file
print("============================================")
# buka file
file_puisi=open("puisi.txt","r")

# baca isi file
puisi=file_puisi.read()

# cetak isi file
print(puisi)

# tutup file
file_puisi.close()

