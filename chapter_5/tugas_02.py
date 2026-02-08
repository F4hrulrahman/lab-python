"""
==========================================================
 TUGAS 2 - Analisis Data Mahasiswa dengan Pandas
 Chapter 5: NumPy & Pandas
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Buat DataFrame 20 mahasiswa dengan kolom:
    Nama, NIM, Jurusan (3 pilihan), Semester (2-8),
    IPK (2.0-4.0), Jenis_Kelamin (L/P)
 2. Tampilkan info dasar: shape, dtypes, describe()
 3. Filter: mahasiswa IPK >= 3.5
 4. Filter: Jurusan "Informatika" DAN semester >= 5
 5. Sorting: urutkan berdasarkan IPK (descending), ambil top 5
 6. Groupby: statistik IPK per jurusan (mean, min, max, count)
 7. Groupby: jumlah mahasiswa per jenis_kelamin per jurusan
 8. Tambah kolom Predikat berdasarkan IPK
 9. Hitung distribusi predikat dengan value_counts()

 Predikat:
 | IPK >= 3.5 | Cum Laude          |
 | IPK >= 3.0 | Sangat Memuaskan   |
 | IPK >= 2.5 | Memuaskan          |
 | IPK <  2.5 | Cukup              |
==========================================================
"""

import pandas as pd
import numpy as np


def buat_dataframe_mahasiswa(seed=42):
    """Membuat DataFrame berisi data 20 mahasiswa.

    Args:
        seed (int): Random seed untuk reprodusibilitas.

    Returns:
        pd.DataFrame: DataFrame dengan kolom Nama, NIM, Jurusan,
                       Semester, IPK, Jenis_Kelamin.
    """
    # TODO: Set seed dan buat data
    # np.random.seed(seed)
    #
    # nama_list = [
    #     "Ahmad", "Budi", "Citra", "Dewi", "Eko",
    #     "Fitri", "Gilang", "Hana", "Irfan", "Jasmine",
    #     "Kamal", "Lina", "Mira", "Naufal", "Olivia",
    #     "Putra", "Qory", "Rizky", "Sari", "Taufik",
    # ]
    #
    # jurusan_list = ["Informatika", "Sistem Informasi", "Teknik Elektro"]
    #
    # data = {
    #     "Nama": nama_list,
    #     "NIM": [f"10520{i:04d}" for i in range(1, 21)],
    #     "Jurusan": np.random.choice(jurusan_list, 20),
    #     "Semester": np.random.randint(2, 9, 20),
    #     "IPK": np.round(np.random.uniform(2.0, 4.0, 20), 2),
    #     "Jenis_Kelamin": np.random.choice(["L", "P"], 20),
    # }
    #
    # return pd.DataFrame(data)
    ...


def info_dasar(df):
    """Menampilkan informasi dasar DataFrame.

    Args:
        df (pd.DataFrame): DataFrame mahasiswa.
    """
    # TODO: Tampilkan shape, dtypes, dan describe()
    # print(f"Shape: {df.shape}")
    # print(f"\nTipe Data:\n{df.dtypes}")
    # print(f"\nStatistik Deskriptif:\n{df.describe()}")
    ...


def filter_ipk_tinggi(df, batas_ipk=3.5):
    """Filter mahasiswa dengan IPK >= batas_ipk.

    Args:
        df (pd.DataFrame): DataFrame mahasiswa.
        batas_ipk (float): Batas minimum IPK.

    Returns:
        pd.DataFrame: DataFrame hasil filter.
    """
    # TODO: Implementasikan filter
    # return df[df["IPK"] >= batas_ipk]
    ...


def filter_jurusan_semester(df, jurusan="Informatika", min_semester=5):
    """Filter mahasiswa berdasarkan jurusan DAN minimum semester.

    Args:
        df (pd.DataFrame): DataFrame mahasiswa.
        jurusan (str): Nama jurusan.
        min_semester (int): Semester minimum.

    Returns:
        pd.DataFrame: DataFrame hasil filter.
    """
    # TODO: Implementasikan filter gabungan (AND)
    # return df[(df["Jurusan"] == jurusan) & (df["Semester"] >= min_semester)]
    ...


def top_mahasiswa(df, n=5):
    """Mengurutkan berdasarkan IPK dan mengambil top n mahasiswa.

    Args:
        df (pd.DataFrame): DataFrame mahasiswa.
        n (int): Jumlah mahasiswa teratas.

    Returns:
        pd.DataFrame: Top n mahasiswa berdasarkan IPK.
    """
    # TODO: Sort by IPK descending, ambil n pertama
    # return df.sort_values("IPK", ascending=False).head(n)
    ...


def statistik_per_jurusan(df):
    """Menghitung statistik IPK per jurusan menggunakan groupby.

    Args:
        df (pd.DataFrame): DataFrame mahasiswa.

    Returns:
        pd.DataFrame: Statistik IPK (mean, min, max, count) per jurusan.
    """
    # TODO: Implementasikan groupby + agg
    # return df.groupby("Jurusan")["IPK"].agg(["mean", "min", "max", "count"])
    ...


def jumlah_per_gender_jurusan(df):
    """Menghitung jumlah mahasiswa per jenis_kelamin per jurusan.

    Args:
        df (pd.DataFrame): DataFrame mahasiswa.

    Returns:
        pd.DataFrame: Tabel pivot jumlah per gender per jurusan.
    """
    # TODO: Implementasikan groupby dua kolom atau crosstab
    # return pd.crosstab(df["Jurusan"], df["Jenis_Kelamin"])
    ...


def tambah_predikat(df):
    """Menambah kolom Predikat berdasarkan IPK.

    Aturan:
        IPK >= 3.5 -> "Cum Laude"
        IPK >= 3.0 -> "Sangat Memuaskan"
        IPK >= 2.5 -> "Memuaskan"
        IPK <  2.5 -> "Cukup"

    Args:
        df (pd.DataFrame): DataFrame mahasiswa.

    Returns:
        pd.DataFrame: DataFrame dengan kolom Predikat baru.
    """
    # TODO: Gunakan np.select atau apply + fungsi
    # conditions = [
    #     df["IPK"] >= 3.5,
    #     df["IPK"] >= 3.0,
    #     df["IPK"] >= 2.5,
    # ]
    # choices = ["Cum Laude", "Sangat Memuaskan", "Memuaskan"]
    # df["Predikat"] = np.select(conditions, choices, default="Cukup")
    # return df
    ...


def distribusi_predikat(df):
    """Menampilkan distribusi predikat menggunakan value_counts().

    Args:
        df (pd.DataFrame): DataFrame yang sudah memiliki kolom Predikat.

    Returns:
        pd.Series: Jumlah per predikat.
    """
    # TODO: Implementasikan value_counts()
    # return df["Predikat"].value_counts()
    ...


# ── Main Program ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # TODO: Jalankan semua fungsi dan tampilkan hasilnya
    #
    # df = buat_dataframe_mahasiswa()
    #
    # print("=" * 60)
    # print(" ANALISIS DATA MAHASISWA (Pandas)")
    # print("=" * 60)
    #
    # print("\n── Info Dasar ──")
    # info_dasar(df)
    #
    # print("\n── Mahasiswa IPK >= 3.5 ──")
    # print(filter_ipk_tinggi(df))
    #
    # print("\n── Informatika & Semester >= 5 ──")
    # print(filter_jurusan_semester(df))
    #
    # print("\n── Top 5 Mahasiswa ──")
    # print(top_mahasiswa(df))
    #
    # print("\n── Statistik IPK per Jurusan ──")
    # print(statistik_per_jurusan(df))
    #
    # print("\n── Jumlah per Gender per Jurusan ──")
    # print(jumlah_per_gender_jurusan(df))
    #
    # df = tambah_predikat(df)
    # print("\n── DataFrame dengan Predikat ──")
    # print(df[["Nama", "IPK", "Predikat"]])
    #
    # print("\n── Distribusi Predikat ──")
    # print(distribusi_predikat(df))

    pass
