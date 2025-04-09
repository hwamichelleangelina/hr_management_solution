# Proyek Pertama: Menyelesaikan Permasalahan Human Resources

## Business Understanding

Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri.

Walaupun telah menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas pada tingginya attrition rate (rasio jumlah karyawan yang keluar dibanding total karyawan) hingga lebih dari 10%.

Untuk mencegah hal ini semakin parah, manajer departemen HR ingin meminta bantuan untuk mengidentifikasi berbagai faktor yang mempengaruhi tingginya attrition rate tersebut. Selain itu, ia juga meminta pembuatan business dashboard agar dapat memonitor faktor-faktor tersebut secara lebih efisien.

### Permasalahan Bisnis

**Tujuan:**  
Mengidentifikasi faktor yang memengaruhi attrition rate tinggi (>10%) dan bantu HR memonitor faktor-faktor tersebut.

**Problem Statement (Pertanyaan Bisnis):**  
Apa saja faktor signifikan yang menyebabkan karyawan resign dari perusahaan Jaya Jaya Maju?

**Target:**  
Mengetahui variabel paling berpengaruh terhadap attrition.

### Cakupan Proyek

- Analisis data employee dari Jaya Jaya Maju
- Feature engineering untuk menghasilkan insight yang lebih dalam
- Identifikasi faktor-faktor signifikan yang mempengaruhi attrition berdasarkan statistik dan korelasi
- Pembuatan business dashboard interaktif untuk membantu tim HR memonitor faktor-faktor tersebut
- Pemberian prediksi berbasis data

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

## Business Dashboard
Dashboard yang dibuat bertujuan untuk memvisualisasikan dan memantau faktor-faktor penyebab utama dari attrition secara interaktif. Visualisasi ini mencakup:

- Distribusi dan perbandingan attrition berdasarkan fitur penting seperti usia, status pernikahan, pendapatan, overtime, dan lainnya
- Filter interaktif untuk memantau perubahan dan pola
- Insight berdasarkan segmentasi seperti JobRole, BusinessTravel, dan lainnya

(Dashboard dapat ditampilkan menggunakan Streamlit atau Power BI, disesuaikan dengan preferensi implementasi.)

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
- Faktor-faktor seperti `DistanceFromHome`, `RelationshipSatisfaction`, `JobLevel`, `TotalWorkingYears`, `YearsAtCompany`, `YearsInCurrentRole`, `YearsWithCurrManager`, `YearsSinceLastPromotion`, `WorkLifeBalance`, `JobInvolvement`, `Education`, `EducationField`, `DailyRate`, `HourlyRate`, `PerformanceRating`, dan `TrainingTimesLastYear` memiliki potensi pengaruh tidak langsung terhadap keputusan resign.

### Rekomendasi Action Items

#### A. Untuk Mengurangi Attrition Rate
1. **Kurangi Beban Lembur Berlebih**  
   - Lakukan evaluasi beban kerja dan alokasi ulang jika perlu. Karyawan lembur memiliki attrition tertinggi.
     - Karyawan yang lembur memiliki attrition rate sebesar 30.2%. Tanpa lembur hanya 11.2%.

2. **Tingkatkan Benefit dan Apresiasi untuk Job Role yang Rentan Resign**  
   - Identifikasi job role rentan, seperti Sales Representative & Laboratory Technician yang memiliki attrition >25%.
   - Role seperti Research Director hanya 6.3%.

3. **Fokus pada Karyawan Muda dan Single**  
   - Berikan mentoring, benefit, dan pengembangan karir yang jelas.
     - Usia <30 tahun: attrition hingga 34.5%
     - Status single: attrition 26.7% (dibanding menikah 13.4% dan cerai 8%)

4. **Evaluasi Struktur Gaji & Tunjangan**  
   - Karyawan dengan pendapatan < 5000 memiliki attrition >25%, sedangkan > 9000 hanya ~8%.

5. **Kurangi Frekuensi Perjalanan Bisnis Tidak Perlu**  
   - Frequent Travel: attrition ~27.5%, Non-Travel hanya ~11%

6. **Tawarkan Retention Program untuk High Jumper**  
   - Karyawan dengan 4-9 pengalaman kerja sebelumnya: attrition >28%

#### B. Untuk Meningkatkan Retensi Jangka Panjang
1. **Program Work-Life Balance**  
   - Fleksibilitas kerja, mental health day, dan ruang istirahat.

2. **Penguatan Budaya Organisasi**  
   - Engagement, feedback loop karyawan, dan pelatihan untuk atasan.

3. **Perbaiki Hubungan Karyawan-Atasan**  
   - Hubungan yang baik bisa mengurangi keinginan resign.
