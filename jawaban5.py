input("NIM :")
input("Nama :")
print("Pilihan")
print("1. Capucino")
print("2. Teh")
print("3. Exit")
pilih = input('Masukan pilihan: ')

if pilih == "1":
    print("Memilih capucino")
elif pilih == "2":
	print("Memilih teh")
elif pilih == "3":
	exit()
harga = int(input("Masukan harga :"))
total = print(harga + harga * 10 / 100)