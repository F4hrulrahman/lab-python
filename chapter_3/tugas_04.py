"""
==========================================================
 TUGAS 4 - Permainan Tebak Angka
 Chapter 3: Control Flow & Fungsi
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Buat fungsi yang menghasilkan angka acak 1-100 (import random)
 2. Buat while loop untuk tebak angka (gunakan input())
 3. Berikan petunjuk "Terlalu besar!" / "Terlalu kecil!"
 4. Hitung dan tampilkan jumlah percobaan saat berhasil
 5. Gunakan break untuk keluar saat tebakan benar
 6. Batas maksimal 10 percobaan, tampilkan "Game Over" jika gagal
 7. Buat fungsi rekursif tebak_rekursif sebagai alternatif

 Catatan: Tugas ini interaktif (menggunakan input()).
          Sertakan screenshot saat menjalankan program.
==========================================================
"""

import random

# Fungsi menghasilkan angka acak
def generate_angka():
    return random.randint(1, 100)

# Fungsi Versi Iteratif (While Loop)
def main_game():
    target = generate_angka()
    percobaan = 0
    maks_percobaan = 10
    
    print("=== PERMAINAN TEBAK ANGKA (ITERATIF) ===")
    print("Saya sudah memikirkan angka antara 1-100.")
    print(f"Kamu punya {maks_percobaan} kesempatan!")

    # While Loop untuk meminta input
    while percobaan < maks_percobaan:
        percobaan += 1
        try:
            tebakan = int(input(f"\nPercobaan ke-{percobaan}: Masukkan tebakanmu: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            percobaan -= 1 # Tidak menghitung percobaan jika input salah
            continue

    # Memberikan petunjuk
        if tebakan < target:
            print("Terlalu kecil!")
        elif tebakan > target:
            print("Terlalu besar!")
        else:
    # Menampilkan hasil dan Break
            print(f"SELAMAT! Kamu berhasil menebak angka {target} dalam {percobaan} percobaan.")
            break
    
    # Penanganan Game Over
    else:
        print("\n=== GAME OVER ===")
        print(f"Maaf, kamu gagal. Angka yang benar adalah {target}.")

# Fungsi Rekursif sebagai alternatif
def tebak_rekursif(target, percobaan=1, maks=10):
    if percobaan > maks:
        print(f"\n[Rekursif] Game Over! Jawabannya adalah {target}")
        return
    
    try:
        tebakan = int(input(f"[Rekursif] Percobaan {percobaan}: "))
    except ValueError:
        return tebak_rekursif(target, percobaan, maks)

    if tebakan == target:
        print(f"Benar! Kamu menang di percobaan ke-{percobaan}")
    elif tebakan < target:
        print("Terlalu kecil!")
        tebak_rekursif(target, percobaan + 1, maks)
    else:
        print("Terlalu besar!")
        tebak_rekursif(target, percobaan + 1, maks)

# Jalankan Program
if __name__ == "__main__":
    main_game()
    # Jika ingin mencoba versi rekursif, hapus tanda pagar di bawah:
    # print("\n\n--- Beralih ke Versi Rekursif ---")
    # tebak_rekursif(random.randint(1,100))
