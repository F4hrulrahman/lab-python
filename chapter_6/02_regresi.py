"""
Chapter 6 - Bagian 2: Regresi
================================
Regresi adalah tipe supervised learning di mana model belajar
memprediksi NILAI KONTINU dari data.

Contoh: Prediksi harga rumah, suhu, gaji, harga saham.

Install: pip install scikit-learn numpy matplotlib
"""

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# ============================================
# 1. Konsep Regresi
# ============================================
print("=" * 60)
print("REGRESI DENGAN SCIKIT-LEARN")
print("=" * 60)

print("\n=== 1. Konsep Regresi ===")
print("Regresi = memprediksi nilai kontinu")
print("  Linear Regression: y = mx + b (garis lurus)")
print("  Tujuan: menemukan garis yang paling 'cocok' dengan data")

# ============================================
# 2. Membuat Dataset
# ============================================
print("\n=== 2. Membuat Dataset ===")

np.random.seed(42)

# Dataset: Pengalaman kerja (tahun) vs Gaji (juta rupiah)
n_samples = 50
pengalaman = np.random.uniform(0, 15, n_samples)  # 0-15 tahun
noise = np.random.normal(0, 2, n_samples)  # Random noise

# Hubungan: gaji = 3 * pengalaman + 5 + noise
gaji = 3 * pengalaman + 5 + noise

print(f"Jumlah data: {n_samples}")
print(f"Pengalaman: min={pengalaman.min():.1f}, max={pengalaman.max():.1f} tahun")
print(f"Gaji: min={gaji.min():.1f}, max={gaji.max():.1f} juta")

# Reshape untuk sklearn (butuh 2D array)
X = pengalaman.reshape(-1, 1)
y = gaji

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"\nTraining: {len(X_train)} sampel")
print(f"Testing:  {len(X_test)} sampel")

# ============================================
# 3. Linear Regression
# ============================================
print("\n=== 3. Linear Regression ===")

model_lr = LinearRegression()
model_lr.fit(X_train, y_train)

# Koefisien model
print(f"Persamaan: y = {model_lr.coef_[0]:.4f} * x + {model_lr.intercept_:.4f}")
print(f"  (Seharusnya mendekati: y = 3x + 5)")

# Prediksi
y_pred_lr = model_lr.predict(X_test)

# Evaluasi
mse = mean_squared_error(y_test, y_pred_lr)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred_lr)
r2 = r2_score(y_test, y_pred_lr)

print(f"\nMetrik Evaluasi:")
print(f"  MSE  (Mean Squared Error)    : {mse:.4f}")
print(f"  RMSE (Root Mean Squared Error): {rmse:.4f}")
print(f"  MAE  (Mean Absolute Error)   : {mae:.4f}")
print(f"  R²   (R-Squared)            : {r2:.4f}")
print(f"  R² artinya model menjelaskan {r2 * 100:.1f}% variasi data")

# Prediksi untuk pengalaman baru
print("\nPrediksi gaji:")
tahun_baru = [1, 5, 10, 15]
for t in tahun_baru:
    pred = model_lr.predict([[t]])[0]
    print(f"  {t:2d} tahun pengalaman -> Rp{pred:.1f} juta")

# ============================================
# 4. Polynomial Regression
# ============================================
print("\n=== 4. Polynomial Regression ===")
print("Untuk data yang hubungannya non-linear")

# Dataset non-linear
np.random.seed(42)
X_nl = np.linspace(0, 10, 100).reshape(-1, 1)
y_nl = 0.5 * X_nl.ravel() ** 2 - 3 * X_nl.ravel() + 10 + np.random.normal(0, 3, 100)

X_nl_train, X_nl_test, y_nl_train, y_nl_test = train_test_split(
    X_nl, y_nl, test_size=0.2, random_state=42
)

# Linear Regression pada data non-linear
lr_nonlin = LinearRegression()
lr_nonlin.fit(X_nl_train, y_nl_train)
y_pred_lr_nl = lr_nonlin.predict(X_nl_test)
r2_lr = r2_score(y_nl_test, y_pred_lr_nl)

# Polynomial Regression (degree=2)
poly = PolynomialFeatures(degree=2)
X_nl_train_poly = poly.fit_transform(X_nl_train)
X_nl_test_poly = poly.transform(X_nl_test)

pr = LinearRegression()
pr.fit(X_nl_train_poly, y_nl_train)
y_pred_pr = pr.predict(X_nl_test_poly)
r2_pr = r2_score(y_nl_test, y_pred_pr)

print(f"Linear Regression R²    : {r2_lr:.4f}")
print(f"Polynomial Regression R²: {r2_pr:.4f}")
print(f"  Polynomial jauh lebih baik untuk data non-linear!")

# ============================================
# 5. Multiple Linear Regression
# ============================================
print("\n=== 5. Multiple Linear Regression ===")
print("Regresi dengan beberapa fitur (variabel independen)")

# Dataset: prediksi harga rumah
np.random.seed(42)
n = 200

luas = np.random.uniform(30, 200, n)  # Luas (m²)
kamar = np.random.randint(1, 6, n).astype(float)  # Jumlah kamar
jarak_pusat = np.random.uniform(1, 30, n)  # Jarak ke pusat kota (km)
umur_bangunan = np.random.uniform(0, 30, n)  # Umur bangunan (tahun)

# Harga (dalam juta Rp) = fungsi dari fitur-fitur di atas
harga = (
    5 * luas
    + 50 * kamar
    - 10 * jarak_pusat
    - 3 * umur_bangunan
    + 100
    + np.random.normal(0, 30, n)
)

# Buat feature matrix
X_rumah = np.column_stack([luas, kamar, jarak_pusat, umur_bangunan])
y_rumah = harga

fitur_nama = ["Luas (m²)", "Jumlah Kamar", "Jarak Pusat (km)", "Umur Bangunan (th)"]

X_r_train, X_r_test, y_r_train, y_r_test = train_test_split(
    X_rumah, y_rumah, test_size=0.2, random_state=42
)

model_rumah = LinearRegression()
model_rumah.fit(X_r_train, y_r_train)
y_r_pred = model_rumah.predict(X_r_test)

r2_rumah = r2_score(y_r_test, y_r_pred)
rmse_rumah = np.sqrt(mean_squared_error(y_r_test, y_r_pred))

print(f"\nR² Score : {r2_rumah:.4f}")
print(f"RMSE     : Rp{rmse_rumah:.1f} juta")

print(f"\nKoefisien model:")
print(f"  Intercept: {model_rumah.intercept_:.2f}")
for nama, koef in zip(fitur_nama, model_rumah.coef_):
    arah = "+" if koef > 0 else ""
    print(f"  {nama:25s}: {arah}{koef:.2f}")

print("\nInterpretasi:")
print(f"  Setiap 1 m² tambahan luas    -> harga naik Rp{model_rumah.coef_[0]:.1f} juta")
print(f"  Setiap 1 kamar tambahan      -> harga naik Rp{model_rumah.coef_[1]:.1f} juta")
print(
    f"  Setiap 1 km lebih jauh       -> harga turun Rp{abs(model_rumah.coef_[2]):.1f} juta"
)

# Prediksi rumah baru
print("\nPrediksi harga rumah baru:")
rumah_baru = [
    [80, 3, 5, 2],  # Luas 80m², 3 kamar, 5km dari pusat, umur 2 tahun
    [120, 4, 10, 5],  # Luas 120m², 4 kamar, 10km, umur 5 tahun
    [50, 2, 20, 15],  # Luas 50m², 2 kamar, 20km, umur 15 tahun
]

for r in rumah_baru:
    pred = model_rumah.predict([r])[0]
    print(f"  Luas={r[0]}m², Kamar={int(r[1])}, Jarak={r[2]}km, Umur={r[3]}th")
    print(f"    -> Prediksi harga: Rp{pred:.0f} juta")

# ============================================
# 6. Penjelasan Metrik Evaluasi
# ============================================
print("\n=== 6. Penjelasan Metrik ===")
print("""
MSE  (Mean Squared Error)     : Rata-rata kuadrat error. Sensitif terhadap outlier.
RMSE (Root Mean Squared Error): Akar dari MSE. Satuan sama dengan target.
MAE  (Mean Absolute Error)    : Rata-rata absolute error. Lebih robust terhadap outlier.
R²   (R-Squared)             : 0-1, seberapa baik model menjelaskan variasi data.
                                1.0 = sempurna, 0.0 = sama buruknya dengan rata-rata.
""")
