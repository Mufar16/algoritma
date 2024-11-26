## Author

Nama : Muh. Fadhlur Rahman R. Salim
NIM : F55123058
Kelas : B

Analisis Quiz 2

### **1. Bubble Sort (Naive Method)**
Bubble Sort membandingkan elemen-elemen yang bersebelahan dalam array dan menukar posisi mereka jika urutannya salah. Proses ini diulang hingga array menjadi terurut.

- **Best Case (O(n))**:
  - Terjadi jika data sudah dalam kondisi terurut.
  - Algoritma hanya memerlukan satu iterasi tanpa pertukaran.
 
- **Average Case (O(n²))**:
  - Untuk data acak, Bubble Sort tetap melakukan banyak pertukaran, sehingga waktu eksekusinya meningkat secara kuadrat.

- **Worst Case (O(n²))**:
  - Terjadi jika data dalam kondisi terbalik (descending).
  - Dibutuhkan banyak iterasi dan pertukaran untuk setiap elemen.

- **Kelebihan**:
  - Sederhana dan mudah diimplementasikan.
  - Cocok untuk dataset kecil.

- **Kekurangan**:
  - Tidak efisien untuk dataset besar.
  - Kompleksitas kuadrat menyebabkan waktu eksekusi yang lambat.

---

### **2. Merge Sort (Conquer Method)**
Merge Sort menggunakan pendekatan divide and conquer, membagi array menjadi dua bagian hingga ukurannya kecil, kemudian menggabungkannya kembali dalam urutan yang benar.

- **Best Case (O(n log n))**:
  - Semua kondisi memiliki waktu eksekusi yang sama karena proses pembagian dan penggabungan tetap dilakukan.

- **Average Case (O(n log n))**:
  - Dalam kondisi rata-rata, data yang bersifat acak juga membutuhkan proses pembagian dan penggabungan yang sama.

- **Worst Case (O(n log n))**:
  - Sama seperti *best case*, waktu eksekusi tetap stabil untuk semua jenis data.

- **Kelebihan**:
  - Sangat efisien untuk dataset besar.
  - Stabil (elemen dengan nilai sama mempertahankan urutan awal).

- **Kekurangan**:
  - Membutuhkan ruang memori tambahan (O(n)) untuk array sementara.

---

## **Kesimpulan**
- **Bubble Sort**:
  - Cocok untuk dataset kecil yang hampir terurut.
  - Tidak disarankan untuk dataset besar karena efisiensinya rendah.

- **Merge Sort**:
  - Lebih efisien untuk semua jenis dataset, terutama yang besar.
  - Direkomendasikan untuk aplikasi yang membutuhkan performa tinggi, meskipun membutuhkan lebih banyak memori.

---