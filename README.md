# Pertemuan 10 - String dan Pengolahan Teks

Nama: Intan Anugra Salsabila
NIM: 2225250154
Kelas: PMAT-F-2026

## Tujuan
Mengolah dan menormalisasi data teks dengan string Python.

## Cara Menjalankan
python3 tugas/normalisasi_data_mahasiswa.py

## Algoritma
Proses normalisasi data teks pada program ini dilakukan dengan langkah-langkah berikut:
1. **Membaca Input**: Menerima input nama lengkap dan kode kelas sebagai string dari pengguna.
2. **Normalisasi Nama**: Menghapus spasi kosong di awal dan akhir teks menggunakan `.strip()`, merapikan huruf kapital menggunakan `.title()`, serta membersihkan spasi ganda di dalam teks menggunakan perulangan `while` dan fungsi `.replace("  ", " ")`.
3. **Pembuatan Inisial**: Memecah nama bersih menjadi list kata dengan `.split()`, lalu mengambil huruf pertama dari setiap kata menggunakan perulangan untuk digabungkan dan diubah menjadi huruf kapital dengan `.upper()`.
4. **Normalisasi Kode Kelas**: Mengubah seluruh teks menjadi huruf besar menggunakan `.upper()`, memecah berdasarkan spasi dengan `.split()`, dan menyatukannya kembali menggunakan tanda hubung melalui fungsi `"-".join()`.
5. **Output**: Menampilkan hasil modifikasi secara rapi ke layar terminal.

## Test Case

| Input Nama | Input Kode | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| `Intan Anugra Salsabila` | `PMAT-F-2026` | Intan Anugra Salsabila \| PMAT-F-2026 \| IAS | Intan Anugra Salsabila \| PMAT-F-2026 \| IAS | Sukses |
| `aan hendrayana` | `pmat a 2026` | Aan Hendrayana \| PMAT-A-2026 \| AH | Aan Hendrayana \| PMAT-A-2026 \| AH | Sukses |
| `fATHIYYAH mUTHMAINNAH` | `kelas b` | Fathiyyah Muthmainnah \| KELAS-B \| FM | Fathiyyah Muthmainnah \| KELAS-B \| FM | Sukses |
| `BUDI` | `pmtk 01` | Budi \| PMTK-01 \| B | Budi \| PMTK-01 \| B | Sukses |
| `siti nur aisyah` | `kelas c` | Siti Nur Aisyah \| KELAS-C \| SNA | Siti Nur Aisyah \| KELAS-C \| SNA | Sukses |

## Refleksi
* **Masalah teks yang ditemukan:** Masalah utama dalam pengolahan string adalah ketidakkonsistenan input pengguna, seperti penggunaan huruf kapital yang berantakan (perpaduan huruf besar-kecil) dan adanya spasi berlebih yang tidak sengaja terketik baik di awal, di akhir, maupun di antara kata.
* **Cara memperbaikinya:** Masalah tersebut berhasil diatasi dengan memanfaatkan metode bawaan Python, yaitu fungsi `.strip()` untuk memotong spasi luar, perulangan `while` dipadukan dengan `.replace()` untuk mereduksi spasi ganda di dalam kalimat menjadi spasi tunggal, serta metode `.title()` atau `.upper()` untuk menyeragamkan format huruf kapital.