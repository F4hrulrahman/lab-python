
# TUGAS 1 - Biodata Mahasiswa (tugas_01.py)
# Chapter 1: Dasar Python
# Laboratorium Python & Dasar AI
# Universitas Muhammadiyah Makassar

# ── Deklarasi Variabel ──────────────────────────────────
nama_lengkap = "FAHRUL RAHMAN"      # Tipe: str
nim          = "105841117522"    # Tipe: str
jurusan      = "INFORMATIKA"     # Tipe: str
semester     = 7                 # Tipe: int
ipk          = 3.19              # Tipe: float (gunakan titik '.')
status_aktif = True              # Tipe: bool

# ── Tampilkan Biodata (f-string) ───────────────────────
print("===== BIODATA MAHASISWA =====")
print(f"Nama     : {nama_lengkap}")
print(f"NIM      : {nim}")
print(f"Jurusan  : {jurusan}")
print(f"Semester : {semester}")
print(f"IPK      : {ipk}")
print(f"Aktif    : {status_aktif}")
print("=============================")

# ── Tampilkan Tipe Data (type) ─────────────────────────
print(f"Tipe 'nama'     : {type(nama_lengkap)}")
print(f"Tipe 'nim'      : {type(nim)}")
print(f"Tipe 'jurusan'  : {type(jurusan)}")
print(f"Tipe 'semester' : {type(semester)}")
print(f"Tipe 'ipk'      : {type(ipk)}")
print(f"Tipe 'aktif'    : {type(status_aktif)}")

# ── Pemeriksaan (isinstance) ───────────────────────────
print("-" * 35)
print(f"Apakah NIM bertipe str?      : {isinstance(nim, str)}")
print(f"Apakah Semester bertipe int? : {isinstance(semester, int)}")
print("-" * 35)
