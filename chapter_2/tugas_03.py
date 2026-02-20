
#==========================================================
 #TUGAS 3 - Analisis Teks dengan Set
 #Chapter 2: Struktur Data
 #Laboratorium Python & Dasar AI
 #Universitas Muhammadiyah Makassar
#==========================================================

# Definisikan 2 buah string kalimat
kalimat1 = "belajar pemrograman python sangat menyenangkan dan bermanfaat untuk masa depan mahasiswa"
kalimat2 = "mahasiswa informatika harus belajar logika pemrograman agar mahir membuat aplikasi bermanfaat"

# Konversi ke set berisi kata-kata unik (lowercase)
# .lower() untuk mengecilkan huruf, .split() untuk memecah kalimat menjadi list kata
set1 = set(kalimat1.lower().split())
set2 = set(kalimat2.lower().split())

print("Kalimat 1:", kalimat1)
print("Kalimat 2:", kalimat2)
print("-" * 30)

# Kata yang muncul di kedua kalimat (Intersection)
irisan = set1.intersection(set2)
print(f"Kata di kedua kalimat (Intersection): \n{irisan}")

# Kata yang hanya ada di kalimat pertama (Difference)
hanya_set1 = set1.difference(set2)
print(f"\nKata hanya di kalimat pertama: \n{hanya_set1}")

# Kata yang hanya ada di kalimat kedua (Difference)
hanya_set2 = set2.difference(set1)
print(f"\nKata hanya di kalimat kedua: \n{hanya_set2}")

# Semua kata unik dari kedua kalimat (Union)
gabungan = set1.union(set2)
print(f"\nSemua kata unik (Union): \n{gabungan}")

# Kata yang hanya ada di salah satu kalimat (Symmetric Difference)
simetris_diff = set1.symmetric_difference(set2)
print(f"\nKata di salah satu kalimat saja (Symmetric Difference): \n{simetris_diff}")

# Hitung jumlah kata unik total
print("-" * 30)
print(f"Jumlah kata unik total: {len(gabungan)}")
