"""
Chapter 3 - Bagian 1: Percabangan
====================================
Percabangan digunakan untuk menjalankan kode berdasarkan kondisi tertentu.
"""

# ============================================
# 1. if, elif, else
# ============================================
print("=== if, elif, else ===")

nilai = 85

if nilai >= 90:
    grade = "A"
elif nilai >= 80:
    grade = "B"
elif nilai >= 70:
    grade = "C"
elif nilai >= 60:
    grade = "D"
else:
    grade = "E"

print(f"Nilai: {nilai} -> Grade: {grade}")

# ============================================
# 2. Kondisi Majemuk
# ============================================
print("\n=== Kondisi Majemuk ===")

umur = 25
punya_sim = True
tidak_mabuk = True

if umur >= 17 and punya_sim and tidak_mabuk:
    print("Boleh mengendarai kendaraan")
else:
    print("Tidak boleh mengendarai kendaraan")

# or
hari = "Sabtu"
if hari == "Sabtu" or hari == "Minggu":
    print(f"{hari} adalah hari libur")
else:
    print(f"{hari} adalah hari kerja")

# ============================================
# 3. Ternary Operator (Inline If)
# ============================================
print("\n=== Ternary Operator ===")

umur = 20
status = "dewasa" if umur >= 18 else "anak-anak"
print(f"Umur {umur}: {status}")

# Contoh lain
x = 10
hasil = "genap" if x % 2 == 0 else "ganjil"
print(f"{x} adalah bilangan {hasil}")

# ============================================
# 4. Nested If
# ============================================
print("\n=== Nested If ===")

skor = 75
kehadiran = 90

if skor >= 60:
    if kehadiran >= 80:
        print("Lulus dengan catatan baik")
    else:
        print("Lulus tapi kehadiran kurang")
else:
    if kehadiran >= 80:
        print("Tidak lulus, tapi kehadiran bagus")
    else:
        print("Tidak lulus dan kehadiran kurang")

# ============================================
# 5. match-case (Python 3.10+)
# ============================================
print("\n=== match-case (Python 3.10+) ===")


def cek_hari(hari):
    match hari.lower():
        case "senin" | "selasa" | "rabu" | "kamis" | "jumat":
            return "Hari kerja"
        case "sabtu" | "minggu":
            return "Hari libur"
        case _:
            return "Hari tidak valid"


for h in ["Senin", "Sabtu", "xyz"]:
    print(f"  {h}: {cek_hari(h)}")


# match-case dengan pattern matching
def cek_perintah(command):
    match command.split():
        case ["quit"]:
            return "Keluar program"
        case ["hello", nama]:
            return f"Halo, {nama}!"
        case ["tambah", a, b]:
            return f"Hasil: {int(a) + int(b)}"
        case _:
            return "Perintah tidak dikenali"


print("\nPattern Matching:")
perintah = ["quit", "hello Budi", "tambah 3 5", "xyz"]
for p in perintah:
    print(f"  '{p}' -> {cek_perintah(p)}")

# ============================================
# 6. Contoh Praktis: Kalkulator Sederhana
# ============================================
print("\n=== Contoh: Kalkulator ===")


def kalkulator(a, operator, b):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b != 0:
            return a / b
        else:
            return "Error: pembagian dengan nol"
    else:
        return "Operator tidak valid"


operasi = [(10, "+", 5), (10, "-", 3), (4, "*", 7), (20, "/", 4), (10, "/", 0)]
for a, op, b in operasi:
    print(f"  {a} {op} {b} = {kalkulator(a, op, b)}")
