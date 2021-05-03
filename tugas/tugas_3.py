# menambahkan data ke file
print("Program Pencatatan Biodata Diri")
print("=================================")

# ambil input dari user
nama = input("Nama: ")
umur = input("Umur: ")
gender = input("Gender: ")
kewarganegaraan = input("Kewarganegaraan: ")
alamat = input("Alamat: ")

# format teks
teks = "Nama: {}\nUmur: {}\nGender: {}\nKewarganegaraan: {}\nAlamat: {}".format(nama, umur, gender, kewarganegaraan, alamat)

# buka file untuk ditulis
file_bio = open("biodata_diri.txt","a")

# tulis teks ke file
file_bio.write(teks)

# tutup file
file_bio.close()