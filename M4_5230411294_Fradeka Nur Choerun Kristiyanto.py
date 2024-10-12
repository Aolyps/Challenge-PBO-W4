class Debitur :
    nama = ""
    __ktp = ""
    _pinjaman = ""

    def __init__(self, nama, ktp, pinjaman):
        self.nama = nama
        self.__ktp = ktp
        self._pinjaman = pinjaman

    def get_ktp(self):
        return self.__ktp

    def get_limit_pinjaman(self):
        return self._pinjaman


class KelolaDebitur :
    def __init__(self):
        self.debitur = []

    def tampilkan_debitur(self):
        for debitur in self.debitur:
            print(f"Nama : {debitur.nama}, KTP : {debitur.get_ktp()}, Limit Pinjaman: Rp.{debitur._pinjaman}")

    def cari_debitur(self, nama):
        result = [debitur for debitur in self.debitur if debitur.nama == nama]
        if result:
            for debitur in result:
                print(f"Nama: {debitur.nama}, KTP: {debitur.get_ktp()}, Limit Pinjaman: {debitur._pinjaman}")
        else:
            print("Debitur tidak ditemukan.")

    def tambah_debitur(self, nama, ktp, pinjaman):
        if any(debitur.get_ktp() == ktp for debitur in self.debitur):
            print("KTP sudah terdaftar.")
        else:
            debitur_baru = Debitur(nama, ktp, pinjaman)
            self.debitur.append(debitur_baru)


class Pinjaman :
    def __init__(self, debitur, pinjaman, bunga, bulan):
        self.debitur = debitur
        self.pinjaman = pinjaman
        self.bunga = bunga
        self.bulan = bulan

    def hitung_angsuran(self):
        angsuran_pokok = self.pinjaman * self.bunga
        angsuran_bulanan = angsuran_pokok / self.bulan
        total_angsuran = angsuran_pokok + angsuran_bulanan 
        return angsuran_pokok, angsuran_bulanan, total_angsuran


class KelolaPinjaman :
    def __init__(self, kelola_debitur):
        self.kelola_debitur = kelola_debitur
        self.pinjaman_list = []

    def tambah_pinjaman(self, nama, pinjaman, bunga, bulan):
        debitur = next((debitur for debitur in self.kelola_debitur.debitur if debitur.nama == nama), None)
        if not debitur:
            print("Nama tidak ada.")
        elif pinjaman > debitur.get_limit_pinjaman():
            print("Pinjaman melebihi limit.")
        else:
            pinjaman_baru = Pinjaman(debitur, pinjaman, bunga, bulan)
            self.pinjaman_list.append(pinjaman_baru)
            print(f"Pinjaman untuk {nama} berhasil ditambahkan.")

    def tampilkan_pinjaman(self):
        for pinjaman in self.pinjaman_list[100]:
            angsuran_pokok, angsuran_bulanan, total_angsuran = pinjaman.hitung_angsuran()
            print(f"Nama: {pinjaman.debitur.nama}, Pinjaman: {pinjaman.pinjaman}, Bunga: {pinjaman.bunga}, "
                  f"Bulan: {pinjaman.bulan},Angsuran Pokok: {angsuran_pokok}, Angsuran Bulanan: {angsuran_bulanan}, Total Angsuran: {total_angsuran}")

def main() :
    kelola_debitur = KelolaDebitur()
    kelola_pinjaman = KelolaPinjaman(kelola_debitur)

    kelola_debitur.tambah_debitur("toji", "123", 5000000)
    kelola_debitur.tambah_debitur("gojo", "456", 6000000)
    kelola_debitur.tambah_debitur("yuji", "789", 7000000)
    kelola_debitur.tambah_debitur("sukuna", "098", 8000000)
    kelola_debitur.tambah_debitur("mai", "765", 9000000)

    while True:
        print("\n============ Admin Pinjol ============")
        print("1. Kelola Debitur")
        print("2. Kelola Pinjaman")
        print("0. Keluar")

        menu = int(input("Masukkan pilihan anda: "))

        if menu == 1:
            print("\n============ Submenu ============")
            print("1. Tambah Debitur")
            print("2. Cari Debitur")
            print("3. Tampilkan Debitur")
            print("0. Keluar")
            men = int(input("Masukkan pilihan anda: "))
            if men == 1:
                nama = input("Masukkan nama: ")
                ktp = input("Masukkan nomor KTP: ")
                pinjaman = int(input("Masukkan limit pinjaman: "))
                kelola_debitur.tambah_debitur(nama, ktp, pinjaman)
                print(f"Debitur {nama} berhasil ditambahkan.")
            elif men == 2:
                nama = input("Masukkan nama debitur yang dicari: ")
                kelola_debitur.cari_debitur(nama)
            elif men == 3:
                kelola_debitur.tampilkan_debitur()
            else:
                break

        elif menu == 2:
            print("\n============ Submenu ============")
            print("1. Tambah Pinjaman")
            print("2. Tampilkan Pinjaman")
            print("0. Keluar")
            men = int(input("Masukkan pilihan anda: "))
            if men == 1:
                nama = input("Masukkan nama debitur: ")
                pinjaman = int(input("Masukkan jumlah pinjaman : "))
                bunga = float(input("Masukkan persen bunga : "))
                bulan = int(input("Masukkan jumlah bulan angsuran : "))
                kelola_pinjaman.tambah_pinjaman(nama, pinjaman, bunga, bulan)
            elif men == 2:
                kelola_pinjaman.tampilkan_pinjaman()
            else:
                break

        elif menu == 0:
            print("Program akan keluar.")
            break
        else:
            print("Menu tidak valid.")

if __name__ == "__main__" :
    main()