
# TUGAS 2 - Kalkulator Konversi Suhu (tugas_02.py)
# Chapter 1: Dasar Python
# Laboratorium Python & Dasar AI
# Universitas Muhammadiyah Makassar

# Daftar nilai Celsius yang akan diuji (minimal 3 nilai)
daftar_celsius = [25, 37.5, 100]

print("======= KALKULATOR KONVERSI SUHU =======")

# Looping untuk menguji setiap nilai Celsius dalam daftar
for celsius in daftar_celsius:
    # 1. Hitung Konversi ke Fahrenheit
    # Rumus: F = (C * 9/5) + 32
    fahrenheit = (celsius * 9/5) + 32

    # 2. Hitung Konversi ke Reamur
    # Rumus: R = C * 4/5
    reamur = celsius * 4/5

    # 3. Hitung Konversi ke Kelvin
    # Rumus: K = C + 273.15
    kelvin = celsius + 273.15

    # 4. Tampilkan Hasil dengan 2 angka desimal menggunakan :.2f
    print(f"Input Celsius : {celsius}°C")
    print(f"-> Fahrenheit : {fahrenheit:.2f}°F")
    print(f"-> Reamur     : {reamur:.2f}°R")
    print(f"-> Kelvin     : {kelvin:.2f} K")
    print("-" * 40)

print("Proses Konversi Selesai.")
