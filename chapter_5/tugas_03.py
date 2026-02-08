"""
==========================================================
 TUGAS 3 - Handling Missing Data
 Chapter 5: NumPy & Pandas
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Buat DataFrame dengan data yang sengaja memiliki NaN
    (minimal 3 kolom, 10-15 baris)
 2. Deteksi missing values: isnull().sum() per kolom
 3. Hitung persentase missing per kolom
 4. Buat 3 versi penanganan:
    - Versi 1: dropna() — hapus baris yang memiliki NaN
    - Versi 2: fillna() — isi numerik dengan mean,
               kategorikal dengan mode
    - Versi 3: fillna(method="ffill") — forward fill
 5. Bandingkan jumlah baris ketiga versi
 6. Berikan komentar kapan metode mana yang tepat digunakan

 Catatan:
 - Gunakan np.nan untuk membuat missing values
 - Buat data yang realistis (misal: data survei/kuesioner)
==========================================================
"""

import pandas as pd
import numpy as np


def buat_data_dengan_missing():
    """Membuat DataFrame dengan data yang memiliki missing values.

    Buat data realistis (misal: survei mahasiswa) dengan 10-15 baris
    dan minimal 3 kolom. Sisipkan np.nan di beberapa posisi.

    Returns:
        pd.DataFrame: DataFrame dengan missing values.
    """
    # TODO: Buat DataFrame dengan NaN di beberapa sel
    # Contoh skenario: data survei mahasiswa
    #
    # data = {
    #     "Nama": ["Ahmad", "Budi", "Citra", "Dewi", "Eko",
    #              "Fitri", "Gilang", "Hana", "Irfan", "Jasmine",
    #              "Kamal", "Lina"],
    #     "Usia": [20, 21, np.nan, 22, 20, np.nan, 23, 21, 20, np.nan, 22, 21],
    #     "IPK": [3.5, np.nan, 3.2, 3.8, np.nan, 3.1, 3.6, np.nan, 3.4, 3.7, np.nan, 3.3],
    #     "Jurusan": ["Informatika", "SI", np.nan, "Informatika", "Elektro",
    #                 "SI", np.nan, "Informatika", "Elektro", np.nan,
    #                 "SI", "Informatika"],
    #     "Skor_Survei": [85, 90, 78, np.nan, 88, 92, np.nan, 75, np.nan, 80, 95, np.nan],
    # }
    #
    # return pd.DataFrame(data)
    ...


def deteksi_missing(df):
    """Mendeteksi dan menampilkan informasi missing values.

    Args:
        df (pd.DataFrame): DataFrame yang mungkin memiliki NaN.

    Returns:
        tuple: (jumlah_missing_per_kolom, persen_missing_per_kolom)
    """
    # TODO: Hitung jumlah NaN per kolom
    # jumlah = df.isnull().sum()
    #
    # TODO: Hitung persentase NaN per kolom
    # persen = (df.isnull().sum() / len(df)) * 100
    #
    # return jumlah, persen
    ...


def versi_dropna(df):
    """Versi 1: Menghapus baris yang mengandung NaN.

    Args:
        df (pd.DataFrame): DataFrame asli.

    Returns:
        pd.DataFrame: DataFrame tanpa baris yang memiliki NaN.
    """
    # TODO: Implementasikan dropna()
    # return df.dropna()
    ...


def versi_fillna_statistik(df):
    """Versi 2: Mengisi NaN — numerik dengan mean, kategorikal dengan mode.

    Args:
        df (pd.DataFrame): DataFrame asli.

    Returns:
        pd.DataFrame: DataFrame dengan NaN terisi.
    """
    # TODO: Buat copy DataFrame agar tidak mengubah aslinya
    # df_filled = df.copy()
    #
    # TODO: Untuk setiap kolom numerik, isi NaN dengan mean
    # for col in df_filled.select_dtypes(include=["number"]).columns:
    #     df_filled[col] = df_filled[col].fillna(df_filled[col].mean())
    #
    # TODO: Untuk setiap kolom kategorikal/object, isi NaN dengan mode
    # for col in df_filled.select_dtypes(include=["object"]).columns:
    #     df_filled[col] = df_filled[col].fillna(df_filled[col].mode()[0])
    #
    # return df_filled
    ...


def versi_fillna_ffill(df):
    """Versi 3: Mengisi NaN dengan forward fill (nilai sebelumnya).

    Args:
        df (pd.DataFrame): DataFrame asli.

    Returns:
        pd.DataFrame: DataFrame dengan NaN terisi (ffill).
    """
    # TODO: Implementasikan ffill
    # return df.ffill()
    ...


def bandingkan_hasil(df_asli, df_dropna, df_fillna_stat, df_fillna_ffill):
    """Membandingkan jumlah baris dan sisa NaN dari ketiga versi.

    Args:
        df_asli (pd.DataFrame): DataFrame asli.
        df_dropna (pd.DataFrame): Hasil dropna.
        df_fillna_stat (pd.DataFrame): Hasil fillna statistik.
        df_fillna_ffill (pd.DataFrame): Hasil fillna ffill.
    """
    # TODO: Tampilkan perbandingan
    # print(f"{'Metode':<25} | {'Baris':>5} | {'NaN Tersisa':>11}")
    # print("-" * 48)
    # print(f"{'Data Asli':<25} | {len(df_asli):>5} | {df_asli.isnull().sum().sum():>11}")
    # print(f"{'dropna()':<25} | {len(df_dropna):>5} | {df_dropna.isnull().sum().sum():>11}")
    # print(f"{'fillna (mean/mode)':<25} | {len(df_fillna_stat):>5} | {df_fillna_stat.isnull().sum().sum():>11}")
    # print(f"{'fillna (ffill)':<25} | {len(df_fillna_ffill):>5} | {df_fillna_ffill.isnull().sum().sum():>11}")
    ...


# ── Kapan Menggunakan Metode Mana? ──────────────────────────────────────────
#
# TODO: Lengkapi penjelasan di bawah berdasarkan pemahaman Anda
#
# dropna():
#   - Gunakan ketika: ...
#   - Risiko: ...
#   - Contoh kasus: ...
#
# fillna(mean/mode):
#   - Gunakan ketika: ...
#   - Risiko: ...
#   - Contoh kasus: ...
#
# fillna(ffill):
#   - Gunakan ketika: ...
#   - Risiko: ...
#   - Contoh kasus: ...


# ── Main Program ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # TODO: Jalankan semua fungsi dan tampilkan hasilnya
    #
    # df = buat_data_dengan_missing()
    #
    # print("=" * 55)
    # print(" HANDLING MISSING DATA")
    # print("=" * 55)
    #
    # print("\n── Data Asli ──")
    # print(df)
    #
    # print("\n── Deteksi Missing Values ──")
    # jumlah, persen = deteksi_missing(df)
    # print(f"Jumlah NaN per kolom:\n{jumlah}")
    # print(f"\nPersentase NaN per kolom:\n{persen.round(1)}")
    #
    # print("\n── Versi 1: dropna() ──")
    # df_v1 = versi_dropna(df)
    # print(df_v1)
    #
    # print("\n── Versi 2: fillna (mean/mode) ──")
    # df_v2 = versi_fillna_statistik(df)
    # print(df_v2)
    #
    # print("\n── Versi 3: fillna (ffill) ──")
    # df_v3 = versi_fillna_ffill(df)
    # print(df_v3)
    #
    # print("\n── Perbandingan Hasil ──")
    # bandingkan_hasil(df, df_v1, df_v2, df_v3)

    pass
