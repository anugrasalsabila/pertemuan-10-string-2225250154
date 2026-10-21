# Nama Lengkap: Intan Anugra Salsabila
# Inisial      : IAS
# Kode         : PMAT-F-2026

def normalisasi_nama(nama):
    # Hapus spasi berlebih awal/akhir dan ubah menjadi Title Case
    nama_bersih = nama.strip().title()
    # Menghapus spasi ganda di dalam teks jika ada
    while "  " in nama_bersih:
        nama_bersih = nama_bersih.replace("  ", " ")
    return nama_bersih

def buat_inisial(nama):
    # Pecah nama menjadi list kata menggunakan split
    kata = nama.split()
    # Bangun inisial dari karakter awal setiap kata
    inisial = ""
    for k in kata:
        inisial += k[0].upper()
    return inisial

def normalisasi_kode(kode):
    # Gunakan strip, upper, split, dan join dengan tanda hubung "-"
    kode_bersih = kode.strip().upper()
    kata_kode = kode_bersih.split()
    return "-".join(kata_kode)

# --- PROGRAM UTAMA ---
# Input data mahasiswa secara dinamis
nama_input = input("Nama: ")
kode_input = input("Kode kelas: ")

# Proses normalisasi menggunakan fungsi yang telah dibuat
nama_hasil = normalisasi_nama(nama_input)
kode_hasil = normalisasi_kode(kode_input)
jumlah_kata = len(nama_hasil.split())
inisial_hasil = buat_inisial(nama_hasil)

# Tampilkan hasil normalisasi secara rapi sesuai Contoh Output
print("\nContoh Output")
print(f"Nama bersih : {nama_hasil}")
print(f"Kode kelas  : {kode_hasil}")
print(f"Jumlah kata : {jumlah_kata}")
print(f"Inisial     : {inisial_hasil}")