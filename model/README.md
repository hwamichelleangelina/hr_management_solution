# Attrition Prediction System

Sistem prediksi ini menggunakan **ensemble model** untuk memprediksi kemungkinan karyawan mengalami attrition (keluar dari perusahaan). Terdapat dua metode input data: **manual** dan **upload file CSV**.

---

## Model yang Digunakan

- **XGBoost Model** (`xgb_model.pkl`)
- **Deep Learning Model** (`dl_model.h5`)
- Hasil prediksi merupakan hasil **voting ensemble** dari kedua model.

---

## Struktur

```
attrition-predictor/
│
├── prediction.py
├── xgb_model.pkl
├── dl_model.h5
├── label_encoders.pkl
├── scaler.pkl
└── README.md
```

---

## Cara Menjalankan

1. **Persiapkan Lingkungan Python**

   Pastikan Python 3.7+ sudah terinstall. Lalu, install dependency:

   ```bash
   pip install pandas scikit-learn xgboost tensorflow
   ```

2. **Jalankan Script**

   Di terminal atau IDE, jalankan:

   ```bash
   python prediction.py
   ```

3. **Pilih Mode Input**

   Akan muncul pilihan:

   ```
   Pilih mode input:
   1. Manual
   2. Upload file CSV
   ```

---

## Mode 1: Input Manual

Mengisi data karyawan satu per satu lewat terminal. Setelah semua diisi:

- Model akan memproses input.
- Prediksi ditampilkan di layar:
  ```
  === DETAIL DATA & PREDIKSI ===
  <Data karyawan>
  Prediksi Attrition dan Probabilitas Resign
  ```

---

## Mode 2: Upload File CSV

1. Siapkan file `.csv` dengan format yang sesuai (kolom input seperti `EmployeeId`, `Age`, `BusinessTravel`, dll.).
2. Upload saat diminta.
3. Sistem akan memproses seluruh baris dan menyimpan hasilnya di:

   ```
   hasil_prediksi.csv
   ```

   File ini berisi data asli + hasil prediksi kolom Attrition.

---

## Keterangan Penting

- `Over18` hanya diisi dengan `'Y'` karena seluruh data pelatihan diasumsikan 18+.
- Pastikan format input sesuai dengan opsi yang ditampilkan untuk kolom kategorikal seperti:
  - `Gender`: `'Male'`, `'Female'`
  - `JobRole`: `'Sales Executive'`, `'Research Scientist'`, dll.
  - `Education`: Integer dari 1 sampai 5
- Kolom numerik harus valid (dalam rentang wajar).

---
