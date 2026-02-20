"""
==========================================================
 TUGAS 3 - Sistem Keuangan dengan Encapsulation
 Chapter 4: Object-Oriented Programming
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Buat class Rekening dengan access modifier:
    - Private: __saldo, __pin, __riwayat_transaksi
    - Protected: _nomor_rekening, _pemilik
    - Public: bank
 2. Implementasikan @property untuk saldo (read-only)
    dan pemilik (dengan setter validation)
 3. Implementasikan method: setor, tarik, transfer,
    cek_riwayat, ganti_pin (semua memerlukan verifikasi PIN)
 4. Demonstrasikan error saat mengakses atribut private
 5. Buat minimal 2 objek Rekening dan lakukan transaksi

 Konsep yang dipelajari:
 - Access modifier (public, protected, private)
 - Name mangling (double underscore)
 - Property decorator (@property, @setter)
 - Data validation dalam setter
 - Encapsulation untuk keamanan data
==========================================================
"""


# Tugas 3 -- Sistem Keuangan dengan Encapsulation (tugas_03.py)
from datetime import datetime

class Rekening:
    def __init__(self, nomor, pemilik, pin_awal, saldo_awal=0):
        # Public Attribute
        self.bank = "Bank Unismuh Syariah"
        
        # Protected Attribute
        self._nomor_rekening = nomor
        self._pemilik = pemilik
        
        # Private Attribute (Gunakan __ untuk enkapsulasi)
        self.__saldo = saldo_awal
        self.__pin = pin_awal
        self.__riwayat_transaksi = [f"Pembukaan rekening: +{saldo_awal}"]

    # Getter untuk Saldo (Read-only)
    @property
    def saldo(self):
        return self.__saldo

    # Getter & Setter untuk Pemilik
    @property
    def pemilik(self):
        return self._pemilik

    @pemilik.setter
    def pemilik(self, nama_baru):
        if nama_baru.strip():
            self._pemilik = nama_baru
        else:
            print("Error: Nama tidak boleh kosong!")

    # Method Setor
    def setor(self, jumlah, pin):
        if pin == self.__pin:
            self.__saldo += jumlah
            self.__riwayat_transaksi.append(f"Setor tunai: +{jumlah}")
            print(f"Setoran Rp{jumlah} berhasil!")
        else:
            print("PIN Salah! Transaksi setor gagal.")

    # Method Tarik
    def tarik(self, jumlah, pin):
        if pin == self.__pin:
            if jumlah <= self.__saldo:
                self.__saldo -= jumlah
                self.__riwayat_transaksi.append(f"Tarik tunai: -{jumlah}")
                print(f"Penarikan Rp{jumlah} berhasil!")
            else:
                print("Saldo tidak mencukupi!")
        else:
            print("PIN Salah! Transaksi tarik gagal.")

    # Method Transfer (Penyebab error biasanya di sini)
    def transfer(self, tujuan, jumlah, pin):
        if pin == self.__pin:
            if jumlah <= self.__saldo:
                self.__saldo -= jumlah
                # Memanggil method helper di objek tujuan
                tujuan._terima_transfer(jumlah, self._pemilik)
                self.__riwayat_transaksi.append(f"Transfer ke {tujuan.pemilik}: -{jumlah}")
                print(f"Transfer ke {tujuan.pemilik} sebesar Rp{jumlah} BERHASIL!")
            else:
                print("Saldo tidak mencukupi untuk transfer!")
        else:
            print("PIN Salah! Transfer dibatalkan.")

    # Helper method (Internal untuk urusan transfer)
    def _terima_transfer(self, jumlah, pengirim):
        self.__saldo += jumlah
        self.__riwayat_transaksi.append(f"Terima transfer dari {pengirim}: +{jumlah}")

    def cek_riwayat(self, pin):
        if pin == self.__pin:
            print(f"\n--- RIWAYAT TRANSAKSI: {self._pemilik} ---")
            for log in self.__riwayat_transaksi:
                print(f"[{datetime.now().strftime('%d/%m/%Y')}] {log}")
            print(f"Saldo Akhir: Rp{self.__saldo}")
        else:
            print("PIN Salah! Akses riwayat ditolak.")

# --- DEMONSTRASI PROGRAM ---

# 1. Inisialisasi Objek
rek_safri = Rekening("1058411", "Safriamsah", "123456", 500000)
rek_ciko = Rekening("1058412", "Ciko", "000000", 100000)

print(f"Selamat Datang di {rek_safri.bank}")

# 2. Pembuktian Enkapsulasi (Try-Except)
print("\n[Uji Enkapsulasi]")
try:
    # Ini akan memicu AttributeError karena __saldo bersifat private
    print(rek_safri.__saldo)
except AttributeError:
    print("Suksess: Atribut __saldo tidak bisa diakses langsung (Private)!")

# 3. Jalankan Operasi
print("\n[Menjalankan Transaksi]")
rek_safri.setor(200000, "123456")         # Setor 200rb
rek_safri.transfer(rek_ciko, 150000, "123456") # Transfer 150rb ke Ciko

# 4. Tampilkan Hasil Akhir
rek_safri.cek_riwayat("123456")
rek_ciko.cek_riwayat("000000")
