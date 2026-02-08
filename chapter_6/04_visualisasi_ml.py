"""
Chapter 6 - Visualisasi Machine Learning
==========================================
Panduan visualisasi hasil Machine Learning menggunakan Matplotlib.
Menampilkan grafik-grafik penting untuk evaluasi dan interpretasi
model klasifikasi, regresi, dan clustering.

Install: pip install matplotlib numpy scikit-learn
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris, make_blobs
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    r2_score,
    mean_squared_error,
    silhouette_score,
    ConfusionMatrixDisplay,
)

print("=" * 60)
print("VISUALISASI MACHINE LEARNING")
print("=" * 60)

# ============================================
# BAGIAN 1: VISUALISASI KLASIFIKASI
# ============================================
print("\n--- BAGIAN 1: KLASIFIKASI ---")

# Load dan persiapan data
iris = load_iris()
X_cls = iris.data
y_cls = iris.target

X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(
    X_cls, y_cls, test_size=0.2, random_state=42, stratify=y_cls
)

scaler_c = StandardScaler()
X_train_cs = scaler_c.fit_transform(X_train_c)
X_test_cs = scaler_c.transform(X_test_c)

# ── 1. Confusion Matrix Heatmap ──────────────────────────────────────────────
print("\n=== 1. Confusion Matrix Heatmap ===")

rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train_c, y_train_c)
y_pred_rf = rf.predict(X_test_c)

fig, ax = plt.subplots(figsize=(8, 6))
cm = confusion_matrix(y_test_c, y_pred_rf)
im = ax.imshow(cm, cmap="Blues")

# Labels
classes = iris.target_names
ax.set_xticks(range(len(classes)))
ax.set_yticks(range(len(classes)))
ax.set_xticklabels(classes, fontsize=11)
ax.set_yticklabels(classes, fontsize=11)

# Tambahkan angka di setiap cell
for i in range(len(classes)):
    for j in range(len(classes)):
        color = "white" if cm[i, j] > cm.max() / 2 else "black"
        ax.text(
            j,
            i,
            str(cm[i, j]),
            ha="center",
            va="center",
            fontsize=16,
            fontweight="bold",
            color=color,
        )

ax.set_xlabel("Prediksi", fontsize=12)
ax.set_ylabel("Aktual", fontsize=12)
ax.set_title(
    "Confusion Matrix - Random Forest\n(Dataset Iris)", fontsize=14, fontweight="bold"
)
plt.colorbar(im, ax=ax, shrink=0.8)

plt.tight_layout()
plt.savefig("chapter_6/plot_01_confusion_matrix.png", dpi=150)
plt.close()
print("  Tersimpan: chapter_6/plot_01_confusion_matrix.png")

# ── 2. Perbandingan Akurasi Model ────────────────────────────────────────────
print("\n=== 2. Perbandingan Akurasi Model ===")

models = {
    "KNN (k=3)": KNeighborsClassifier(n_neighbors=3),
    "KNN (k=5)": KNeighborsClassifier(n_neighbors=5),
    "KNN (k=7)": KNeighborsClassifier(n_neighbors=7),
    "Decision Tree": DecisionTreeClassifier(random_state=42, max_depth=3),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
}

accuracies = {}
for name, model in models.items():
    if "KNN" in name:
        model.fit(X_train_cs, y_train_c)
        acc = accuracy_score(y_test_c, model.predict(X_test_cs))
    else:
        model.fit(X_train_c, y_train_c)
        acc = accuracy_score(y_test_c, model.predict(X_test_c))
    accuracies[name] = acc

fig, ax = plt.subplots(figsize=(10, 6))
names = list(accuracies.keys())
accs = list(accuracies.values())
colors = ["#3498db", "#2980b9", "#1f6dad", "#e74c3c", "#2ecc71"]

bars = ax.barh(names, accs, color=colors, edgecolor="white", height=0.6)

for bar, acc in zip(bars, accs):
    ax.text(
        bar.get_width() + 0.005,
        bar.get_y() + bar.get_height() / 2,
        f"{acc:.1%}",
        va="center",
        fontweight="bold",
        fontsize=12,
    )

ax.set_xlim(0, 1.15)
ax.set_xlabel("Akurasi", fontsize=12)
ax.set_title(
    "Perbandingan Akurasi Model Klasifikasi\n(Dataset Iris)",
    fontsize=14,
    fontweight="bold",
)
ax.axvline(x=1.0, color="green", linestyle="--", alpha=0.3, label="Perfect (100%)")
ax.grid(axis="x", alpha=0.3)
ax.legend()

plt.tight_layout()
plt.savefig("chapter_6/plot_02_model_comparison.png", dpi=150)
plt.close()
print("  Tersimpan: chapter_6/plot_02_model_comparison.png")

# ── 3. Feature Importance ────────────────────────────────────────────────────
print("\n=== 3. Feature Importance (Random Forest) ===")

importances = rf.feature_importances_
indices = np.argsort(importances)

fig, ax = plt.subplots(figsize=(9, 6))
ax.barh(range(len(indices)), importances[indices], color="#3498db", edgecolor="white")
ax.set_yticks(range(len(indices)))
ax.set_yticklabels([iris.feature_names[i] for i in indices], fontsize=12)

for i, (idx, imp) in enumerate(zip(indices, importances[indices])):
    ax.text(imp + 0.01, i, f"{imp:.3f}", va="center", fontsize=11, fontweight="bold")

ax.set_xlabel("Importance", fontsize=12)
ax.set_title(
    "Feature Importance - Random Forest\n(Dataset Iris)", fontsize=14, fontweight="bold"
)
ax.grid(axis="x", alpha=0.3)

plt.tight_layout()
plt.savefig("chapter_6/plot_03_feature_importance.png", dpi=150)
plt.close()
print("  Tersimpan: chapter_6/plot_03_feature_importance.png")

# ============================================
# BAGIAN 2: VISUALISASI REGRESI
# ============================================
print("\n--- BAGIAN 2: REGRESI ---")

# ── 4. Scatter + Garis Regresi ───────────────────────────────────────────────
print("\n=== 4. Scatter Plot + Garis Regresi ===")

np.random.seed(42)
n = 50
pengalaman = np.random.uniform(0, 15, n)
gaji = 3 * pengalaman + 5 + np.random.normal(0, 2, n)
X_reg = pengalaman.reshape(-1, 1)

model_lr = LinearRegression()
model_lr.fit(X_reg, gaji)
x_line = np.linspace(0, 16, 100).reshape(-1, 1)
y_line = model_lr.predict(x_line)

fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(
    pengalaman,
    gaji,
    c="#3498db",
    s=60,
    alpha=0.7,
    edgecolors="white",
    label="Data aktual",
)
ax.plot(
    x_line,
    y_line,
    "r-",
    linewidth=2,
    label=f"Regresi: y = {model_lr.coef_[0]:.2f}x + {model_lr.intercept_:.2f}",
)

# Tambahkan residual lines untuk beberapa titik
for i in range(0, n, 5):
    pred = model_lr.predict([[pengalaman[i]]])[0]
    ax.plot(
        [pengalaman[i], pengalaman[i]], [gaji[i], pred], "g--", alpha=0.4, linewidth=1
    )

r2 = r2_score(gaji, model_lr.predict(X_reg))
ax.text(
    0.02,
    0.98,
    f"R² = {r2:.4f}",
    transform=ax.transAxes,
    fontsize=12,
    va="top",
    bbox=dict(boxstyle="round", facecolor="lightyellow", alpha=0.8),
)

ax.set_xlabel("Pengalaman Kerja (tahun)", fontsize=12)
ax.set_ylabel("Gaji (juta Rp)", fontsize=12)
ax.set_title("Linear Regression: Pengalaman vs Gaji", fontsize=14, fontweight="bold")
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("chapter_6/plot_04_regression.png", dpi=150)
plt.close()
print("  Tersimpan: chapter_6/plot_04_regression.png")

# ── 5. Linear vs Polynomial Regression ──────────────────────────────────────
print("\n=== 5. Linear vs Polynomial Regression ===")

np.random.seed(42)
X_nl = np.linspace(0, 10, 80).reshape(-1, 1)
y_nl = 0.5 * X_nl.ravel() ** 2 - 3 * X_nl.ravel() + 10 + np.random.normal(0, 3, 80)

# Linear
lr_nl = LinearRegression()
lr_nl.fit(X_nl, y_nl)
y_lr_pred = lr_nl.predict(X_nl)

# Polynomial degree=2
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X_nl)
pr_nl = LinearRegression()
pr_nl.fit(X_poly, y_nl)
X_plot_sorted = np.sort(X_nl, axis=0)
y_pr_pred = pr_nl.predict(poly.transform(X_plot_sorted))

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Linear
axes[0].scatter(X_nl, y_nl, c="#3498db", s=30, alpha=0.6, label="Data")
axes[0].plot(X_nl, y_lr_pred, "r-", linewidth=2, label="Linear Regression")
r2_lin = r2_score(y_nl, y_lr_pred)
axes[0].set_title(
    f"Linear Regression (R² = {r2_lin:.4f})", fontsize=13, fontweight="bold"
)
axes[0].set_xlabel("X")
axes[0].set_ylabel("y")
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Polynomial
axes[1].scatter(X_nl, y_nl, c="#3498db", s=30, alpha=0.6, label="Data")
axes[1].plot(X_plot_sorted, y_pr_pred, "r-", linewidth=2, label="Polynomial (degree=2)")
r2_poly = r2_score(y_nl, pr_nl.predict(X_poly))
axes[1].set_title(
    f"Polynomial Regression (R² = {r2_poly:.4f})", fontsize=13, fontweight="bold"
)
axes[1].set_xlabel("X")
axes[1].set_ylabel("y")
axes[1].legend()
axes[1].grid(True, alpha=0.3)

fig.suptitle(
    "Perbandingan Linear vs Polynomial Regression",
    fontsize=15,
    fontweight="bold",
    y=1.02,
)

plt.tight_layout()
plt.savefig("chapter_6/plot_05_lin_vs_poly.png", dpi=150)
plt.close()
print("  Tersimpan: chapter_6/plot_05_lin_vs_poly.png")

# ── 6. Residual Plot ────────────────────────────────────────────────────────
print("\n=== 6. Residual Plot ===")

np.random.seed(42)
X_res = np.random.uniform(0, 15, 50).reshape(-1, 1)
y_res = 3 * X_res.ravel() + 5 + np.random.normal(0, 2, 50)
model_res = LinearRegression()
model_res.fit(X_res, y_res)
y_pred_res = model_res.predict(X_res)
residuals = y_res - y_pred_res

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Predicted vs Actual
axes[0].scatter(y_res, y_pred_res, c="#3498db", s=50, alpha=0.7, edgecolors="white")
min_val = min(y_res.min(), y_pred_res.min())
max_val = max(y_res.max(), y_pred_res.max())
axes[0].plot(
    [min_val, max_val],
    [min_val, max_val],
    "r--",
    linewidth=2,
    label="Perfect prediction",
)
axes[0].set_xlabel("Nilai Aktual", fontsize=12)
axes[0].set_ylabel("Nilai Prediksi", fontsize=12)
axes[0].set_title("Actual vs Predicted", fontsize=13, fontweight="bold")
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Residual plot
axes[1].scatter(y_pred_res, residuals, c="#e74c3c", s=50, alpha=0.7, edgecolors="white")
axes[1].axhline(y=0, color="black", linestyle="-", linewidth=1)
axes[1].axhline(y=2 * np.std(residuals), color="gray", linestyle="--", alpha=0.5)
axes[1].axhline(y=-2 * np.std(residuals), color="gray", linestyle="--", alpha=0.5)
axes[1].set_xlabel("Nilai Prediksi", fontsize=12)
axes[1].set_ylabel("Residual (error)", fontsize=12)
axes[1].set_title("Residual Plot", fontsize=13, fontweight="bold")
axes[1].grid(True, alpha=0.3)

fig.suptitle("Diagnostik Model Regresi", fontsize=15, fontweight="bold", y=1.02)

plt.tight_layout()
plt.savefig("chapter_6/plot_06_residual.png", dpi=150)
plt.close()
print("  Tersimpan: chapter_6/plot_06_residual.png")

# ============================================
# BAGIAN 3: VISUALISASI CLUSTERING
# ============================================
print("\n--- BAGIAN 3: CLUSTERING ---")

# ── 7. Elbow Method ─────────────────────────────────────────────────────────
print("\n=== 7. Elbow Method ===")

np.random.seed(42)
X_clust, _ = make_blobs(n_samples=300, centers=4, cluster_std=1.0, random_state=42)
scaler_clust = StandardScaler()
X_clust_s = scaler_clust.fit_transform(X_clust)

K_range = range(2, 11)
inertias = []
sil_scores = []

for k in K_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_clust_s)
    inertias.append(km.inertia_)
    sil_scores.append(silhouette_score(X_clust_s, km.labels_))

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Elbow plot (Inertia)
axes[0].plot(list(K_range), inertias, "bo-", linewidth=2, markersize=8)
axes[0].axvline(x=4, color="red", linestyle="--", alpha=0.5, label="K optimal = 4")
axes[0].set_xlabel("Jumlah Cluster (K)", fontsize=12)
axes[0].set_ylabel("Inertia", fontsize=12)
axes[0].set_title("Elbow Method", fontsize=13, fontweight="bold")
axes[0].legend(fontsize=11)
axes[0].grid(True, alpha=0.3)
axes[0].set_xticks(list(K_range))

# Silhouette score
axes[1].plot(list(K_range), sil_scores, "go-", linewidth=2, markersize=8)
best_k = list(K_range)[np.argmax(sil_scores)]
axes[1].axvline(
    x=best_k, color="red", linestyle="--", alpha=0.5, label=f"K optimal = {best_k}"
)
axes[1].set_xlabel("Jumlah Cluster (K)", fontsize=12)
axes[1].set_ylabel("Silhouette Score", fontsize=12)
axes[1].set_title("Silhouette Score per K", fontsize=13, fontweight="bold")
axes[1].legend(fontsize=11)
axes[1].grid(True, alpha=0.3)
axes[1].set_xticks(list(K_range))

fig.suptitle(
    "Menentukan Jumlah Cluster Optimal", fontsize=15, fontweight="bold", y=1.02
)

plt.tight_layout()
plt.savefig("chapter_6/plot_07_elbow.png", dpi=150)
plt.close()
print("  Tersimpan: chapter_6/plot_07_elbow.png")

# ── 8. Hasil Clustering (Scatter 2D) ────────────────────────────────────────
print("\n=== 8. Hasil Clustering 2D ===")

kmeans_final = KMeans(n_clusters=4, random_state=42, n_init=10)
labels_final = kmeans_final.fit_predict(X_clust_s)
centroids = kmeans_final.cluster_centers_

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Sebelum clustering
axes[0].scatter(X_clust_s[:, 0], X_clust_s[:, 1], c="gray", s=30, alpha=0.5)
axes[0].set_title("Data Sebelum Clustering", fontsize=13, fontweight="bold")
axes[0].set_xlabel("Fitur 1 (scaled)")
axes[0].set_ylabel("Fitur 2 (scaled)")
axes[0].grid(True, alpha=0.3)

# Setelah clustering
colors_cluster = ["#3498db", "#e74c3c", "#2ecc71", "#f39c12"]
for i in range(4):
    mask = labels_final == i
    axes[1].scatter(
        X_clust_s[mask, 0],
        X_clust_s[mask, 1],
        c=colors_cluster[i],
        s=30,
        alpha=0.6,
        label=f"Cluster {i}",
    )

# Centroids
axes[1].scatter(
    centroids[:, 0],
    centroids[:, 1],
    c="black",
    marker="X",
    s=200,
    linewidths=2,
    edgecolors="white",
    label="Centroid",
    zorder=5,
)

sil = silhouette_score(X_clust_s, labels_final)
axes[1].set_title(
    f"Hasil K-Means (K=4, Silhouette={sil:.3f})", fontsize=13, fontweight="bold"
)
axes[1].set_xlabel("Fitur 1 (scaled)")
axes[1].set_ylabel("Fitur 2 (scaled)")
axes[1].legend(fontsize=10, loc="best")
axes[1].grid(True, alpha=0.3)

fig.suptitle("Visualisasi K-Means Clustering", fontsize=15, fontweight="bold", y=1.02)

plt.tight_layout()
plt.savefig("chapter_6/plot_08_clustering.png", dpi=150)
plt.close()
print("  Tersimpan: chapter_6/plot_08_clustering.png")

# ── 9. Segmentasi Pelanggan (Contoh Praktis) ────────────────────────────────
print("\n=== 9. Segmentasi Pelanggan ===")

np.random.seed(42)
pengeluaran = np.concatenate(
    [
        np.random.normal(500, 100, 60),
        np.random.normal(2000, 300, 80),
        np.random.normal(5000, 500, 60),
    ]
)
frekuensi = np.concatenate(
    [
        np.random.normal(3, 1, 60),
        np.random.normal(8, 2, 80),
        np.random.normal(15, 3, 60),
    ]
)
pengeluaran = np.abs(pengeluaran)
frekuensi = np.abs(frekuensi)

X_cust = np.column_stack([pengeluaran, frekuensi])
X_cust_s = StandardScaler().fit_transform(X_cust)

km_cust = KMeans(n_clusters=3, random_state=42, n_init=10)
labels_cust = km_cust.fit_predict(X_cust_s)

fig, ax = plt.subplots(figsize=(10, 7))

segment_names = {0: "Budget", 1: "Regular", 2: "Premium"}
segment_colors = {"Budget": "#3498db", "Regular": "#f39c12", "Premium": "#e74c3c"}

for i in range(3):
    mask = labels_cust == i
    avg_spend = pengeluaran[mask].mean()
    if avg_spend < 1000:
        name = "Budget"
    elif avg_spend < 3500:
        name = "Regular"
    else:
        name = "Premium"

    ax.scatter(
        pengeluaran[mask] / 1000,
        frekuensi[mask],
        c=segment_colors[name],
        s=50,
        alpha=0.6,
        label=f"{name} ({mask.sum()} pelanggan)",
        edgecolors="white",
    )

ax.set_xlabel("Pengeluaran Bulanan (ribu Rp)", fontsize=12)
ax.set_ylabel("Frekuensi Belanja (kali/bulan)", fontsize=12)
ax.set_title("Segmentasi Pelanggan dengan K-Means", fontsize=14, fontweight="bold")
ax.legend(fontsize=11, loc="upper left")
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("chapter_6/plot_09_segmentasi.png", dpi=150)
plt.close()
print("  Tersimpan: chapter_6/plot_09_segmentasi.png")

# ============================================
# Ringkasan
# ============================================
print("\n" + "=" * 60)
print("RINGKASAN VISUALISASI ML")
print("=" * 60)
print("""
File yang dihasilkan:

KLASIFIKASI:
  1. plot_01_confusion_matrix.png  - Confusion Matrix (evaluasi klasifikasi)
  2. plot_02_model_comparison.png  - Perbandingan akurasi model
  3. plot_03_feature_importance.png - Feature importance dari Random Forest

REGRESI:
  4. plot_04_regression.png        - Scatter + garis regresi
  5. plot_05_lin_vs_poly.png       - Linear vs Polynomial regression
  6. plot_06_residual.png          - Actual vs Predicted + Residual plot

CLUSTERING:
  7. plot_07_elbow.png             - Elbow Method + Silhouette Score
  8. plot_08_clustering.png        - Sebelum vs Sesudah clustering
  9. plot_09_segmentasi.png        - Contoh segmentasi pelanggan

Panduan Visualisasi ML:
  - Klasifikasi -> Confusion Matrix, ROC Curve, Feature Importance
  - Regresi     -> Scatter + garis regresi, Residual plot, Actual vs Predicted
  - Clustering  -> Elbow Method, Scatter plot per cluster, Silhouette plot
""")
