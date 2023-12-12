class mahasiswa():
    def __init__(self):
        self.nama = []
        self.nim = []
        self.tugas = []
        self.uts = []
        self.uas = []

# Menambahkan data inputan 
    def tambah(self):
        print("Tambah data\n")
        nama    = input("Nama Mahasiswa     : ")
        self.nama.append(nama)
        nim     = int(input("NIM Mahasiswa      : "))
        self.nim.append(nim)
        tugas   = int(input("Nilai Tugas        : "))
        self.tugas.append(tugas)
        uts     = int(input("Nilai UTS          : "))
        self.uts.append(uts)
        uas     = int(input("Nilai UAS          : "))
        self.uas.append(uas)

# Menampilkan seluruh data 
    def lihat(self):
        for i in range(len(self.nama)):
            print(f"\nData ke -{i+1}")
            print(f"Nama Mahasiswa: {self.nama[i]}")
            print(f"NIM Mahasiswa : {self.nim[i]}")
            print(f"Nilai TUGAS   : {self.tugas[i]}")
            print(f"Nilai UTS     : {self.uts[i]}")
            print(f"Nilai UAS     : {self.uas[i]}")
                
# Menghapus inputan nama
    def hapus(self, nama):
        print("Hapus data inputan")
        nama = (input("\nMasukan Nama Mahasiswa : "))
        if nama in self.nama:
            print("Data {0} berhasil di hapus".format(nama))
            index = self.nama.index(nama)
            del self.nama[index]
            del self.nim[index]
            del self.tugas[index]
            del self.uts[index]
            del self.uas[index]
        else:
            print("NAMA {0} TIDAK ADA!".format(nama))
    
# Mengubah data nama inputan
    def ubah(self, nama):
        nama = input("Nama yang ingin di ubah : ")
        if nama in self.nama:
            index = self.nama.index(nama)
            self.nim[index]     = int(input("NIM            : "))
            self.tugas[index]   = int(input("Nilai Tugas    : "))
            self.uts[index]     = int(input("Nilai UTS      : "))
            self.uas[index]     = int(input("Nilai UAS      : "))

            print("\nData {0} berhasil di ubah".format(nama))
        else:
            print("NAMA {0} TIDAK ADA!".format(nama))


print("="*20)
print("|PROGRAM INPUT DATA|")
print("="*20)

data = mahasiswa()

while True: 
    print()
    menu = input("[(T)ambah, (L)ihat, (H)apus, (U)bah, (K)eluar] : ")
    print("~"*78)
    print()

    if menu.lower() == 't':
        data.tambah()

    elif menu.lower() == 'l':
        if data.nama:
            data.lihat()
        else:
            print("BELUM ADA DATA!, pilih [T/t] untuk menambah data")       

    elif menu.lower() == "h":
        data.hapus(data.nama)


    elif menu.lower() == "u":
        data.ubah(data.nama) 

    elif menu.lower() == "k":
        print("Program selesai, Terima Kasih :) ")
        break

    else:
        print("\n INPUT {} TIDAK ADA!, Silakan pilih [T/L/H/U/K] untuk menjalankan program!".format(menu))