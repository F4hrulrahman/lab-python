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


# ============================================
# 1. Membuat Dataset
# ============================================
def buat_dataset(n_samples=200, random_state=42):
    """Buat dataset sintetis prediksi nilai mahasiswa.

    Args:
        n_samples (int): Jumlah sampel (default 200).
        random_state (int): Random seed.

    Returns:
        tuple: (X, y, feature_names)
               X = feature matrix (n_samples, 4)
               y = target array (nilai_akhir)
               feature_names = list nama fitur
    """
    # TODO: Set random seed
    # np.random.seed(random_state)
    #
    # TODO: Generate fitur-fitur
    # jam_belajar = np.random.uniform(0, 20, n_samples)       # 0-20 jam/minggu
    # kehadiran = np.random.uniform(50, 100, n_samples)       # 50-100%
    # tugas_selesai = np.random.randint(0, 11, n_samples).astype(float)  # 0-10
    # nilai_uts = np.random.uniform(0, 100, n_samples)        # 0-100
    #
    # TODO: Buat target (nilai_akhir) sebagai kombinasi linear + noise
    # noise = np.random.normal(0, 5, n_samples)
    # nilai_akhir = (
    #     2.0 * jam_belajar
    #     + 0.3 * kehadiran
    #     + 3.0 * tugas_selesai
    #     + 0.2 * nilai_uts
    #     + noise
    # )
    #
    # TODO: Clip nilai agar dalam range 0-100
    # nilai_akhir = np.clip(nilai_akhir, 0, 100)
    #
    # TODO: Buat feature matrix
    # X = np.column_stack([jam_belajar, kehadiran, tugas_selesai, nilai_uts])
    # feature_names = ["Jam Belajar", "Kehadiran (%)", "Tugas Selesai", "Nilai UTS"]
    #
    # TODO: Tampilkan info dataset
    # print(f"Jumlah sampel : {n_samples}")
    # print(f"Jumlah fitur  : {len(feature_names)}")
    # print(f"Fitur         : {feature_names}")
    # print(f"\nStatistik fitur:")
    # for i, name in enumerate(feature_names):
    #     print(f"  {name:20s}: min={X[:, i].min():.1f}, max={X[:, i].max():.1f}, mean={X[:, i].mean():.1f}")
    # print(f"  {'Nilai Akhir':20s}: min={nilai_akhir.min():.1f}, max={nilai_akhir.max():.1f}, mean={nilai_akhir.mean():.1f}")
    #
    # return X, nilai_akhir, feature_names
    ...


# ============================================
# 2. Preprocessing (Train/Test Split)
# ============================================
def split_data(X, y):
    """Split data menjadi training dan testing set.

    Args:
        X (ndarray): Feature matrix.
        y (ndarray): Target array.

    Returns:
        tuple: (X_train, X_test, y_train, y_test)
    """
    # TODO: Split 80:20 dengan random_state=42
    # X_train, X_test, y_train, y_test = train_test_split(
    #     X, y, test_size=0.2, random_state=42
    # )
    #
    # TODO: Tampilkan info split
    # print(f"Total data    : {len(X)}")
    # print(f"Training data : {len(X_train)} ({len(X_train)/len(X)*100:.0f}%)")
    # print(f"Testing data  : {len(X_test)} ({len(X_test)/len(X)*100:.0f}%)")
    #
    # return X_train, X_test, y_train, y_test
    ...


# ============================================
# 3. Linear Regression
# ============================================
def train_linear_regression(X_train, X_test, y_train, y_test, feature_names):
    """Train dan evaluasi Linear Regression.

    Args:
        X_train (ndarray): Training features.
        X_test (ndarray): Testing features.
        y_train (ndarray): Training target.
        y_test (ndarray): Testing target.
        feature_names (list): Nama fitur.

    Returns:
        tuple: (model, mse, rmse, mae, r2, y_pred)
    """
    # TODO: Train model
    # model_lr = LinearRegression()
    # model_lr.fit(X_train, y_train)
    #
    # TODO: Tampilkan persamaan regresi
    # print("Persamaan regresi:")
    # print(f"  nilai_akhir = ", end="")
    # terms = []
    # for name, coef in zip(feature_names, model_lr.coef_):
    #     terms.append(f"{coef:.4f} * {name}")
    # print(" + ".join(terms))
    # print(f"  + {model_lr.intercept_:.4f} (intercept)")
    #
    # TODO: Prediksi
    # y_pred_lr = model_lr.predict(X_test)
    #
    # TODO: Hitung metrik evaluasi
    # mse = mean_squared_error(y_test, y_pred_lr)
    # rmse = np.sqrt(mse)
    # mae = mean_absolute_error(y_test, y_pred_lr)
    # r2 = r2_score(y_test, y_pred_lr)
    #
    # TODO: Tampilkan metrik
    # print(f"\nMetrik Evaluasi:")
    # print(f"  MSE  (Mean Squared Error)    : {mse:.4f}")
    # print(f"  RMSE (Root Mean Squared Error): {rmse:.4f}")
    # print(f"  MAE  (Mean Absolute Error)   : {mae:.4f}")
    # print(f"  R²   (R-Squared)            : {r2:.4f}")
    # print(f"  R² artinya model menjelaskan {r2*100:.1f}% variasi data")
    #
    # TODO: Tampilkan koefisien dengan interpretasi
    # print(f"\nInterpretasi Koefisien:")
    # for name, coef in zip(feature_names, model_lr.coef_):
    #     arah = "menaikkan" if coef > 0 else "menurunkan"
    #     print(f"  {name:20s}: {coef:+.4f} (setiap +1 unit {arah} nilai sebesar {abs(coef):.2f})")
    #
    # return model_lr, mse, rmse, mae, r2, y_pred_lr
    ...


# ============================================
# 4. Polynomial Regression (degree=2)
# ============================================
def train_polynomial_regression(X_train, X_test, y_train, y_test, degree=2):
    """Train dan evaluasi Polynomial Regression.

    Args:
        X_train (ndarray): Training features.
        X_test (ndarray): Testing features.
        y_train (ndarray): Training target.
        y_test (ndarray): Testing target.
        degree (int): Derajat polynomial (default 2).

    Returns:
        tuple: (model, poly_transformer, mse, rmse, mae, r2, y_pred)
    """
    # TODO: Transformasi fitur ke polynomial
    # poly = PolynomialFeatures(degree=degree, include_bias=False)
    # X_train_poly = poly.fit_transform(X_train)
    # X_test_poly = poly.transform(X_test)
    #
    # TODO: Tampilkan info transformasi
    # print(f"Degree             : {degree}")
    # print(f"Fitur awal         : {X_train.shape[1]}")
    # print(f"Fitur setelah poly : {X_train_poly.shape[1]}")
    #
    # TODO: Train model
    # model_poly = LinearRegression()
    # model_poly.fit(X_train_poly, y_train)
    #
    # TODO: Prediksi
    # y_pred_poly = model_poly.predict(X_test_poly)
    #
    # TODO: Hitung metrik evaluasi
    # mse = mean_squared_error(y_test, y_pred_poly)
    # rmse = np.sqrt(mse)
    # mae = mean_absolute_error(y_test, y_pred_poly)
    # r2 = r2_score(y_test, y_pred_poly)
    #
    # TODO: Tampilkan metrik
    # print(f"\nMetrik Evaluasi:")
    # print(f"  MSE  : {mse:.4f}")
    # print(f"  RMSE : {rmse:.4f}")
    # print(f"  MAE  : {mae:.4f}")
    # print(f"  R²   : {r2:.4f} ({r2*100:.1f}%)")
    #
    # return model_poly, poly, mse, rmse, mae, r2, y_pred_poly
    ...


# ============================================
# 5. Prediksi Mahasiswa Baru
# ============================================
def prediksi_mahasiswa_baru(model_lr, model_poly, poly_transformer, feature_names):
    """Prediksi nilai akhir untuk 5 mahasiswa baru.

    Args:
        model_lr: Model Linear Regression.
        model_poly: Model Polynomial Regression.
        poly_transformer: PolynomialFeatures transformer.
        feature_names (list): Nama fitur.
    """
    # TODO: Buat 5 data mahasiswa baru
    # mahasiswa_baru = np.array([
    #     [15, 90, 9, 85],   # Rajin, kehadiran tinggi
    #     [5, 60, 4, 50],    # Kurang rajin
    #     [10, 80, 7, 70],   # Rata-rata
    #     [20, 95, 10, 95],  # Sangat rajin
    #     [2, 55, 2, 30],    # Kurang motivasi
    # ])
    #
    # deskripsi = [
    #     "Rajin belajar",
    #     "Kurang rajin",
    #     "Rata-rata",
    #     "Sangat rajin",
    #     "Kurang motivasi",
    # ]
    #
    # TODO: Prediksi dengan kedua model
    # pred_lr = model_lr.predict(mahasiswa_baru)
    # mhs_poly = poly_transformer.transform(mahasiswa_baru)
    # pred_poly = model_poly.predict(mhs_poly)
    #
    # TODO: Tampilkan hasil
    # print(f"{'No':>2} | {'Profil':<18} | {'Jam':>4} | {'Hadir':>5} | {'Tugas':>5} | {'UTS':>4} | {'LR':>7} | {'Poly':>7}")
    # print("-" * 80)
    # for i, (mhs, desc, p_lr, p_poly) in enumerate(
    #     zip(mahasiswa_baru, deskripsi, pred_lr, pred_poly), 1
    # ):
    #     print(f"{i:>2} | {desc:<18} | {mhs[0]:>4.0f} | {mhs[1]:>5.0f} | {mhs[2]:>5.0f} | {mhs[3]:>4.0f} | {p_lr:>7.2f} | {p_poly:>7.2f}")
    ...


# ============================================
# 6. Perbandingan Model
# ============================================
def perbandingan_model(hasil_lr, hasil_poly):
    """Buat tabel perbandingan Linear vs Polynomial Regression.

    Args:
        hasil_lr (dict): {'mse': ..., 'rmse': ..., 'mae': ..., 'r2': ...}
        hasil_poly (dict): {'mse': ..., 'rmse': ..., 'mae': ..., 'r2': ...}
    """
    # TODO: Buat tabel perbandingan
    # print(f"{'Metrik':<30} | {'Linear':>12} | {'Polynomial':>12} | {'Lebih Baik':<12}")
    # print("-" * 75)
    #
    # metrics = [
    #     ("MSE", hasil_lr['mse'], hasil_poly['mse'], "lower"),
    #     ("RMSE", hasil_lr['rmse'], hasil_poly['rmse'], "lower"),
    #     ("MAE", hasil_lr['mae'], hasil_poly['mae'], "lower"),
    #     ("R-Squared", hasil_lr['r2'], hasil_poly['r2'], "higher"),
    # ]
    #
    # for name, val_lr, val_poly, better in metrics:
    #     if better == "lower":
    #         winner = "Linear" if val_lr < val_poly else "Polynomial"
    #     else:
    #         winner = "Linear" if val_lr > val_poly else "Polynomial"
    #     print(f"{name:<30} | {val_lr:>12.4f} | {val_poly:>12.4f} | {winner:<12}")
    #
    # TODO: Kesimpulan
    # if hasil_poly['r2'] > hasil_lr['r2']:
    #     print(f"\nKesimpulan: Polynomial Regression lebih baik (R² lebih tinggi)")
    # else:
    #     print(f"\nKesimpulan: Linear Regression lebih baik (R² lebih tinggi)")
    # print("Catatan: Jika perbedaan kecil, pilih Linear karena lebih sederhana (prinsip Occam's Razor)")
    ...


# ============================================
# 7. Analisis Koefisien
# ============================================
def analisis_koefisien():
    """Tulis analisis interpretasi koefisien regresi."""
    # TODO: Tulis analisis dalam bentuk print statement
    # Jawab pertanyaan berikut:
    # 1. Fitur mana yang paling berpengaruh terhadap nilai akhir?
    # 2. Apakah koefisien sesuai dengan formula awal?
    #    (formula: 2*jam + 0.3*kehadiran + 3*tugas + 0.2*uts)
    # 3. Apakah Polynomial Regression signifikan lebih baik?
    # 4. Apa rekomendasi untuk mahasiswa yang ingin meningkatkan nilai?
    #
    # Contoh:
    # print("=" * 50)
    # print("ANALISIS KOEFISIEN REGRESI")
    # print("=" * 50)
    # print("""
    # 1. Fitur paling berpengaruh: ...
    #    Koefisien: ...
    #
    # 2. Perbandingan dengan formula awal:
    #    - jam_belajar: expected=2.0, actual=...
    #    - kehadiran: expected=0.3, actual=...
    #    - tugas_selesai: expected=3.0, actual=...
    #    - nilai_uts: expected=0.2, actual=...
    #
    # 3. Linear vs Polynomial: ...
    #
    # 4. Rekomendasi untuk mahasiswa:
    #    - ...
    # """)
    ...


# ── Main Program ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # TODO: Jalankan semua fungsi secara berurutan
    # print("=" * 60)
    # print("TUGAS 2 - REGRESI PREDIKSI NILAI MAHASISWA")
    # print("=" * 60)
    #
    # # 1. Buat dataset
    # print("\n=== 1. Membuat Dataset ===")
    # X, y, feature_names = buat_dataset()
    #
    # # 2. Split data
    # print("\n=== 2. Train/Test Split ===")
    # X_train, X_test, y_train, y_test = split_data(X, y)
    #
    # # 3. Linear Regression
    # print("\n=== 3. Linear Regression ===")
    # model_lr, mse_lr, rmse_lr, mae_lr, r2_lr, y_pred_lr = train_linear_regression(
    #     X_train, X_test, y_train, y_test, feature_names
    # )
    #
    # # 4. Polynomial Regression
    # print("\n=== 4. Polynomial Regression (degree=2) ===")
    # model_poly, poly_trans, mse_poly, rmse_poly, mae_poly, r2_poly, y_pred_poly = (
    #     train_polynomial_regression(X_train, X_test, y_train, y_test, degree=2)
    # )
    #
    # # 5. Prediksi mahasiswa baru
    # print("\n=== 5. Prediksi Mahasiswa Baru ===")
    # prediksi_mahasiswa_baru(model_lr, model_poly, poly_trans, feature_names)
    #
    # # 6. Perbandingan
    # print("\n=== 6. Perbandingan Model ===")
    # perbandingan_model(
    #     {'mse': mse_lr, 'rmse': rmse_lr, 'mae': mae_lr, 'r2': r2_lr},
    #     {'mse': mse_poly, 'rmse': rmse_poly, 'mae': mae_poly, 'r2': r2_poly},
    # )
    #
    # # 7. Analisis
    # print("\n=== 7. Analisis Koefisien ===")
    # analisis_koefisien()

    pass
