import json
from prettytable import PrettyTable
from pwinput import pwinput
from datetime import datetime


'''========================================================'''
'''                     JSON MENU                          '''
'''========================================================'''

def BacaData():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return data


def SimpanData(Data):
    with open('data.json', 'w') as file:
        json.dump(Data, file, indent=4)

'''========================================================'''
'''                JSON AKUN CUST                          '''
'''========================================================'''
def BacaUsers():
    with open('users.json', 'r') as file:
        users = json.load(file)
    return users


def SimpanUsers(users):
    with open('users.json', 'w') as file:
        json.dump(users, file, indent=4)

def tambah_ke_keranjang(keranjang):
    data = BacaData()
    tampilkan_menu()
    try:
        id_menu = int(input("Masukkan ID menu yang ingin ditambah ke keranjang: "))
    except ValueError:
        print("================================================================")
        print("            ID harus berupa angka! (｡•́︿•̀｡)                  ")
        print("================================================================") 
        return               
    
    menu = None
    for item in data:
        if item["Id"] == id_menu:
            menu = item
            break

    if menu is None:
        print("================================================================")
        print("              Maaf menu tidak ditemukan ૮(˶╥︿╥)                  ")
        print("================================================================")                
        

    try:
        qty = int(input("Masukkan jumlah: "))
        if qty <= 0:
            print("Jumlah harus lebih dari 0.")
            return
    except ValueError:
        print("================================================================")
        print("            Jumlah harus berupa angka! (｡•́︿•̀｡)                  ")
        print("================================================================")
        return    

# UNTUK MEMASTIKAN QTY SUDAH DITAMBAHKAN
    for item in keranjang:
        if item["Id"] == id_menu:
            item["qty"] += qty
            print(f"{menu['Nama']} berhasil ditambah ke keranjang. Total qty: {item['qty']}")
            return

# JIKA BELUM ADA TAMBAH BARU
    keranjang.append({"Id": menu["Id"], "Nama": menu["Nama"], "Harga": menu["Harga"], "qty": qty})
    print(f"{menu['Nama']} berhasil ditambah ke keranjang.")

def ubah_hapus_pesanan(keranjang):
    if not keranjang:
        print("================================================================")
        print("           Maaf keranjang anda kosong ૮(˶╥︿╥)            ")
        print("================================================================")
        return
    try:
        id_menu = int(input("Masukkan ID menu yang ingin diubah/hapus: "))
    except ValueError:
        print("================================================================")
        print("            ID harus berupa angka! (｡•́︿•̀｡)                  ")
        print("================================================================")
        return
    
    item = None
    for i in keranjang:
        if i["Id"] == id_menu:
            item = i
            break

    if item is None:        
        print("================================================================")
        print("                  Menu Tidak Ada ૮(˶╥︿╥)ა                   ")
        print("================================================================")
        return

    print(f"Menu: {item['Nama']} (Qty: {item['qty']})")
    print("1. Ubah Qty")
    print("2. Hapus dari keranjang")
    print("3. Kembali")
    
    pilih = input("Pilih (1/2/3): ")
    if pilih == "1":
        try:
            qty_baru = int(input("Masukkan qty baru: "))
            if qty_baru <= 0:
                print("Qty harus lebih dari 0.")
                return
            item["qty"] = qty_baru
            print("Qty berhasil diubah.")
        except ValueError:
            print("Qty harus angka.")
            return
    elif pilih == "2":
        keranjang.remove(item)
        print("Menu berhasil dihapus dari keranjang.")
    elif pilih == "3":
        return
    else:
        print("================================================================")
        print("                  Pilihan Tidak Ada ૮(˶╥︿╥)ა                   ")
        print("                     Silakan Pilih (1-3)                        ")
        print("================================================================")

def lihat_keranjang(keranjang):
    if not keranjang:
        print("================================================================")
        print("           Maaf keranjang anda kosong ૮(˶╥︿╥)            ")
        print("================================================================")

        return

    tabel = PrettyTable()
    tabel.title = "KERANJANG BELANJA"
    tabel.field_names = ["Id", "Nama", "Harga (Rp)", "Qty", "Total (Rp)"]
    total = 0
    for item in keranjang:
        subtotal = item["Harga"] * item["qty"]
        total += subtotal
        tabel.add_row([item["Id"], item["Nama"], item["Harga"], item["qty"], subtotal])
    print(tabel)
    print("\n")
    print(f"Total Keseluruhan: Rp{total}")

def checkout(keranjang, user):
    if not keranjang:
        print("================================================================")
        print("           Maaf keranjang anda kosong ૮(˶╥︿╥)ა           ")
        print("             Tidak bisa melakukan checkout")
        print("================================================================")
        return

    lihat_keranjang(keranjang)
    konfirmasi = input("Apakah Anda yakin ingin checkout? (ya/tidak): ").strip().lower()
    if konfirmasi != "ya":
        print("================================================================")
        print("   Checkout dibatalkan. Kembali ke menu utama! ૮₍｡´ᴖ ˔ ᴖ`｡₎ა    ")
        print("================================================================")
        return
    
    subtotal = sum(item["Harga"] * item["qty"] for item in keranjang)
    total = subtotal
    diskon = 0
    if subtotal >= 100000:
        diskon = subtotal * 0.15
        total -= diskon
        print(f"Diskon 15%: Rp{diskon}")
    print(f"Total Pembayaran: Rp{total}")
    print(f"Jumlah Emoney Anda: Rp{user['emoney']}")

    # Cek emoney
    if user["emoney"] >= total:
        user["emoney"] -= total
        # Simpan user
        users = BacaUsers()
        for u in users:
            if u["username"] == user["username"]:
                u["emoney"] = user["emoney"]
                break
            # UNTUK INVOICE
            transaksi = {
                "username": user["username"],
                "items": keranjang.copy(),
                "subtotal": subtotal,
                "diskon": diskon,
                "total": total,
                "timestamp": datetime.now().isoformat()
            }
        # Cetak invoice
        print("INVOICE")
        tabel = PrettyTable()
        tabel.field_names = ["Nama", "Qty", "Harga", "Total"]
        for item in keranjang:
            tabel.add_row([item["Nama"], item["qty"], item["Harga"], item["Harga"] * item["qty"]])
        print(tabel)
        print("=====================================================")
        print(f"Subtotal        : Rp{subtotal}")
        if diskon > 0:
            print(f"Diskon (15%)    : Rp{diskon}")
        print(f"Total Bayar     : Rp{total}")
        print(f"Waktu Pembayaran: {datetime.fromisoformat(transaksi['timestamp']).strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Pelanggan       : {user['username']}")
        print("=====================================================")
        print("Pembayaran menggunakan Emoney berhasil!")
        print("Transaksi berhasil!\n")
        keranjang.clear()
    else:
        print(f"Emoney tidak cukup. Anda memiliki Rp{user['emoney']}. Total yang dibutuhkan: Rp{total}")
        menu_emoney(user)
        checkout(keranjang, user)

# UNTUK MENCARI MENU

def pencarian_menu():
    data = BacaData()
    nama_menu = input("Masukkan nama menu yang dicari: ").strip().lower()
    if not nama_menu:
        print("Input tidak boleh kosong.")
        return

    hasil = []
    for item in data:
        # Bandingkan nama, ID, atau harga
        if nama_menu in item["Nama"].lower() or nama_menu == item["Id"] or nama_menu == item["Harga"]:
            hasil.append(item)

    if not hasil:
        print("================================================================")
        print("              Maaf menu tidak ditemukan ૮(˶╥︿╥)                  ")
        print("================================================================")
        input("Enter Untuk Melanjutkan.....")  
        return

    if hasil:
        print("HASIL PENCARIAN")
        tabel = PrettyTable()
        tabel.field_names = ["Id", "Nama", "Harga (Rp)"]
        for item in hasil:
            tabel.add_row([item["Id"], item["Nama"], f"Rp{item['Harga']}"])
        print(tabel)
    else:
        print("================================================================")
        print("              Maaf menu tidak ditemukan ૮(˶╥︿╥)                  ")
        print("================================================================")


def topup_emoney(user):
    print("\n=================================")
    print("            Topup Emoney        ")
    print("=================================")
    try:
        jumlah = int(input("Masukkan jumlah topup (Rp): "))
        if jumlah <= 0:
            print("Jumlah topup harus lebih dari 0.")
            return
        if jumlah > 100000000:
            print("Topup maksimal Rp100.000.000.")
            return
        user["emoney"] += jumlah
        users = BacaUsers()
        for u in users:
            if u["username"] == user["username"]:
                u["emoney"] = user["emoney"]
                break
        SimpanUsers(users)
        print(f"Topup berhasil! Emoney Anda sekarang: Rp{user['emoney']}")
    except ValueError:
        print("Jumlah topup harus angka.")
        return



def menu_emoney(user):
    while True:
        tabel = PrettyTable()
        tabel.title = "Menu Emoney"
        tabel.field_names = ["No", "Pilihan"]
        tabel.add_row(["1", "Lihat Jumlah Emoney"])
        tabel.add_row(["2", "Topup Emoney"])
        tabel.add_row(["3", "Kembali"])
        print(tabel)
        tabel_jumlah = PrettyTable()
        tabel_jumlah.title = "Jumlah Emoney Anda"
        tabel_jumlah.field_names = ["Jumlah (Rp)"]
        tabel_jumlah.add_row([user['emoney']])
        print(tabel_jumlah)
        try:
            pilih = input("Pilih Menu (1/2/3): ")
            if pilih == "1":
                print(f"Jumlah Emoney Anda: Rp{user['emoney']}")
            elif pilih == "2":
                topup_emoney(user)
            elif pilih == "3":
                return
            else:
                print("================================================================")
                print("                  Pilihan Tidak Ada ૮(˶╥︿╥)ა                   ")
                print("                     Silakan Pilih (1-3)                        ")
                print("================================================================")
                input("Enter untuk melanjutkan....")

        except (KeyboardInterrupt, EOFError):
            print("================================================================")
            print("            Dilarang Menggunakan Shortcut! (｡•́︿•̀｡)              ")
            print("================================================================")
            

def menu_user(user):
    keranjang = []
    while True:
        tabel = PrettyTable()
        tabel.title = "Menu User"
        tabel.field_names = ["No", "Pilihan"]
        tabel.add_row(["1", "Tampilkan Menu"])
        tabel.add_row(["2", "Cari Menu"])
        tabel.add_row(["3", "Tambah ke Keranjang"])
        tabel.add_row(["4", "Lihat Keranjang"])
        tabel.add_row(["5", "Ubah/hapus pesanan"])
        tabel.add_row(["6", "Menu Emoney"])
        tabel.add_row(["7", "Checkout"])
        tabel.add_row(["8", "Kembali ke menu awal"])
        print(tabel)
        print(f"Jumlah Emoney Anda: Rp{user['emoney']}")
        try:
            pilih = input("Pilih Menu (1/2/3/4/5/6/7): ")
            if   pilih == "1":
                tampilkan_menu()
            elif pilih == "2":
                pencarian_menu()
            elif pilih == "3":
                tambah_ke_keranjang(keranjang)
            elif pilih == "4":
                lihat_keranjang(keranjang)
            elif pilih == "5":
                ubah_hapus_pesanan(keranjang)
            elif pilih == "6":
                menu_emoney(user)
            elif pilih == "7":
                checkout(keranjang, user)
            elif pilih == "8":
                return
            else:
                print("================================================================")
                print("                  Pilihan Tidak Ada ૮(˶╥︿╥)ა                   ")
                print("                     Silakan Pilih (1-8)                        ")
                print("================================================================")
                input("Enter untuk melanjutkan....")
        except (KeyboardInterrupt, EOFError):
            print("================================================================")
            print("            Dilarang Menggunakan Shortcut! (｡•́︿•̀｡)              ")
            print("================================================================")
              
        
#  UNTUK MENAMBAH MENU 
def tambah_menu():
    data = BacaData()
    id = len(data) + 1

    while True:
        try:
            nama = input("Masukkan nama menu: ")
            if len(nama) > 20:
                print("================================================================")
                print("        Nama menu tidak boleh melebihi 20 karakter! (｡•́︿•̀｡)     ")
                print("================================================================")
         
                continue  

            harga = int(input("Masukkan harga: "))
            if harga > 50000:
                print("================================================================")
                print("        Harga tidak boleh melebihi Rp50.000! (｡•́︿•̀｡)           ")
                print("================================================================")
         
                continue  
            break

        except ValueError:
            print("================================================================")
            print("            Harga harus berupa angka! (｡•́︿•̀｡)                  ")
            print("================================================================")

        except KeyboardInterrupt:
            print("================================================================")
            print("        Input dibatalkan! Kembali ke menu awal  ૮₍｡´ᴖ ˔ ᴖ`｡₎ა    ")
            print("================================================================")

              

    data.append({"Id": id, "Nama": nama, "Harga": harga})
    SimpanData(data)
    print("================================================================")
    print("        Menu Berhasil Ditambahkan!   ૮₍｡´ᴖ ˔ ᴖ`｡₎ა              ")
    print("================================================================")


# UNTUK MENAMPILKAN MENU-MENU
def tampilkan_menu():
    data = BacaData()
    if not data:
        print("Belum ada data.")
        return

    tabel = PrettyTable()
    tabel.title = "=== DAFTAR MENU ==="
    tabel.field_names = ["Id", "Nama", "Harga (Rp)"]
    for m in data:
        tabel.add_row([m["Id"], m["Nama"], m["Harga"]])
    print(tabel)

# UNTUK MENGGANTI MENU YANG SUDAH ADA
def update_menu():
    data = BacaData()
    if not data:
        print("Belum ada data.")
        return

    tampilkan_menu()

    while True:
        try:
            id_produk = int(input("Masukkan ID Produk yang Ingin Diupdate: "))
        except ValueError:
            print("================================================================")
            print("            ID harus berupa angka! (｡•́︿•̀｡)                  ")
            print("================================================================")

        # cari produk berdasarkan ID
        produk = None
        for item in data:
            if item["Id"] == id_produk:
                produk = item
                break

        # kalau tidak ketemu, ulang
        if produk is None:
            print("=======================================================================")
            print("                DATA YANG ANDA MASUKKAN TIDAK VALID                   ")
            print("=======================================================================")
            print("   Pastikan ID produk ada, menu tidak kosong, dan harga sesuai.       ")
            print("=======================================================================")
            tampilkan_menu()
            continue

        # kalau ketemu, minta data baru
        print(f"\nProduk ditemukan: {produk['Nama']} (Harga: Rp{produk['Harga']})")

        menu_baru = input("Masukkan Nama Menu Baru (kosongkan jika tidak diubah): ").strip()
        if menu_baru and len(menu_baru) > 20:
            print("Nama menu tidak boleh melebihi 20 huruf.")
            continue
        harga_input = input("Masukkan Harga Baru (kosongkan jika tidak diubah): ").strip()

        # ubah nama jika diisi
        if menu_baru:
            produk["Nama"] = menu_baru

        # ubah harga jika diisi
        if harga_input:
            try:
                harga_baru = int(harga_input)
                if harga_baru <= 0:
                    print("Harga harus lebih dari 0.")
                    continue
                if harga_baru > 50000:
                    print("Harga tidak boleh melebihi Rp50.000.")
                    continue
                produk["Harga"] = harga_baru
            except ValueError:
                print("================================================================")
                print("            Harga harus berupa angka! (｡•́︿•̀｡)                  ")
                print("================================================================")

        # simpan hasil update
        SimpanData(data)
        print("\nData berhasil diupdate! Terima Kasih.")
        tampilkan_menu()
        break  
# UNTUK MENGHAPUS 
def hapus_menu():
    data = BacaData()
    tampilkan_menu()
    try:
        id_produk = int(input("Masukkan ID yang ingin dihapus: "))
    except ValueError:
        print("================================================================")
        print("            ID harus berupa angka! (｡•́︿•̀｡)                  ")
        print("================================================================")
        return
    
    baru = [d for d in data if d["Id"] != id_produk]
    if len(baru) == len(data):
        print("================================================================")
        print("              Maaf ID tidak ditemukan ૮(˶╥︿╥)                  ")
        print("================================================================") 
        return
    SimpanData(baru)
    print("================================================================")
    print("           Menu berhasil dihapus! ૮₍｡´ᴖ ˔ ᴖ`｡₎ა                  ")
    print("================================================================")


# MENU ADMIN
def menu_admin():
    while True:
        tabel = PrettyTable()
        tabel.title = "Menu Admin"
        tabel.field_names = ["No", "Pilihan"]
        tabel.add_row(["1", "Tambahkan Menu"])
        tabel.add_row(["2", "Tampilkan Menu"])
        tabel.add_row(["3", "Update Menu"])
        tabel.add_row(["4", "Hapus Menu"])
        tabel.add_row(["5", "Kembali Ke Menu Utama"])
        print(tabel)
        print("\n")
        try:
            pilih = input("Pilih Menu (1/2/3/4/5): ")
            if   pilih == "1":
                tambah_menu()
            elif pilih == "2":
                tampilkan_menu()
            elif pilih == "3":
                update_menu()
            elif pilih == "4":
                hapus_menu()
            elif pilih == "5":
                return
            else:
                print("================================================================")
                print("                  Pilihan Tidak Ada ૮(˶╥︿╥)ა                   ")
                print("                     Silakan Pilih (1-3)                        ")
                print("================================================================")
                input("Enter untuk melanjutkan....")

        except (KeyboardInterrupt, EOFError):
            print("================================================================")
            print("            Dilarang Menggunakan Shortcut! (｡•́︿•̀｡)              ")
            print("================================================================")
            

# =========================
# LOGIN ADMIN
# =========================
def login_admin():
    print("\n=======================================================")
    print("      Silakan Login sebagai Admin ◝(ᵔᵕᵔ)◜                  ")
    print("=======================================================")

    batas_login = 3
    while batas_login > 0:
        try:
            username = input("Masukkan Username Admin: ")
            password = pwinput("Masukkan Password Admin: ")
        except (KeyboardInterrupt, EOFError):
            print("================================================================")
            print("            Dilarang Menggunakan Shortcut! (｡•́︿•̀｡)              ")
            print("================================================================")
            return None

        for admin in admins:
            if admin["username"] == username and admin["password"] == password:
                print("======================================================================")
                print(f"      Halo Admin {username}! ◝(ᵔᵕᵔ)◜ Silakan Pilih Menu Berikut     ")
                print("======================================================================")
                return admin  

        batas_login -= 1
        print("==============================================================")
        print("   Username/Password Admin Salah! ૮(˶╥︿╥)ა  Coba Lagi        ")
        print(f"             Sisa percobaan: {batas_login}                   ")
        print("==============================================================")

    print("=====================================================")
    print("   Login Admin Gagal! Terlalu Banyak Percobaan Salah ")
    print("=====================================================")
    return None

# =========================
# LOGIN CUSTOMER
# =========================
def login_customer():
    users = BacaUsers()
    print("\n=======================================================")
    print("      Silakan Login sebagai Customer ◝(ᵔᵕᵔ)◜               ")
    print("=======================================================")

    batas_login = 3
    while batas_login > 0:
        try:
            username = input("Masukkan Username Anda: ")
            password = pwinput("Masukkan Password Anda: ")
        except (KeyboardInterrupt, EOFError):
            print("================================================================")
            print("            Dilarang Menggunakan Shortcut! (｡•́︿•̀｡)              ")
            print("================================================================")
            return None

        for user in users:
            if user["username"] == username and user["password"] == password and user["role"] == "customer":
                print("================================================================")
                print(f"      Halo {username}! ◝(ᵔᵕᵔ)◜ Silakan Pilih Menu Berikut     ")
                print("================================================================")
                return user  
        else:
            batas_login -= 1
            print("=====================================================")
            print("   Username/Password Anda Salah! ૮(˶╥︿╥)ა Coba Lagi ")
            print(f"   Sisa percobaan: {batas_login}")
            print("=====================================================")
     

    print("=============================-============================")
    print("   Login Gagal! Terlalu Banyak Percobaan Salah ૮(˶╥︿╥)ა  ")
    print("==========================================================")
    return None

# =========================
# SIGN UP CUSTOMER
# =========================
def sign_up_customer():
    users = BacaUsers()
    print("\n=======================================================")
    print("       Sign Up sebagai Customer Baru   ૮₍｡´ᴖ ˔ ᴖ`｡₎ა    ")
    print("=======================================================")
    while True:
        try:
            username = input("Masukkan Username Baru: ").strip()
            password = pwinput("Masukkan Password Baru: ").strip()

            if not username:
                print("================================================================")
                print("           Maaf username tidak boleh kosong ૮(˶╥︿╥)            ")
                print("                 Masukkan Username yang benar                   ")
                print("================================================================")
         
                continue
            
            if len(username) < 3 or len(username) > 10:
                print("=======================================================")
                print("         Username harus 3-10 karakter!  ◝(ᵔ^ᵔ)◜      ") 
                print("=======================================================")
         
                continue

            for u in users:
                if u["username"] == username:
                    print("================================================================")
                    print("                  Username sudah ada ૮(˶╥︿╥)ა                   ")
                    print("                     Masukkan username lain                     ")
                    print("================================================================")
             
                    continue

            if not password:
                print("================================================================")
                print("           Maaf password tidak boleh kosong ૮(˶╥︿╥)            ")
                print("                 Masukkan Password yang benar                   ")
                print("================================================================")
         
                continue

            confirm_password = pwinput("Konfirmasi Password: ").strip()
            if password != confirm_password:
                print("================================================================")
                print("               Maaf password tidak cocok ૮(˶╥︿╥)               ")
                print("                 Masukkan password yang sesuai                  ")
                print("================================================================")
         
                continue  
            break
        except (KeyboardInterrupt, EOFError):
            print("================================================================")
            print("            Dilarang Menggunakan Shortcut! (｡•́︿•̀｡)              ")
            print("================================================================")

    new_user = {
            "username": username,
            "password": password,
            "role": "customer",
            "emoney": 0
        }
    users.append(new_user)
    SimpanUsers(users)
    print("=====================================================")
    print("            Sign Up Berhasil! ૮₍｡´ᴖ ˔ ᴖ`｡₎ა           ")
    print("            Silakan Login sebagai Customer           ")
    print("=====================================================")
    return new_user



# AKUN-AKUN ADMIN 
admins = [
    {"username": "Aulia", "password": "29992", "role": "admin"},
    {"username": "Fatimah", "password": "20255", "role": "admin"},
    {"username": "Azam", "password": "00011", "role": "admin"}
]

# =========================
# ADMIN LOGIN
# =========================
def menu_admin_login():
    while True:
        tabel = PrettyTable()
        tabel.title = "Menu Admin"
        tabel.field_names = ["No", "Pilihan"]
        tabel.add_row(["1", "Sign In sebagai Admin"])
        tabel.add_row(["2", "Kembali ke Menu Utama"])
        print(tabel)
        print("\n")
        try:
            pilih = input("Pilih Menu (1/2): ")
        except (KeyboardInterrupt, EOFError):
            print("================================================================")
            print("            Dilarang Menggunakan Shortcut! (｡•́︿•̀｡)              ")
            print("================================================================")
            continue

        if pilih == "1":
            user = login_admin()
            if user:
                menu_admin()
                return  
        elif pilih == "2":
            return
        else:
            print("================================================================")
            print("                  Pilihan Tidak Ada ૮(˶╥︿╥)ა                   ")
            print("                     Silakan Pilih (1-2)                        ")
            print("================================================================")
            input("Enter untuk melanjutkan....")

# =========================
# MENU CUSTOMER LOGIN
# =========================
def menu_customer_login():
    while True:
        tabel = PrettyTable()
        tabel.title = "Menu Customer"
        tabel.field_names = ["No", "Pilihan"]
        tabel.add_row(["1", "Sign In sebagai Customer"])
        tabel.add_row(["2", "Sign Up sebagai Customer"])
        tabel.add_row(["3", "Kembali ke Menu Utama"])
        print(tabel)
        print("\n")
        try:
            pilih = input("Pilih Menu (1/2/3): ")
        except (KeyboardInterrupt, EOFError):
            print("================================================================")
            print("                 Input dibatalkan! (｡•́︿•̀｡)                      ")
            print("================================================================")
            return 

        if pilih == "1":
            user = login_customer()
            if user:
                menu_user(user)
                return 
        elif pilih == "2":
            sign_up_customer()
        elif pilih == "3":
            return
        else:
            print("================================================================")
            print("                  Pilihan Tidak Ada ૮(˶╥︿╥)ა                   ")
            print("                     Silakan Pilih (1-3)                        ")
            print("================================================================")
            input("Enter untuk melanjutkan....")

# =========================
# MENU LOGIN UTAMA
# =========================
def login():
    while True:
        tabel = PrettyTable()
        tabel.title = "Sistem Manajemen Mie Gacoan Kelompok 11"
        tabel.field_names = ["No", "Pilihan"]
        tabel.add_row(["1", "Admin"])
        tabel.add_row(["2", "Customer"])
        tabel.add_row(["3", "Keluar"])
        print(tabel)
        print("\n")
        try:
            pilih_login = input("Pilih Role Anda (1/2/3): ")
        except (KeyboardInterrupt, EOFError):
            print("================================================================")
            print("            Dilarang Menggunakan Shortcut! (｡•́︿•̀｡)              ")
            print("================================================================")
            continue

        if pilih_login == "1":
            menu_admin_login()
        elif pilih_login == "2":
            menu_customer_login()
        elif pilih_login == "3":
            print("================================================================")
            print("   Terima Kasih Telah Menggunakan Sistem Kami! ૮₍｡´ᴖ ˔ ᴖ`｡₎ა     ")
            print("================================================================")
            break
        else:
            print("================================================================")
            print("                  Pilihan Tidak Ada ૮(˶╥︿╥)ა                   ")
            print("                     Silakan Pilih (1-3)                        ")
            print("================================================================")
            input("Enter untuk melanjutkan....")
login()
