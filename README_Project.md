# Proyek Pertama: Menyelesaikan Permasalahan Human Resources

## Business Understanding

Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri.

Walaupun telah menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas pada tingginya attrition rate (rasio jumlah karyawan yang keluar dibanding total karyawan) hingga lebih dari 10%.

Untuk mencegah hal ini semakin parah, manajer departemen HR ingin meminta bantuan untuk mengidentifikasi berbagai faktor yang mempengaruhi tingginya attrition rate tersebut. Selain itu, ia juga meminta pembuatan business dashboard agar dapat memonitor faktor-faktor tersebut secara lebih efisien.

### Permasalahan Bisnis
- Apa saja 6 faktor signifikan utama yang menyebabkan karyawan resign dari perusahaan Jaya Jaya Maju?
- Apa saja feature pendukung yang paling memengaruhi 6 faktor signifikan utama tersebut?

### Cakupan Proyek

- Memahami data dan melakukan data cleansing untuk missing values
- Analisis data employee dari Jaya Jaya Maju
- Feature engineering untuk menghasilkan insight yang lebih dalam
- Identifikasi faktor-faktor signifikan yang mempengaruhi attrition berdasarkan statistik dan korelasi
- Pembuatan business dashboard interaktif untuk membantu tim HR memonitor faktor-faktor tersebut
- Pemberian prediksi attrition karyawan berbasis dataset

### Persiapan

**Sumber data:**  
[employee_data.csv](https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv)

**Setup environment:**

Pastikan seluruh file (notebook, script `.py`, dan file data) berada dalam satu folder. Jalankan sesuai preferensi:
- File `.ipynb` menggunakan Jupyter Notebook
- File `.py` menggunakan Python IDE

Install package dengan:

```
pip install -r requirements.txt
```
Jalankan semua cell dalam `notebook.ipynb`. File tersebut akan menampilkan Exploratory Data Analysis, kesimpulan hasil analisis, dan pembuatan model machine learning untuk prediksi attrition.

#### Menjalankan Program `prediction.py`
Pastikan file-file berikut di dalam direktori kerja:
- `prediction.py` — skrip utama untuk menjalankan prediksi
- `xgb_model.pkl` — model XGBoost
- `rf_model.pkl` — model Random Forest
- `dl_model.h5` — model Deep Learning (Keras)
- `scaler.pkl` — normalisasi fitur numerik
- `label_encoders.pkl` — encoder untuk fitur kategorikal

Jalankan perintah berikut untuk menginstal dependensi yang diperlukan:

```
pip install pandas scikit-learn xgboost tensorflow
```
Eksekusi skrip `prediction.py` dari terminal:
```
python prediction.py
```
Isi data karyawan langsung di terminal berdasarkan petunjuk yang diberikan: 1. Manual 2. Upload csv
- Jika menggunakan mode CSV:
  - File output akan disimpan sebagai: hasil_prediksi.csv
- Jika menggunakan input manual:
  - Hasil prediksi akan ditampilkan langsung di terminal.

Output akan memiliki dua kolom tambahan:
- Attrition_Prediction: 1 jika diprediksi akan keluar, 0 jika tetap.
- Attrition_Probability: Nilai probabilitas keluar dari perusahaan.

Setelah skrip dijalankan akan muncul pesan berhasil:
```
Prediksi selesai. Hasil disimpan di 'hasil_prediksi.csv'.
```
Pastikan hasil prediksi terdapat kolom: `Attrition_Prediction` dan `Attrition_Probability`. Jika kedua poin di atas terpenuhi, maka prediksi menggunakan berkas .py telah berhasil dijalankan dengan baik.


## Business Dashboard
Dashboard yang dibuat bertujuan untuk memvisualisasikan dan memantau faktor-faktor penyebab utama dari attrition secara interaktif. Visualisasi ini mencakup:

- Distribusi dan perbandingan attrition berdasarkan fitur penting seperti usia, status pernikahan, pendapatan, overtime, dan lainnya
- Pemantauan demografi karyawan attrition
- Insight berdasarkan segmentasi working experience dan personal assessment

Business Dashboard: [Jaya Jaya Maju Attrition Rate Dashboard for Human Resources Department](https://lookerstudio.google.com/reporting/efed906a-c8f6-4de6-b98c-7eb642ec9705/page/nxCHF)

## Conclusion
- Berdasarkan hasil analisis, terdapat enam faktor utama yang paling berpengaruh terhadap tingkat karyawan keluar (attrition) di perusahaan:
  - Lembur (OverTime): Karyawan yang sering lembur memiliki kemungkinan lebih tinggi untuk mengundurkan diri.
  - Jabatan (JobRole): Beberapa jenis jabatan tertentu menunjukkan tingkat attrition yang lebih tinggi dibanding yang lain.
  - Pendapatan Bulanan (Monthly Income): Karyawan dengan penghasilan yang lebih rendah cenderung lebih mudah keluar dari perusahaan.
  - Total Pengalaman Kerja (Total Working Years): Karyawan dengan pengalaman kerja yang masih sedikit, terutama di level entry, lebih rentan keluar dibanding yang lebih berpengalaman.
  - Level Jabatan (Job Level): Semakin rendah level jabatan seorang karyawan, semakin tinggi kemungkinan mereka untuk resign.
  - Status Pernikahan (Marital Status): Karyawan yang masih lajang lebih sering mengundurkan diri dibanding yang sudah menikah atau pernah menikah.
- Selain keenam faktor utama yang berpengaruh terhadap attrition, terdapat beberapa faktor pendukung yang memiliki hubungan erat dengan faktor-faktor utama tersebut. Pemahaman terhadap hubungan ini bisa membantu HR dalam merancang strategi yang lebih menyeluruh.
  - **Lembur (OverTime):**
    - Job Role: Jenis jabatan tertentu cenderung lebih sering lembur.
    - Gender: Ada perbedaan kecenderungan lembur berdasarkan jenis kelamin.
    - Environment Satisfaction: Tingkat kepuasan terhadap lingkungan kerja bisa memengaruhi apakah karyawan bersedia atau merasa terpaksa untuk lembur.
  - **Jabatan (JobRole):**
    - Department: Departemen tertentu cenderung memiliki jabatan-jabatan dengan risiko attrition lebih tinggi.
    - Monthly Income: Jabatan memengaruhi tingkat penghasilan, yang pada akhirnya berkaitan dengan retensi.
    - Job Level: Job role biasanya selaras dengan level jabatan yang memengaruhi beban dan tanggung jawab kerja.
  - **Pendapatan Bulanan (Monthly Income):**
    - Job Level: Level jabatan yang lebih tinggi memberikan penghasilan yang lebih besar.
    - Job Role: Jabatan tertentu cenderung memiliki kisaran gaji yang berbeda.
    - Total Working Years: Pengalaman kerja berkontribusi pada peningkatan penghasilan.
  - **Total Pengalaman Kerja (Total Working Years):**
    - Job Level: Karyawan dengan pengalaman lebih banyak biasanya memiliki jabatan yang lebih tinggi.
    - Monthly Income: Semakin berpengalaman, umumnya semakin besar penghasilan.
    - Age: Usia juga turut mencerminkan tingkat pengalaman kerja.
  - **Level Jabatan (Job Level):**
    - Monthly Income: Semakin tinggi jabatan, semakin besar penghasilan.
    - Total Working Years: Karyawan dengan masa kerja lebih panjang cenderung menempati jabatan lebih tinggi.
    - Job Role: Tipe jabatan sering kali menentukan level jabatan seseorang.
  - **Status Pernikahan (Marital Status):**
    - Stock Option Level: Ada kecenderungan tertentu pada karyawan yang sudah menikah dengan level kompensasi saham tertentu.
    - Job Role: Beberapa jabatan lebih banyak diisi oleh karyawan lajang.
    - Gender: Ada sedikit kecenderungan perbedaan berdasarkan jenis kelamin dalam hal status pernikahan.

### Rekomendasi Action Items
#### A. Untuk Mengurangi Attrition Rate
1. **Kurangi Beban Lembur Berlebih**  
    - Lakukan evaluasi beban kerja dan alokasi ulang jika perlu. Karyawan lembur memiliki attrition tertinggi.
      - Karyawan yang lembur (OverTime tinggi) memiliki attrition rate sebesar 30.2%. Sementara karyawan tanpa lembur hanya 11.2%.
2. **Tingkatkan Benefit dan Apresiasi untuk Job Role yang Rentan Resign**  
    - Identifikasi job role, terutama bidang yang bersinggungan langsung dengan Marketing dan Teknis dengan attrition tinggi, dan beri penghargaan atau program kesejahteraan.
      - Role seperti Sales Representative dan Laboratory Technician memiliki attrition rate di atas 25%. Sedangkan Research Director hanya 6.3%.
3. **Fokus pada Karyawan Muda dan Single**  
    - Berikan program mentoring, benefit, lingkungan kerja, dan pengembangan karir yang jelas. Karyawan muda dan single paling banyak resign.
      - Karyawan usia < 30 tahun memiliki attrition rate hingga 34.5%. Karyawan single memiliki attrition 26.7%, jauh lebih tinggi dari yang menikah (13.4%) atau cerai (8%).
4. **Evaluasi Struktur Gaji & Tunjangan**  
    - Karyawan berpendapatan rendah lebih cenderung resign. Lakukan benchmarking gaji dan berikan kompensasi yang non-finansial.
      - Karyawan dengan pendapatan < 5000 memiliki attrition rate > 25%, sedangkan > 9000 hanya ~8%.
5. **Perhatikan Pengaruh Job Level dan Career Path**
    - Karyawan dengan level jabatan rendah lebih rentan keluar karena merasa stagnan. Tawarkan jalur karir dan promosi yang jelas.
      - Attrition rate Job Level 1 mencapai 28.3%, sedangkan Level 5 hanya 4.5%.
      - Job Level berkorelasi kuat dengan MonthlyIncome (r = 0.95) dan TotalWorkingYears (r = 0.78), menandakan faktor-faktor ini saling menguatkan.
6. **Fokus Dukungan kepada Entry-Level & Fresh Graduate**
    - Terdapat hal yang membuat karyawan para entry level tidak nyaman di Jaya Jaya Maju. Tambahkan program onboarding, buddy system, dan career visioning di 6 bulan pertama.
      - Durasi pengalaman kerja yang kurang dari 2 tahun cenderung memiliki attrition rate tinggi (sering lebih dari 30%).

#### B. Untuk Meningkatkan Retensi Jangka Panjang
1. **Program Work-Life Balance**  
    - Sediakan fleksibilitas waktu kerja, mental health day, dan ruang istirahat untuk menurunkan stres kerja.
2. **Penguatan Budaya Organisasi**  
    - Program engagement, feedback loop karyawan, dan pelatihan atasan dalam komunikasi bisa menurunkan keinginan resign.
3. **Perbaiki Hubungan Karyawan-Atasan**  
    - Hubungan yang baik dengan atasan bisa mencegah attrition.
