"""
Chapter 5 - Visualisasi Data dengan Matplotlib
=================================================
Panduan visualisasi data menggunakan Matplotlib untuk
melengkapi analisis NumPy & Pandas.

Menampilkan berbagai jenis grafik yang umum digunakan dalam
analisis data dan data science.

Install: pip install matplotlib numpy pandas
"""

import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")  # Backend non-interaktif (untuk menyimpan file)
import matplotlib.pyplot as plt

print("=" * 60)
print("VISUALISASI DATA DENGAN MATPLOTLIB")
print("=" * 60)

# ============================================
# 1. Line Plot - Tren Nilai Mahasiswa
# ============================================
print("\n=== 1. Line Plot: Tren Nilai Mahasiswa ===")

np.random.seed(42)
minggu = np.arange(1, 13)  # 12 minggu
nilai_ahmad = np.clip(60 + np.cumsum(np.random.normal(2, 3, 12)), 40, 100)
nilai_siti = np.clip(75 + np.cumsum(np.random.normal(1, 2, 12)), 40, 100)
nilai_budi = np.clip(50 + np.cumsum(np.random.normal(3, 4, 12)), 40, 100)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(minggu, nilai_ahmad, "o-", label="Ahmad", linewidth=2, markersize=6)
ax.plot(minggu, nilai_siti, "s--", label="Siti", linewidth=2, markersize=6)
ax.plot(minggu, nilai_budi, "^:", label="Budi", linewidth=2, markersize=6)

ax.set_xlabel("Minggu ke-", fontsize=12)
ax.set_ylabel("Nilai", fontsize=12)
ax.set_title(
    "Tren Perkembangan Nilai Mahasiswa (12 Minggu)", fontsize=14, fontweight="bold"
)
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)
ax.set_xticks(minggu)
ax.set_ylim(30, 110)

plt.tight_layout()
plt.savefig("chapter_5/plot_01_line.png", dpi=150)
plt.close()
print("  Tersimpan: chapter_5/plot_01_line.png")

# ============================================
# 2. Bar Chart - IPK per Jurusan
# ============================================
print("\n=== 2. Bar Chart: Rata-rata IPK per Jurusan ===")

jurusan = [
    "Informatika",
    "Sistem\nInformasi",
    "Teknik\nElektro",
    "Matematika",
    "Fisika",
]
ipk_mean = [3.45, 3.52, 3.38, 3.60, 3.41]
ipk_std = [0.25, 0.20, 0.30, 0.22, 0.28]

fig, ax = plt.subplots(figsize=(10, 6))
colors = ["#3498db", "#2ecc71", "#e74c3c", "#f39c12", "#9b59b6"]
bars = ax.bar(
    jurusan,
    ipk_mean,
    yerr=ipk_std,
    color=colors,
    capsize=5,
    edgecolor="white",
    linewidth=1.5,
)

# Tambahkan label nilai di atas bar
for bar, mean in zip(bars, ipk_mean):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.03,
        f"{mean:.2f}",
        ha="center",
        va="bottom",
        fontweight="bold",
        fontsize=11,
    )

ax.set_ylabel("Rata-rata IPK", fontsize=12)
ax.set_title("Perbandingan Rata-rata IPK per Jurusan", fontsize=14, fontweight="bold")
ax.set_ylim(0, 4.2)
ax.axhline(y=3.5, color="red", linestyle="--", alpha=0.5, label="Target (3.50)")
ax.legend()
ax.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig("chapter_5/plot_02_bar.png", dpi=150)
plt.close()
print("  Tersimpan: chapter_5/plot_02_bar.png")

# ============================================
# 3. Histogram - Distribusi Nilai
# ============================================
print("\n=== 3. Histogram: Distribusi Nilai Ujian ===")

np.random.seed(42)
nilai_ujian = np.concatenate(
    [
        np.random.normal(75, 10, 150),  # Mayoritas di sekitar 75
        np.random.normal(50, 8, 50),  # Kelompok bawah
        np.random.normal(90, 5, 30),  # Kelompok atas
    ]
)
nilai_ujian = np.clip(nilai_ujian, 0, 100)

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Histogram biasa
axes[0].hist(nilai_ujian, bins=20, color="#3498db", edgecolor="white", alpha=0.8)
axes[0].axvline(
    np.mean(nilai_ujian),
    color="red",
    linestyle="--",
    linewidth=2,
    label=f"Mean: {np.mean(nilai_ujian):.1f}",
)
axes[0].axvline(
    np.median(nilai_ujian),
    color="green",
    linestyle="--",
    linewidth=2,
    label=f"Median: {np.median(nilai_ujian):.1f}",
)
axes[0].set_xlabel("Nilai", fontsize=12)
axes[0].set_ylabel("Frekuensi", fontsize=12)
axes[0].set_title("Distribusi Nilai Ujian", fontsize=13, fontweight="bold")
axes[0].legend(fontsize=10)
axes[0].grid(axis="y", alpha=0.3)

# Box plot
bp = axes[1].boxplot(
    nilai_ujian,
    vert=True,
    patch_artist=True,
    boxprops=dict(facecolor="#3498db", alpha=0.7),
    medianprops=dict(color="red", linewidth=2),
)
axes[1].set_ylabel("Nilai", fontsize=12)
axes[1].set_title("Box Plot Nilai Ujian", fontsize=13, fontweight="bold")
axes[1].set_xticklabels(["Semua\nMahasiswa"])
axes[1].grid(axis="y", alpha=0.3)

# Tambahkan statistik
stats_text = (
    f"Mean: {np.mean(nilai_ujian):.1f}\n"
    f"Std: {np.std(nilai_ujian):.1f}\n"
    f"Min: {np.min(nilai_ujian):.1f}\n"
    f"Max: {np.max(nilai_ujian):.1f}"
)
axes[1].text(
    1.3,
    np.max(nilai_ujian),
    stats_text,
    fontsize=10,
    va="top",
    bbox=dict(boxstyle="round", facecolor="lightyellow", alpha=0.8),
)

plt.tight_layout()
plt.savefig("chapter_5/plot_03_histogram.png", dpi=150)
plt.close()
print("  Tersimpan: chapter_5/plot_03_histogram.png")

# ============================================
# 4. Scatter Plot - Korelasi Jam Belajar vs IPK
# ============================================
print("\n=== 4. Scatter Plot: Jam Belajar vs IPK ===")

np.random.seed(42)
n = 100
jam_belajar = np.random.uniform(1, 20, n)
ipk = np.clip(2.0 + 0.08 * jam_belajar + np.random.normal(0, 0.3, n), 1.5, 4.0)

fig, ax = plt.subplots(figsize=(10, 6))
scatter = ax.scatter(
    jam_belajar, ipk, c=ipk, cmap="RdYlGn", s=60, alpha=0.7, edgecolors="white"
)

# Garis tren (regresi linear)
z = np.polyfit(jam_belajar, ipk, 1)
p = np.poly1d(z)
x_line = np.linspace(jam_belajar.min(), jam_belajar.max(), 100)
ax.plot(
    x_line,
    p(x_line),
    "r--",
    linewidth=2,
    label=f"Tren: IPK = {z[0]:.3f} x Jam + {z[1]:.3f}",
)

ax.set_xlabel("Jam Belajar per Minggu", fontsize=12)
ax.set_ylabel("IPK", fontsize=12)
ax.set_title("Korelasi Jam Belajar dengan IPK", fontsize=14, fontweight="bold")
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# Colorbar
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label("IPK", fontsize=11)

# Korelasi
korelasi = np.corrcoef(jam_belajar, ipk)[0, 1]
ax.text(
    0.02,
    0.98,
    f"Korelasi: {korelasi:.3f}",
    transform=ax.transAxes,
    fontsize=11,
    va="top",
    bbox=dict(boxstyle="round", facecolor="lightyellow", alpha=0.8),
)

plt.tight_layout()
plt.savefig("chapter_5/plot_04_scatter.png", dpi=150)
plt.close()
print("  Tersimpan: chapter_5/plot_04_scatter.png")

# ============================================
# 5. Pie Chart - Distribusi Jurusan
# ============================================
print("\n=== 5. Pie Chart: Distribusi Mahasiswa per Jurusan ===")

jurusan_names = [
    "Informatika",
    "Sistem Informasi",
    "Teknik Elektro",
    "Matematika",
    "Fisika",
]
jumlah = [120, 95, 75, 45, 35]
colors_pie = ["#3498db", "#2ecc71", "#e74c3c", "#f39c12", "#9b59b6"]
explode = (0.05, 0, 0, 0, 0)  # Highlight Informatika

fig, ax = plt.subplots(figsize=(9, 7))
wedges, texts, autotexts = ax.pie(
    jumlah,
    labels=jurusan_names,
    autopct="%1.1f%%",
    colors=colors_pie,
    explode=explode,
    shadow=True,
    textprops={"fontsize": 11},
    startangle=90,
)
for autotext in autotexts:
    autotext.set_fontweight("bold")

ax.set_title(
    "Distribusi Mahasiswa per Jurusan\n(Total: 370 Mahasiswa)",
    fontsize=14,
    fontweight="bold",
)

plt.tight_layout()
plt.savefig("chapter_5/plot_05_pie.png", dpi=150)
plt.close()
print("  Tersimpan: chapter_5/plot_05_pie.png")

# ============================================
# 6. Heatmap - Korelasi Antar Variabel
# ============================================
print("\n=== 6. Heatmap: Matriks Korelasi ===")

np.random.seed(42)
n = 200
data_mhs = pd.DataFrame(
    {
        "Jam_Belajar": np.random.uniform(1, 20, n),
        "Kehadiran": np.random.uniform(50, 100, n),
        "Tugas": np.random.randint(0, 11, n),
        "UTS": np.random.uniform(30, 100, n),
    }
)
data_mhs["UAS"] = (
    0.2 * data_mhs["Jam_Belajar"] * 5
    + 0.3 * data_mhs["Kehadiran"]
    + 0.15 * data_mhs["Tugas"] * 10
    + 0.35 * data_mhs["UTS"]
    + np.random.normal(0, 5, n)
)
data_mhs["UAS"] = np.clip(data_mhs["UAS"], 0, 100)

korelasi_matrix = data_mhs.corr()

fig, ax = plt.subplots(figsize=(8, 7))
im = ax.imshow(korelasi_matrix.values, cmap="RdYlGn", vmin=-1, vmax=1)

# Labels
ax.set_xticks(range(len(korelasi_matrix.columns)))
ax.set_yticks(range(len(korelasi_matrix.columns)))
ax.set_xticklabels(korelasi_matrix.columns, fontsize=11, rotation=45, ha="right")
ax.set_yticklabels(korelasi_matrix.columns, fontsize=11)

# Tambahkan nilai di setiap cell
for i in range(len(korelasi_matrix)):
    for j in range(len(korelasi_matrix)):
        val = korelasi_matrix.values[i, j]
        color = "white" if abs(val) > 0.6 else "black"
        ax.text(
            j,
            i,
            f"{val:.2f}",
            ha="center",
            va="center",
            fontsize=11,
            fontweight="bold",
            color=color,
        )

ax.set_title("Matriks Korelasi Variabel Akademik", fontsize=14, fontweight="bold")
cbar = plt.colorbar(im, ax=ax, shrink=0.8)
cbar.set_label("Koefisien Korelasi", fontsize=11)

plt.tight_layout()
plt.savefig("chapter_5/plot_06_heatmap.png", dpi=150)
plt.close()
print("  Tersimpan: chapter_5/plot_06_heatmap.png")

# ============================================
# 7. Subplot Gabungan - Dashboard Analisis
# ============================================
print("\n=== 7. Dashboard: Analisis Data Penjualan ===")

np.random.seed(42)
hari = pd.date_range("2024-01-01", periods=30, freq="D")
penjualan_harian = np.random.randint(10, 100, 30) * 100_000

produk_nama = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headset"]
produk_total = [45_000_000, 12_000_000, 8_500_000, 25_000_000, 6_500_000]

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle(
    "Dashboard Analisis Penjualan - Januari 2024",
    fontsize=16,
    fontweight="bold",
    y=1.02,
)

# Plot 1: Tren penjualan harian (line)
axes[0, 0].fill_between(range(30), penjualan_harian / 1e6, alpha=0.3, color="#3498db")
axes[0, 0].plot(range(30), penjualan_harian / 1e6, "o-", color="#3498db", markersize=4)
axes[0, 0].set_title("Tren Penjualan Harian", fontweight="bold")
axes[0, 0].set_xlabel("Hari ke-")
axes[0, 0].set_ylabel("Penjualan (Juta Rp)")
axes[0, 0].grid(True, alpha=0.3)

# Plot 2: Penjualan per produk (bar horizontal)
colors_bar = ["#3498db", "#2ecc71", "#e74c3c", "#f39c12", "#9b59b6"]
bars_h = axes[0, 1].barh(
    produk_nama, [x / 1e6 for x in produk_total], color=colors_bar, edgecolor="white"
)
for bar, val in zip(bars_h, produk_total):
    axes[0, 1].text(
        bar.get_width() + 0.5,
        bar.get_y() + bar.get_height() / 2,
        f"Rp{val / 1e6:.0f}jt",
        va="center",
        fontweight="bold",
        fontsize=10,
    )
axes[0, 1].set_title("Total Penjualan per Produk", fontweight="bold")
axes[0, 1].set_xlabel("Penjualan (Juta Rp)")

# Plot 3: Distribusi penjualan harian (histogram)
axes[1, 0].hist(
    penjualan_harian / 1e6, bins=10, color="#2ecc71", edgecolor="white", alpha=0.8
)
axes[1, 0].axvline(
    np.mean(penjualan_harian) / 1e6,
    color="red",
    linestyle="--",
    label=f"Mean: {np.mean(penjualan_harian) / 1e6:.1f} jt",
)
axes[1, 0].set_title("Distribusi Penjualan Harian", fontweight="bold")
axes[1, 0].set_xlabel("Penjualan (Juta Rp)")
axes[1, 0].set_ylabel("Frekuensi")
axes[1, 0].legend()
axes[1, 0].grid(axis="y", alpha=0.3)

# Plot 4: Proporsi penjualan (pie)
axes[1, 1].pie(
    [x / 1e6 for x in produk_total],
    labels=produk_nama,
    autopct="%1.1f%%",
    colors=colors_bar,
    startangle=90,
    textprops={"fontsize": 10},
)
axes[1, 1].set_title("Proporsi Penjualan per Produk", fontweight="bold")

plt.tight_layout()
plt.savefig("chapter_5/plot_07_dashboard.png", dpi=150)
plt.close()
print("  Tersimpan: chapter_5/plot_07_dashboard.png")

# ============================================
# Ringkasan
# ============================================
print("\n" + "=" * 60)
print("RINGKASAN VISUALISASI")
print("=" * 60)
print("""
File yang dihasilkan:
  1. plot_01_line.png      - Line Plot (tren data)
  2. plot_02_bar.png       - Bar Chart (perbandingan kategori)
  3. plot_03_histogram.png - Histogram & Box Plot (distribusi)
  4. plot_04_scatter.png   - Scatter Plot (korelasi)
  5. plot_05_pie.png       - Pie Chart (proporsi)
  6. plot_06_heatmap.png   - Heatmap (matriks korelasi)
  7. plot_07_dashboard.png - Dashboard (subplot gabungan)

Panduan Memilih Jenis Grafik:
  - Tren waktu          -> Line Plot
  - Perbandingan        -> Bar Chart
  - Distribusi          -> Histogram / Box Plot
  - Hubungan 2 variabel -> Scatter Plot
  - Proporsi            -> Pie Chart
  - Korelasi banyak var -> Heatmap
  - Ringkasan lengkap   -> Dashboard (subplot)
""")
