"""
==========================================================
 TUGAS 2 - Regresi Prediksi Nilai Mahasiswa
 Chapter 6: Machine Learning & AI
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Buat dataset sintetis 200 mahasiswa dengan fitur:
    - jam_belajar (0-20 jam/minggu)
    - kehadiran (50-100 persen)
    - tugas_selesai (0-10 tugas)
    - nilai_uts (0-100)
    Target: nilai_akhir = kombinasi linear + noise
 2. Split data 80:20, random_state=42
 3. Linear Regression:
    - Tampilkan koefisien dan intercept
    - Hitung MSE, RMSE, MAE, R-squared
 4. Polynomial Regression (degree=2):
    - Hitung metrik yang sama
 5. Prediksi untuk 5 mahasiswa baru
 6. Buat tabel perbandingan Linear vs Polynomial
 7. Analisis interpretasi koefisien

 Formula target (contoh):
   nilai_akhir = 2*jam_belajar + 0.3*kehadiran +
                 3*tugas_selesai + 0.2*nilai_uts + noise
==========================================================
"""

# TODO: Uncomment import yang diperlukan
# import numpy as np
# from sklearn.linear_model import LinearRegression
# from sklearn.preprocessing import PolynomialFeatures
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Agar hasil random konsisten
np.random.seed(42)

# 1. Generate Dataset (200 sampel)
n = 200
jam_belajar = np.random.uniform(0, 20, n)
kehadiran = np.random.uniform(50, 100, n)
tugas_selesai = np.random.randint(0, 11, n)
nilai_uts = np.random.uniform(0, 100, n)

# Target: nilai_akhir (Kombinasi linear + noise)
# Rumus hipotesis: 1.5*jam + 0.2*hadir + 2*tugas + 0.4*uts + noise
noise = np.random.normal(0, 2, n)
nilai_akhir = (1.5 * jam_belajar) + (0.2 * kehadiran) + (2.0 * tugas_selesai) + (0.4 * nilai_uts) + noise
nilai_akhir = np.clip(nilai_akhir, 0, 100)

df = pd.DataFrame({
    'jam_belajar': jam_belajar,
    'kehadiran': kehadiran,
    'tugas_selesai': tugas_selesai,
    'nilai_uts': nilai_uts,
    'nilai_akhir': nilai_akhir
})

# 2. Train/Test Split (80:20)
X = df.drop('nilai_akhir', axis=1)
y = df['nilai_akhir']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Latih Model Linear Regression
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
y_pred_lr = lr_model.predict(X_test)

# 4. Latih Model Polynomial Regression (degree=2)
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)
y_pred_poly = poly_model.predict(X_test_poly)

# Fungsi untuk evaluasi
def evaluate(y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    return mse, rmse, mae, r2

# 5. Tabel Perbandingan
res_lr = evaluate(y_test, y_pred_lr)
res_poly = evaluate(y_test, y_pred_poly)

print("===== PERBANDINGAN MODEL REGRESI =====")
data_compare = {
    'Metric': ['MSE', 'RMSE', 'MAE', 'R-squared'],
    'Linear': res_lr,
    'Polynomial (deg=2)': res_poly
}
print(pd.DataFrame(data_compare).to_string(index=False))

# 6. Interpretasi Koefisien (Linear)
print("\n--- Interpretasi Koefisien (Linear) ---")
coeff_df = pd.DataFrame({'Fitur': X.columns, 'Koefisien': lr_model.coef_})
for _, row in coeff_df.iterrows():
    print(f"{row['Fitur']:<15}: {row['Koefisien']:+.2f}")

# 7. Prediksi 5 Mahasiswa Baru
data_baru = np.array([
    [15, 95, 9, 85], # Safriamsah
    [3, 60, 4, 50],
    [10, 80, 7, 70],
    [18, 98, 10, 90],
    [5, 55, 2, 40]
])
df_baru = pd.DataFrame(data_baru, columns=X.columns)
pred_akhir = lr_model.predict(df_baru)

print("\n===== PREDIKSI NILAI AKHIR MAHASISWA (LINEAR) =====")
print(f"{'No':<2} | {'Jam':<3} | {'Hadir':<5} | {'Tugas':<5} | {'UTS':<4} | {'Prediksi'}")
print("-" * 50)
for i, (row, pred) in enumerate(zip(data_baru, pred_akhir), 1):
    print(f"{i:<2} | {int(row[0]):<3} | {int(row[1]):<4}% | {int(row[2]):<5} | {int(row[3]):<4} | {pred:.1f}")

"""
ANALISIS:
1. Fitur paling berpengaruh: 'tugas_selesai' (koefisien tertinggi), diikuti 'jam_belajar'.
2. R-squared mendekati 1.0 menunjukkan model sangat akurat dalam menjelaskan variasi nilai.
3. Polynomial Regression memberikan hasil sedikit lebih baik jika hubungan data tidak benar-benar lurus.
"""
