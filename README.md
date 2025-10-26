# PA-KELOMPOK-13-A-25-
TEMA: SISTEM MANAJEMEN GACOAN
NAMA ANGGOTA: 
1. AULIA AISYAH AL HUMAIRA (2509116029)
2. FATIMATUZZAHRAH (2509116020)
3.  M. ISMUL AZAM A. (2509116034)
   
_____________________________________________________________________________________________________________________________________________________________________________________________________________________
# Deskripsi
Program ini merupakan program sistem manajemen mie gacoan yang memiliki 2 role, yaitu admim dan customer.Pada role admin dilengkapi sistem CRUD seperti dapat menambahkan, menampilkan, mengupdate, dan menghapus menu. Sedangkan pada menu customer, pengguna dapat menampilkan menu, mencari menu, menambahkan menu ke dalam keranjang, melihat isi keranjang, menghapus/ mengubah jumlah pesanan, top e-money,dan check out pesanan.
_____________________________________________________________________________________________________________________________________________________________________________________________________________________
# Fitur Program
Menu Admin
1. Tambahkan Menu
2. Tampilkan Menu
3. Update Menu
4. Hapus Menu
5. Kembali Ke Menu Utama 

Menu User
1. Tampilkan Menu
2. Cari Menu 
3. Tambah ke Keranjang
4. Lihat Keranjang 
5. Ubah/ Hapus pesanan 
6. Menu E-money 
7. Checkout
8. Kembali ke Menu utama

_____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Output
1. Halaman utama
   Pada saat program dijalankan, pengguna akan disajikan dengan tampilan menu utama sebagai berikut:
   <img width="323" height="230" alt="image" src="https://github.com/user-attachments/assets/09c5d8a5-b46a-49cc-9f90-31ae97e63592" />
   Tampilan tersebut merupakan halaman utama yang menjadi titik awal penggunaan program.
   Adapun penjelasan dari setiap pilihan menu sebagai berikut:
   Admin -> digunakan untuk masuk sebagai pengelola (admin) yang memiliki akses terhadap pengelolaan data produk.
   Customer -> digunakan untuk masuk sebagai pelanggan yang dapat melakukan transaksi pembelian.
   Keluar -> digunakan untuk menutup atau keluar dari program.

2. Role admin

   Jika memilih nomor 1 akan menampilkan login Admin dan keluar
   ![IMG-20251026-WA0036 1](https://github.com/user-attachments/assets/6dae09a1-fd61-4f03-91f6-e4b41a826e24)
   
   Jika sudah maka akan menampilkan login sebagai admin dan perlu mengisi username dan password yang sudah tersedia.
   ![WhatsApp Image 2025-10-26 at 18 43 45_bad0068e](https://github.com/user-attachments/assets/68cc0d7b-a1bd-4ed0-b333-c0236ba63064)

   Jika berhasil login sebagai admin akan diarahkan ke menu admin dan menampilkan menu CRUD, dan keluar
   ![WhatsApp Image 2025-10-26 at 18 46 53_229797b4](https://github.com/user-attachments/assets/b53e3bc9-c76e-4b76-8093-a70cefb6edc5)

   Jika memilih nomor 1 maka admin akan diarahkan untuk menambah menu yang ingin ditambahkan
   ![WhatsApp Image 2025-10-26 at 18 46 53_8a0300fa](https://github.com/user-attachments/assets/d55e681b-47e5-4283-aa11-249a103f4b62)

   Untuk melihat daftar menu yang tersedia, admin dapat melihat di nomor 2
   ![WhatsApp Image 2025-10-26 at 18 47 54_20e50728](https://github.com/user-attachments/assets/661a45f5-2b84-41ca-9ced-91ab5f47a3fc)

   Jika memilih nomor 3 program akan menampilkan menu update yang berguna untuk mengganti harga maupun nama dari daftar menu
   ![WhatsApp Image 2025-10-26 at 18 49 04_3cf2b497](https://github.com/user-attachments/assets/eed9c2ad-f7e0-4a77-86b0-56c36f1478bb)

   Nomor 4 berguna untuk menghapus menu yang sudah tidak dijual maupun habis
   ![WhatsApp Image 2025-10-26 at 18 49 59_c4cd2358](https://github.com/user-attachments/assets/c094c361-66f6-4ff5-8170-4c22b63adf1c)

   Nomor 5 akan menampilkan menu seperti awal memulai program
   ![WhatsApp Image 2025-10-26 at 18 50 33_603a4360](https://github.com/user-attachments/assets/0a6336ca-d14f-436d-bc6e-e08c8e57109f)


3. Role customer
   Jika memilih customer , muncul menu login dan daftar :
   <img width="525" height="305" alt="Screenshot 2025-10-26 180552" src="https://github.com/user-attachments/assets/74a30969-2c9c-4319-acfc-39dbfc4bddcf" />

   Sign Up
   Buat akun baru dengan username dan password ( Username harus 3-10 karakter )
   <img width="539" height="191" alt="Screenshot 2025-10-26 180906" src="https://github.com/user-attachments/assets/17323f33-3edc-4361-a08f-69d460191176" />

   Sign in
   Masuk dengan akun yang sudah dibuat :
   <img width="559" height="166" alt="Screenshot 2025-10-26 181021" src="https://github.com/user-attachments/assets/7594bc67-b3b5-4f38-8172-acc8a12fb0a7" />

   jika berhasil, tampil menu utama customer :
   <img width="645" height="432" alt="Screenshot 2025-10-26 181035" src="https://github.com/user-attachments/assets/4afe1dee-d3e1-4669-ae26-33a32729e9f7" />

   Fitur-Fitur Customer
   Tampilkan Menu
   Menampilkan daftar menu makanan dan minuman dalam bentuk tabel lengkap dengan harga :
   <img width="475" height="906" alt="Screenshot 2025-10-26 181229" src="https://github.com/user-attachments/assets/979e05ee-3f21-489b-a9ca-4028d91c3aa1" />

   Cari Menu
   Mencari menu berdasarkan nama (misal: “Gacoan”).
   Jika ditemukan, hasil akan muncul dalam tabel.
   <img width="474" height="207" alt="Screenshot 2025-10-26 184619" src="https://github.com/user-attachments/assets/2c0fee69-d9b6-471a-92b3-80f44a34b622" />

   Tambah ke Keranjang
   Fitur ini digunakan untuk menambahkan produk yang ingin dipesan ke dalam keranjang belanja.
   Pelanggan cukup memasukkan ID menu dan jumlah pesanan.
   Jika sudah ada di keranjang, jumlahnya akan ditambah otomatis.
   <img width="518" height="599" alt="Screenshot 2025-10-26 184948" src="https://github.com/user-attachments/assets/7f70f611-b977-4bf9-a893-95ba9b817f57" />

   Lihat Keranjang
   Menampilkan seluruh daftar pesanan yang telah dimasukkan ke keranjang dalam bentuk tabel, termasuk total harga setiap produk dan total keseluruhan.
   <img width="497" height="248" alt="Screenshot 2025-10-26 190419" src="https://github.com/user-attachments/assets/efbf1320-70dd-4d1a-a83b-116bdd9c6563" />

   Ubah/Hapus Pesanan
   Fitur ini memungkinkan pelanggan untuk memperbarui jumlah pesanan atau menghapus produk dari keranjang.
   Ubah jumlah pesanan (qty)
   <img width="462" height="211" alt="Screenshot 2025-10-26 192405" src="https://github.com/user-attachments/assets/1d9bd4d4-5284-45c0-8d5e-0c4363277569" />

   Hapus item dari keranjang
   <img width="500" height="180" alt="Screenshot 2025-10-26 192327" src="https://github.com/user-attachments/assets/4efe3a25-1b57-4e65-ade3-93be889064ea" />

   Menu Emoney
   <img width="315" height="226" alt="Screenshot 2025-10-26 192910" src="https://github.com/user-attachments/assets/4a9226c6-85a1-4aa3-9ee5-52e0463e7530" />
   Lihat Saldo Emoney, untuk menampilkan jumlah saldo saat ini.
   <img width="426" height="397" alt="Screenshot 2025-10-26 194442" src="https://github.com/user-attachments/assets/4a7fbc99-cc02-4b2c-9f80-4183b0e0ef3f" />
   Top Up Emoney, untuk menambah saldo dengan batas maksimal Rp100.000.000.
   <img width="571" height="168" alt="Screenshot 2025-10-26 194549" src="https://github.com/user-attachments/assets/c3653292-310e-48c5-b6a4-7f572fc689f4" />

   Checkout
   Digunakan untuk melakukan proses pembayaran.
   Sistem akan menampilkan ringkasan pesanan beserta total harga.
   Jika total pembelian melebihi Rp100.000, maka pelanggan akan mendapatkan diskon sebesar 15%.
   Pembayaran dilakukan secara otomatis dengan memotong saldo e-money pelanggan.
   <img width="576" height="679" alt="Screenshot 2025-10-26 195606" src="https://github.com/user-attachments/assets/dd19c012-82e1-42ba-a71e-31797eaf3353" />

   Kembali ke menu awal
   <img width="452" height="247" alt="Screenshot 2025-10-26 195709" src="https://github.com/user-attachments/assets/b3529e92-88ed-498c-9fb2-df540f913036" />


   



