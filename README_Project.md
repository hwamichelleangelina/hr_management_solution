# Proyek Pertama: Menyelesaikan Permasalahan Human Resources

## Business Understanding

Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri.

Walaupun telah menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas pada tingginya attrition rate (rasio jumlah karyawan yang keluar dibanding total karyawan) hingga lebih dari 10%.

Untuk mencegah hal ini semakin parah, manajer departemen HR ingin meminta bantuan untuk mengidentifikasi berbagai faktor yang mempengaruhi tingginya attrition rate tersebut. Selain itu, ia juga meminta pembuatan business dashboard agar dapat memonitor faktor-faktor tersebut secara lebih efisien.

### Permasalahan Bisnis
**Tujuan**
- Mengidentifikasi faktor yang memengaruhi attrition rate tinggi (>10%) dan bantu HR memonitor faktor-faktor tersebut.

**Problem Statement**
- Apa saja 6 faktor signifikan utama yang menyebabkan karyawan resign dari perusahaan Jaya Jaya Maju?
- Apa saja feature pendukung yang paling memengaruhi 6 faktor signifikan utama tersebut?

**Target**
  - Mengetahui 6 faktor signifikan yang paling berpengaruh terhadap attrition rate di Jaya Jaya Maju.
  - Mengidentifikasi solusi yang yang dapat menurunkan attrition rate.

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

Kemudian jalankan program sesuai kebutuhan.

## Business Dashboard
Dashboard yang dibuat bertujuan untuk memvisualisasikan dan memantau faktor-faktor penyebab utama dari attrition secara interaktif. Visualisasi ini mencakup:

- Distribusi dan perbandingan attrition berdasarkan fitur penting seperti usia, status pernikahan, pendapatan, overtime, dan lainnya
- Pemantauan demografi karyawan attrition
- Insight berdasarkan segmentasi working experience dan personal assessment

Business Dashboard: [Jaya Jaya Maju Attrition Rate Dashboard for Human Resources Department](https://lookerstudio.google.com/reporting/efed906a-c8f6-4de6-b98c-7eb642ec9705/page/nxCHF)

## Conclusion
- 6 Faktor signifikan yang memengaruhi attrition (berdasarkan uji p-value menggunakan Chi-square dan T-test) adalah:
  - `OverTime` dengan `p_value` bernilai 1.84e-16: Karyawan yang lembur memiliki kemungkinan lebih besar untuk keluar
  - `JobRole` dengan `p_value` bernilai 2.56e-11: Peran jabatan tertentu memiliki attrition rate yang tinggi
  - `MonthlyIncome` dengan `p_value` bernilai 5.78e-10: Karyawan dengan penghasilan rendah lebih mungkin keluar
  - `TotalWorkingYears` dengan `p_value` bernilai 2.16e-09: Karyawan dengan pengalaman kerja lebih lama cenderung retention. Lebih banyak karyawan dengan pengalaman kerja entry level yang memilih untuk resign.
  - `JobLevel` dengan `p_value` bernilai 2.63e-09: Karyawan dengan job level rendah rentan melakukan resignation. Semakin tinggi jabatan semakin rendah attrition ratenya
  - `MaritalStatus` dengan `p_value` bernilai 6.77e-09: Karyawan single memiliki attrition rate yang tinggi dibandingkan dengan Married dan Divorced
---
- 3 feature pendukung faktor utama dalam pengaruhnya terhadap attrition rate adalah:
  - 3 Feature Utama Berkorelasi dengan 'OverTime':
    - JobRole: 0.029 (Korelasi Positif)
    - Gender: 0.018 (Korelasi Positif)
    - EnvironmentSatisfaction: 0.007 (Korelasi Positif)
  - 3 Feature Utama Berkorelasi dengan 'JobRole':
    - Department: 0.926 (Korelasi Positif)
    - MonthlyIncome: 0.821 (Korelasi Positif)
    - JobLevel: 0.764 (Korelasi Positif)
  - 3 Feature Utama Berkorelasi dengan 'MonthlyIncome':
    - JobLevel: 0.954 (Korelasi Positif)
    - JobRole: 0.821 (Korelasi Positif)
    - TotalWorkingYears: 0.778 (Korelasi Positif)
  - 3 Feature Utama Berkorelasi dengan 'JobLevel':
    - MonthlyIncome: 0.954 (Korelasi Positif)
    - TotalWorkingYears: 0.787 (Korelasi Positif)
    - JobRole: 0.764 (Korelasi Positif)
  - 3 Feature Utama Berkorelasi dengan 'TotalWorkingYears':
    - JobLevel: 0.787 (Korelasi Positif)
    - MonthlyIncome: 0.778 (Korelasi Positif)
    - Age: 0.690 (Korelasi Positif)
  - 3 Feature Utama Berkorelasi dengan 'MaritalStatus':
    - StockOptionLevel: 0.476 (Korelasi Positif)
    - JobRole: 0.059 (Korelasi Positif)
    - Gender: 0.051 (Korelasi Positif)

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
