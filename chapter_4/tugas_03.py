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


class Rekening:
    """Rekening bank dengan encapsulation.

    Access Modifier:
        Private (__)  : __saldo, __pin, __riwayat_transaksi
        Protected (_) : _nomor_rekening, _pemilik
        Public        : bank

    Attributes:
        bank (str): Nama bank.
    """

    def __init__(self, nomor_rekening, pemilik, pin, saldo_awal=0, bank="Bank Unismuh"):
        """Inisialisasi rekening baru.

        Args:
            nomor_rekening (str): Nomor rekening.
            pemilik (str): Nama pemilik rekening.
            pin (str): PIN 6 digit untuk verifikasi.
            saldo_awal (float): Saldo awal (default 0).
            bank (str): Nama bank (default "Bank Unismuh").
        """
        # TODO: Inisialisasi atribut dengan access modifier yang benar
        # Public
        # self.bank = bank
        #
        # Protected (konvensi: satu underscore)
        # self._nomor_rekening = nomor_rekening
        # self._pemilik = pemilik
        #
        # Private (name mangling: dua underscore)
        # self.__saldo = saldo_awal
        # self.__pin = pin
        # self.__riwayat_transaksi = []
        ...

    # ── Property: saldo (read-only) ─────────────────────────────────────────
    @property
    def saldo(self):
        """Getter untuk saldo (read-only, tanpa setter).

        Returns:
            float: Saldo saat ini.
        """
        # TODO: Kembalikan nilai __saldo
        ...

    # ── Property: pemilik (dengan setter dan validasi) ──────────────────────
    @property
    def pemilik(self):
        """Getter untuk nama pemilik.

        Returns:
            str: Nama pemilik rekening.
        """
        # TODO: Kembalikan nilai _pemilik
        ...

    @pemilik.setter
    def pemilik(self, nama_baru):
        """Setter untuk nama pemilik dengan validasi.

        Args:
            nama_baru (str): Nama baru pemilik.

        Raises:
            ValueError: Jika nama kosong atau kurang dari 3 karakter.
        """
        # TODO: Validasi nama_baru
        # Hint: if not nama_baru or len(nama_baru) < 3:
        #           raise ValueError("Nama harus minimal 3 karakter")
        ...

    def __verifikasi_pin(self, pin):
        """Verifikasi PIN (method private).

        Args:
            pin (str): PIN yang dimasukkan.

        Returns:
            bool: True jika PIN benar.
        """
        # TODO: Bandingkan pin dengan self.__pin
        ...

    def __catat_transaksi(self, jenis, jumlah, keterangan=""):
        """Mencatat transaksi ke riwayat (method private).

        Args:
            jenis (str): Jenis transaksi (SETOR/TARIK/TRANSFER).
            jumlah (float): Jumlah uang.
            keterangan (str): Keterangan tambahan.
        """
        # TODO: Tambahkan dict transaksi ke __riwayat_transaksi
        # Hint: {"jenis": jenis, "jumlah": jumlah, "keterangan": keterangan,
        #        "saldo_setelah": self.__saldo}
        ...

    def setor(self, jumlah, pin):
        """Menyetor uang ke rekening.

        Args:
            jumlah (float): Jumlah uang yang disetor (harus > 0).
            pin (str): PIN untuk verifikasi.

        Returns:
            str: Pesan berhasil/gagal.
        """
        # TODO: Implementasikan
        # 1. Verifikasi PIN
        # 2. Validasi jumlah > 0
        # 3. Tambahkan ke __saldo
        # 4. Catat transaksi
        # 5. Kembalikan pesan berhasil
        ...

    def tarik(self, jumlah, pin):
        """Menarik uang dari rekening.

        Args:
            jumlah (float): Jumlah uang yang ditarik (harus > 0).
            pin (str): PIN untuk verifikasi.

        Returns:
            str: Pesan berhasil/gagal.
        """
        # TODO: Implementasikan
        # 1. Verifikasi PIN
        # 2. Validasi jumlah > 0 dan jumlah <= __saldo
        # 3. Kurangi __saldo
        # 4. Catat transaksi
        # 5. Kembalikan pesan berhasil
        ...

    def transfer(self, tujuan, jumlah, pin):
        """Transfer uang ke rekening lain.

        Args:
            tujuan (Rekening): Objek Rekening tujuan.
            jumlah (float): Jumlah uang yang ditransfer.
            pin (str): PIN pengirim untuk verifikasi.

        Returns:
            str: Pesan berhasil/gagal.
        """
        # TODO: Implementasikan
        # 1. Verifikasi PIN pengirim
        # 2. Validasi jumlah > 0 dan jumlah <= __saldo
        # 3. Kurangi __saldo pengirim
        # 4. Tambah __saldo tujuan (akses via tujuan.__saldo? Tidak bisa!)
        #    Hint: gunakan tujuan.setor() BUKAN akses langsung ke __saldo
        #          Tapi setor() butuh pin tujuan... alternatif: buat method
        #          _terima_transfer(jumlah) yang protected, atau langsung
        #          manipulasi dengan name mangling: tujuan._Rekening__saldo
        # 5. Catat transaksi di kedua rekening
        ...

    def cek_riwayat(self, pin):
        """Menampilkan riwayat transaksi.

        Args:
            pin (str): PIN untuk verifikasi.

        Returns:
            str: Riwayat transaksi dalam format tabel, atau pesan error.
        """
        # TODO: Implementasikan
        # 1. Verifikasi PIN
        # 2. Tampilkan semua transaksi dalam __riwayat_transaksi
        # Hint: for t in self.__riwayat_transaksi:
        #           print(f"  {t['jenis']:<10} | Rp {t['jumlah']:>12,.0f} | {t['keterangan']}")
        ...

    def ganti_pin(self, pin_lama, pin_baru):
        """Mengganti PIN rekening.

        Args:
            pin_lama (str): PIN lama untuk verifikasi.
            pin_baru (str): PIN baru (harus 6 digit angka).

        Returns:
            str: Pesan berhasil/gagal.
        """
        # TODO: Implementasikan
        # 1. Verifikasi PIN lama
        # 2. Validasi PIN baru (harus 6 digit, semua angka)
        #    Hint: len(pin_baru) == 6 and pin_baru.isdigit()
        # 3. Ganti __pin
        ...

    def __str__(self):
        """Representasi string rekening.

        Returns:
            str: Contoh -> "[Bank Unismuh] 001 - Ahmad (Saldo: Rp 1,000,000)"
        """
        # TODO: Implementasikan
        # Hint: f"[{self.bank}] {self._nomor_rekening} - {self._pemilik} (Saldo: Rp {self.__saldo:,.0f})"
        ...


# ── Demonstrasi ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # TODO: Buat 2 objek Rekening
    # rek1 = Rekening("001", "Ahmad Dahlan", "123456", 5_000_000)
    # rek2 = Rekening("002", "Siti Rahmah", "654321", 3_000_000)

    # TODO: Tampilkan info rekening
    # print("=== INFO REKENING ===")
    # print(rek1)
    # print(rek2)

    # TODO: Setor uang
    # print("\n=== SETOR ===")
    # print(rek1.setor(1_000_000, "123456"))

    # TODO: Tarik uang
    # print("\n=== TARIK ===")
    # print(rek1.tarik(500_000, "123456"))

    # TODO: Transfer
    # print("\n=== TRANSFER ===")
    # print(rek1.transfer(rek2, 2_000_000, "123456"))

    # TODO: Cek saldo menggunakan property
    # print("\n=== CEK SALDO (property) ===")
    # print(f"Saldo Ahmad: Rp {rek1.saldo:,.0f}")
    # print(f"Saldo Siti : Rp {rek2.saldo:,.0f}")

    # TODO: Coba ubah saldo langsung (seharusnya error!)
    # print("\n=== TEST AKSES PRIVATE ===")
    # try:
    #     rek1.saldo = 999_999_999  # AttributeError (no setter)
    # except AttributeError as e:
    #     print(f"Error saldo: {e}")
    #
    # try:
    #     print(rek1.__saldo)  # AttributeError (name mangling)
    # except AttributeError as e:
    #     print(f"Error __saldo: {e}")
    #
    # # Tapi bisa diakses via name mangling (tidak disarankan!)
    # print(f"Name mangling: rek1._Rekening__saldo = {rek1._Rekening__saldo}")

    # TODO: Test property setter dengan validasi
    # print("\n=== TEST PROPERTY SETTER ===")
    # rek1.pemilik = "Ahmad Dahlan Syamsuddin"  # berhasil
    # print(f"Pemilik baru: {rek1.pemilik}")
    # try:
    #     rek1.pemilik = "AB"  # ValueError (kurang dari 3 karakter)
    # except ValueError as e:
    #     print(f"Error setter: {e}")

    # TODO: Cek riwayat transaksi
    # print("\n=== RIWAYAT TRANSAKSI ===")
    # rek1.cek_riwayat("123456")

    # TODO: Ganti PIN
    # print("\n=== GANTI PIN ===")
    # print(rek1.ganti_pin("123456", "111111"))
    # print(rek1.ganti_pin("111111", "abc"))  # gagal: bukan 6 digit angka

    pass
