
# 💻 Capstone 1 – Sistem Manajemen Penjualan Laptop

## 📝 Preface
Capstone 1 ini adalah proyek terminal-based inventory & sales management system dengan studi kasus pada manajemen penjualan laptop yang dirancang sebagai latihan pemrograman Python untuk mengelola data penjualan laptop secara efisien. Program ini dibangun dalam rangka memenuhi tugas akhir dari pembelajaran dasar Python dan simulasi implementasi sistem berbasis data untuk toko laptop fiktif.

## 📌 Introduction
Sistem ini ditujukan untuk pemilik toko atau manajer inventaris yang ingin memantau pembelian, penjualan, dan stok laptop secara real-time melalui interface berbasis terminal. Dengan data yang tersimpan dalam struktur dictionary Python, pengguna dapat menambahkan, mengedit, menghapus, dan melihat data hanya dengan beberapa input sederhana.

## 🎯 Features Overview

| Fitur                  | Pembelian | Penjualan | Stok |
|------------------------|-----------|-----------|------|
| View (Tinjau)          | ✅         | ✅         | ✅    |
| Create (Tambah)        | ✅         | ✅         | ✅ *(otomatis dari pembelian)* |
| Update (Edit)          | ✅         | ✅         | ✅ *(otomatis)* |
| Delete (Hapus)         | ✅         | ✅         | ✅    |
| Serial Number Tracking | ✅         | ✅         | ✅    |   
    ^
    |__ Bagian ini terdapat dalam semua fitur karena user perlu menginputkan serial number dari laptop saat membeli maupun menjual 
## 🔍 Feature Details

### 🔎 View
- Menampilkan data dalam format tabel (menggunakan `tabulate`) untuk kemudahan membaca.
- Detail nomor seri laptop dapat dilihat berdasarkan index.

### ➕ Add
- Tambahkan data pembelian atau penjualan baru.
- Validasi stok otomatis: penjualan tidak dapat melebihi stok tersedia.
- Otomatis memperbarui stok saat pembelian atau penjualan dilakukan.

### ✏️ Edit
- Edit data berdasarkan index dan kolom yang dipilih (ID, Merk, Tipe, Jumlah, Harga).
- Update juga mengatur stok dan serial number secara otomatis sesuai perubahan.

### ❌ Delete
- Hapus data berdasarkan index.
- Setelah penghapusan, sistem langsung menampilkan data terkini.

## 🛠️ Technology Used
- Python 3.x  
- Tabulate (untuk tampilan tabel di terminal)

## 💾 Installation & Usage

1. Pastikan Python telah terinstal di sistem Anda.
2. Clone atau download file `Capstone 1 fixed.py` ke lokal komputer.
3. Jalankan program dengan perintah berikut di terminal:

```
python "Capstone 1 fixed.py"
```

4. Ikuti menu interaktif yang tersedia di terminal untuk mengelola data toko laptop.

## 🧠 What Makes It Special?
✅ Menyediakan *serial number tracking* per unit.  
✅ Otomatisasi stok saat pembelian & penjualan.  
✅ Validasi input agar data tetap konsisten.  
✅ Navigasi antarmuka berbasis teks yang sederhana dan intuitif.

## 📎 Example Use Case

1. Tambah pembelian: Tambahkan 5 unit Lenovo Thinkpad baru → stok otomatis bertambah.  
2. Tambah penjualan: Jual 2 unit dari stok → serial number berkurang dari gudang.  
3. Edit data: Ubah harga jual HP Pavilion → update harga & tampilkan ulang.  
4. Lihat stok: Tampilkan stok real-time dengan serial number yang tersedia.  
5. Hapus penjualan: Hapus satu data penjualan → stok akan tetap seperti semula.  

## 📬 Author
Dibuat oleh Dhika Wahyu Pratama  
Capstone 1 Project – Fundamental Python  
Lembaga: Purwadhika JCDSOH

