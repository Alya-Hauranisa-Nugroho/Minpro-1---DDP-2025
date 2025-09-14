# Minpro 1 - DDP 2025
# Profil
Nama: Alya Hauranisa Nugroho\
NIM: 2509116005\
Kelas: Sistem Informasi A 2025

# Deskripsi Singkat
Program Python sederhana yang saya buat ini berjudul **"Sistem Manajemen Pemesanan Bouquet Bunga"**. Program ini dapat dimanfaatkan oleh pengguna(florist/owner) 
untuk mencatat dan memilah orderan yang masuk, sehingga memudahkan pengguna untuk memanajemen dan mengatur pesanan yang ada. Selain itu, 
program ini juga telah memuat seluruh sistem CRUD (Create, Read, Update, dan Delete).
### **Program ini memiliki beberapa menu yang tersedia, yakni:**
1. Dapat memasukkan orderan baru
2. Dapat melihat orderan yang ada
3. Dapat mengupdate status orderan
4. Dapat menghapus orderan
5. Keluar dari program

# Flowchart
Berikut merupakan flowchart dari program **Sistem Manajemen Pemesanan Bouquet Bunga**\
<img width="10115" height="9860" alt="MINPRO1 drawio (5)" src="https://github.com/user-attachments/assets/b0aa8f49-9563-44f3-9307-429a027f6f04" />


# Alur Program
- Saat membuka program, pengguna akan diminta untuk input angka dari 1-5 untuk memilih menu yang tersedia
<img width="591" height="264" alt="image" src="https://github.com/user-attachments/assets/31f49689-c1b9-44b8-86a9-7cccf2f4d46c" />

- Apabila angka menu yang diinput tidak sesuai, maka program akan terhenti dan menampilkan "Yahh... Menu yang kamu pilih tidak valid :("
<img width="749" height="273" alt="image" src="https://github.com/user-attachments/assets/47bbf634-998c-4831-93fc-f532b0edd8f7" />


## Menu 1 - Masukkan Orderan Baru
- Menu ini memungkinkan pengguna menambahkan orderan baru ke dalam list orderan
<img width="650" height="234" alt="image" src="https://github.com/user-attachments/assets/d259e5ea-b204-472a-8183-cb9bebd00e20" />

- Pada menu ini, pengguna akan diminta untuk memasukkan input nama pemesan, No HP, paket bouquet yang dipilih, custom (+add on bunga), warna wrapping paper, serta tanggal pengambilan.
<img width="606" height="514" alt="image" src="https://github.com/user-attachments/assets/d1c7b624-e23f-4c18-b4c2-aa9b174935f7" />

- Program akan menambahkan orderan baru ke dalam list orderan.
<img width="757" height="44" alt="image" src="https://github.com/user-attachments/assets/d820e167-ffee-4d6e-816c-3e69d5d56a9f" />

- Selanjutnya, program menampilkan ringkasan pesanan dan daftar orderan yang terbaru.
<img width="1012" height="405" alt="image" src="https://github.com/user-attachments/assets/38b22f07-1790-47c2-963e-b3f1c9df92aa" />

- Apabila ditengah input paket bouquet, custom bunga, ataupun warna wrapping paper pengguna memasukkan angka yang salah, maka program akan terhenti dan mengeluarkan output "Pilihan kamu tidak valid :("
<img width="496" height="206" alt="image" src="https://github.com/user-attachments/assets/6d13a10c-5cf0-47cc-890e-5b7caaebffa1" />

## Menu 2 - Lihat Orderan
- Menu ini memungkinkan pengguna untuk melihat orderan yang ada
<img width="703" height="232" alt="image" src="https://github.com/user-attachments/assets/6596a20b-0bd4-403f-aa29-b752f6e886f1" />

- Apabila jumlah list orderan = 0, maka program akan menampilkan output "Belum ada orderan, nih :("
<img width="575" height="81" alt="image" src="https://github.com/user-attachments/assets/c0cae574-2763-4dd9-b045-b093ba9f9af0" />

- Namun, apabila list orderan terisi, maka program akan menampilkan seluruh daftar orderan.
<img width="1010" height="374" alt="image" src="https://github.com/user-attachments/assets/ba15cef0-1029-4939-ae3d-96aceed7e845" />

## Menu 3 - Update Status Orderan
- Menu ini memungkinkan pengguna untuk update status dari sebuah orderan
<img width="639" height="195" alt="image" src="https://github.com/user-attachments/assets/f98fca0b-c4f0-4753-bae3-128bb458352a" />

- Apabila jumlah list orderan = 0, maka program akan menampilkan output "Oh noo, belum ada orderan buat diupdate :("
<img width="670" height="78" alt="image" src="https://github.com/user-attachments/assets/d8697bdc-cd2c-402d-853c-16fe5ee42266" />

- Jika list orderan terisi, maka program akan menampilkan daftar orderan dan pengguna diminta untuk input nomor orderan yang statusnya ingin diupdate. Selanjutnya, pengguna diminta untuk input angka 0-2 untuk menentukan status baru, sehingga program dapat mengubah elemen list sesuai dengan index yang dimasukkan. 
<img width="1047" height="450" alt="image" src="https://github.com/user-attachments/assets/c6c3b69d-6efe-4d40-849f-363b3b454145" />

- Program akan menampilkan list orderan yang telah terupdate, serta seluruh daftar orderan.
- Apabila ditengah menjalankan menu ini terdapat input yang salah, maka program akan terhenti dan menampilkan "Pilihan kamu tidak valid :("
<img width="494" height="138" alt="image" src="https://github.com/user-attachments/assets/48900193-29e6-4897-98d0-d6b4fe41ae94" />


## Menu 4 - Hapus Orderan
- Menu ini memungkinkan pengguna untuk menghapus orderan yang ada
<img width="712" height="229" alt="image" src="https://github.com/user-attachments/assets/1003bacf-9ab9-417a-8dfb-ad843edeb3bd" />

- Apabila jumlah list orderan = 0, maka program akan menampilkan output "Belum ada orderan yang bisa dihapus :p"
<img width="702" height="78" alt="image" src="https://github.com/user-attachments/assets/bc3341ec-3698-4ef8-9b8e-60e283ef55ec" />

- Jika list orderan terisi, maka program akan menampilkan daftar orderan dan pengguna diminta untuk input nomor orderan yang ingin dihapus.
<img width="1000" height="275" alt="image" src="https://github.com/user-attachments/assets/217d7e53-4bc6-4a2f-98fd-0b6efb9254c5" />

- Selanjutnya, program akan menghapus orderan yang terpilih
<img width="536" height="20" alt="image" src="https://github.com/user-attachments/assets/6deb603e-674e-4c3d-926f-8e367ac4b14e" />

- Program akan menampilkan orderan yang telah dihapus, serta seluruh daftar orderan terbaru.
<img width="1065" height="196" alt="image" src="https://github.com/user-attachments/assets/9e6aec39-3687-40e8-8649-0f072bf5eed6" />

- Apabila ditengah menjalankan menu ini terdapat input yang salah, maka program akan terhenti dan menampilkan "Pilihan kamu tidak valid :("
<img width="985" height="167" alt="image" src="https://github.com/user-attachments/assets/07cab8b0-9901-440a-909e-fdb58c47ef53" />

## Menu 5 - Keluar >>>
- Menampilkan "HEHEHE Terima kasih sudah menggunakan layanan kami <3" dan program selesai.
<img width="697" height="263" alt="image" src="https://github.com/user-attachments/assets/2a9b74fe-72d0-4cec-906c-ce1029f807fe" />











