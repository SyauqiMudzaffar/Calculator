# Deskripsi Tugas

Tugas ini terdiri dari tiga aplikasi yang berfungsi untuk melakukan enkripsi, dekripsi, dan steganografi. Berikut adalah rincian dari masing-masing aplikasi:

## 1. Aplikasi Kalkulator Caesar Cipher

### Deskripsi:
Aplikasi ini menerapkan metode Caesar Cipher untuk enkripsi dan dekripsi teks dengan pergeseran karakter. Pengguna dapat memasukkan teks dan nilai pergeseran untuk melakukan proses tersebut.

### Cara Menjalankan:
1. Jalankan file `calculator.py`.
2. Masukkan teks dan nilai pergeseran (antara 1 dan 25).
3. Klik tombol "Enkripsi" untuk mendapatkan hasil enkripsi, dan "Dekripsi" untuk mendapatkan teks asli.

### tampilan caesar chiper gui 
![Screenshot 2024-12-25 162259](https://github.com/user-attachments/assets/38adfc39-3b0f-4e6d-91ea-30fc7331632e)
---

## 2. Aplikasi Enkripsi dan Dekripsi DES
### Deskripsi:
Aplikasi ini menggunakan algoritma DES (Data Encryption Standard) untuk mengenkripsi dan mendekripsi teks. Pengguna dapat memasukkan teks dan kunci (harus 8 karakter) untuk melakukan enkripsi dan dekripsi.

### Cara Menjalankan:
1. Jalankan file `DESGUI.py`.
2. Masukkan teks yang ingin dienkripsi dan kunci yang valid.
3. Klik tombol "Enkripsi" untuk mendapatkan teks terenkripsi, dan "Dekripsi" untuk mendapatkan teks asli.

### tampilan des gui![Screenshot (404)](https://github.com/user-attachments/assets/f329db1a-6cae-4f73-bfad-823f068255b2)

---

## 3. Aplikasi Steganografi

### Deskripsi:
Aplikasi ini memungkinkan pengguna untuk menyembunyikan pesan dalam gambar menggunakan teknik steganografi. Pengguna dapat menyembunyikan pesan dalam gambar PNG atau JPG dan mengekstrak pesan dari gambar tersebut.

### Cara Menjalankan:
1. Jalankan file `SteganoGUI.py`.
2. Pilih gambar untuk menyembunyikan pesan atau untuk mengekstrak pesan.
3. Ikuti instruksi di GUI untuk menyembunyikan atau menampilkan pesan.

### tampilan stegano gui
![Screenshot 2024-12-25 162424](https://github.com/user-attachments/assets/354aa31d-c5ec-4dd1-8742-78fc7838c752)
![Screenshot 2024-12-25 162506](https://github.com/user-attachments/assets/011c756a-8b5d-4b5e-8aa0-a6e5e30ca66d)
![Screenshot 2024-12-25 162531](https://github.com/user-attachments/assets/7378c67a-90bf-46b5-8f3c-f46518ff25a6)
![Screenshot 2024-12-25 162545](https://github.com/user-attachments/assets/234fe4c0-7573-4d6a-aa0c-bca3d097b1f9)


---

## Cara Menjalankan

Untuk menjalankan aplikasi-aplikasi ini, pastikan Anda memiliki Python terinstal di sistem Anda. Anda juga perlu menginstal beberapa pustaka yang diperlukan. Berikut adalah langkah-langkah untuk menjalankan aplikasi:

### Instalasi Pustaka yang Diperlukan:
1. Buka terminal atau command prompt.
2. Jalankan perintah berikut untuk menginstal pustaka yang diperlukan:

### Menjalankan Aplikasi:
Navigasikan ke direktori tempat file aplikasi disimpan.

Jalankan aplikasi dengan perintah berikut:

1. Untuk Enkripsi dan Dekripsi DES: bash Salin kode python desgui.py
2. Untuk Kalkulator Caesar Cipher: bash Salin kode python kalkulator_caesar.py
3. Untuk Steganografi:bash Salin kode python steganogui.py
Dengan mengikuti langkah-langkah di atas, Anda dapat menjalankan dan menggunakan aplikasi-aplikasi yang telah dibuat.

```bash
pip install tkinter pycryptodome pillow stegano
