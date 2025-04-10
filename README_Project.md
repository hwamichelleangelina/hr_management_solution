# Proyek Pertama: Menyelesaikan Permasalahan Human Resources

## Business Understanding

Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri.

Walaupun telah menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas pada tingginya attrition rate (rasio jumlah karyawan yang keluar dibanding total karyawan) hingga lebih dari 10%.

Untuk mencegah hal ini semakin parah, manajer departemen HR ingin meminta bantuan untuk mengidentifikasi berbagai faktor yang mempengaruhi tingginya attrition rate tersebut. Selain itu, ia juga meminta pembuatan business dashboard agar dapat memonitor faktor-faktor tersebut secara lebih efisien.

### Permasalahan Bisnis

**Tujuan:**  
Mengidentifikasi faktor yang memengaruhi attrition rate tinggi (> 10%) dan bantu HR memonitor faktor-faktor tersebut.

**Problem Statement (Pertanyaan Bisnis):**  
Apa saja faktor signifikan yang menyebabkan karyawan resign dari perusahaan Jaya Jaya Maju?

**Target:**  
Mengetahui variabel paling berpengaruh terhadap attrition.

### Cakupan Proyek

- Memahami data dan melakukan data cleansing untuk missing values, duplikat, dan outlier
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

Business Dashboard: [Jaya Jaya Maju Attrition Rate Dashboard](https://public.tableau.com/views/jayajayamaju_attrition_rate/main_dashboard?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

## Conclusion
- Faktor signifikan yang memengaruhi attrition (berdasarkan uji p-value & korelasi) adalah:
  - `OverTime`: Karyawan yang lembur memiliki kemungkinan lebih besar untuk keluar
  - `JobRole`: Peran jabatan tertentu memiliki attrition rate yang tinggi
  - `Age`: Kelompok usia muda lebih rentan resign
  - `MonthlyIncome`: Karyawan dengan penghasilan rendah lebih mungkin keluar
  - `MaritalStatus`: Karyawan single memiliki attrition rate paling tinggi
  - `BusinessTravel`: Perjalanan bisnis tinggi meningkatkan attrition rate
  - `NumCompaniesWorked`: Semakin sering pindah kerja sebelumnya, semakin rentan keluar
  - `StockOptionLevel`: Meskipun pengaruhnya kecil, opsi saham masih relevan
- `Gender`, `PercentSalaryHike`, dan `Department` tidak memiliki pengaruh signifikan
- Faktor-faktor seperti `DistanceFromHome`, `RelationshipSatisfaction`, `JobLevel`, `TotalWorkingYears`, `YearsAtCompany`, `YearsInCurrentRole`, `YearsWithCurrManager`, `YearsSinceLastPromotion`, `WorkLifeBalance`, `JobInvolvement`, `Education`, `EducationField`, `DailyRate`, `HourlyRate`, `PerformanceRating`, dan `TrainingTimesLastYear` memiliki potensi pengaruh tidak langsung terhadap keputusan resign, tetapi kurang berperan besar.

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
  
5. **Kurangi Frekuensi Perjalanan Bisnis Tidak Perlu**  
    - BusinessTravel tinggi bisa mengganggu work-life balance. Evaluasi kebutuhan dan efisiensi perjalanan.
      - Karyawan Frequent Travel mencapai attrition ~27.5%, sedangkan Karyawan Non-Travel hanya ~11%.

6. **Tawarkan Retention Program untuk High Jumper**  
    - Bagi yang memiliki riwayat kerja berpindah-pindah, beri program pengembangan dan benefit jangka panjang agar merasa tertaut dengan perusahaan.
      - Karyawan dengan riwayat kerja di 4-9 perusahaan mencapai attrition > 28%.

#### B. Untuk Meningkatkan Retensi Jangka Panjang
1. **Program Work-Life Balance**  
    - Sediakan fleksibilitas waktu kerja, mental health day, dan ruang istirahat untuk menurunkan stres kerja.
2. **Penguatan Budaya Organisasi**  
    - Program engagement, feedback loop karyawan, dan pelatihan atasan dalam komunikasi bisa menurunkan keinginan resign.
3. **Perbaiki Hubungan Karyawan-Atasan**  
    - Hubungan yang baik dengan atasan bisa mencegah attrition.
