# Pencarian Lintasan Terpendek dengan UCS dan A*
## Tugas Kecil 3 IF2211 Strategi Algoritma

## Daftar Isi
* [Deskripsi Permasalahan](#deskripsi-permasalahan)
* [Struktur Repositori](#struktur-repositori)
* [Struktur File Input](#struktur-file-input)
* [Prasyarat Menjalankan Program](#prasyarat-menjalankan-program)
* [Cara Menjalankan Program](#cara-menjalankan-program)
* [Garis Besar Alur Program](#garis-besar-alur-program)
* [Identitas Kelompok](#identitas-kelompok)

## Deskripsi Permasalahan
Algoritma UCS (Uniform cost search) dan A* (atau A star) dapat digunakan untuk menentukan
lintasan terpendek dari suatu titik ke titik lain. Pada tugas kecil 3 ini, anda diminta menentukan
lintasan terpendek berdasarkan peta Google Map jalan-jalan di kota Bandung. Dari ruas-ruas jalan
di peta dibentuk graf. Simpul menyatakan persilangan jalan (simpang 3, 4 atau 5) atau ujung jalan.
Asumsikan jalan dapat dilalui dari dua arah. Bobot graf menyatakan jarak (m atau km) antar simpul.
Jarak antar dua simpul dapat dihitung dari koordinat kedua simpul menggunakan rumus jarak
Euclidean (berdasarkan koordinat) atau dapat menggunakan ruler di Google Map, atau cara
lainnya yang disediakan oleh Google Map

Langkah pertama di dalam program ini adalah membuat graf yang merepresentasikan peta (di area
tertentu, misalnya di sekitar Bandung Utara/Dago). Berdasarkan graf yang dibentuk, lalu program
menerima input simpul asal dan simpul tujuan, lalu menentukan lintasan terpendek antara
keduanya menggunakan algoritma UCS dan A*. Lintasan terpendek dapat ditampilkan pada
peta/graf (misalnya jalan-jalan yang menyatakan lintasan terpendek diberi warna merah). Nilai
heuristik yang dipakai adalah jarak garis lurus dari suatu titik ke tujuan.

## Struktur Repositori
```bash
└───Tucil3_13521098_13521168
    │ 
    ├───src
    |   ├───AStar.py
    |   ├───Coordinate.py
    |   ├───Graph.py
    |   ├───LinkedNode.py
    |   ├───main.py
    |   ├───Node.py
    |   ├───UCS.py
    |   ├───Utility.py
    │ 
    ├───test
        ├───output
        ├───alunalunbandung.txt
        ├───buahbatu.txt
        ├───gedebage.txt
        ├───itb.txt
```

## Struktur File Input
1. File input disimpan dalam format txt
2. Baris pertama adalah banyak simpul
3. Baris kedua adalah nama setiap simpul yang berupa bilangan bulat terurut dimulai dari 0 dan dipisahkan oleh spasi. Contohnya, jika terdapat lima simpul, maka baris kedua ditulis sebagai berikut `0 1 2 3 4` 
4. Jika banyak simpul adalah N, maka N baris selanjutnya adalah matriks ketetanggaan berbobot yang
berukuran NxN
5. N baris selanjutnya adalah koordinat yang terdiri dari garis lintang dan garis bujur yang dipisahkan
oleh spasi

## Prasyarat Menjalankan Program
1. Python
2. Library matplotlib
3. Library networkx

## Cara Menjalankan Program
1. Clone repository ini menggunakan menggunakan command `git clone https://github.com/satrianababan/Tucil3_13521098_13521168.git`.
2. Buat file input sesuai dengan struktur yang dijelaskan pada bagian sebelumnya, kemudian save file tersebut pada folder test.
3. Ubah current working direcory menjadi folder src.
4. Jalankan program menggunakan command `python main.py`. Kesalahan dapat terjadi jika command python
tidak dapat dijalankan karena kesalahan konfigurasi path interpreter python. Untuk mengatasi kesalahan ini, ganti python dengan path folder bin dari interpreter python. Contohnya, jika absolute path folder bin dari interpreter python pada komputer adalah /bin/python3, maka command yang dapat digunakan untuk menjalankan program ini adalah `/bin/python3 main.py`.

## Garis Besar Alur Program
1. Program meminta input file yang valid berdasarkan konfigurasi struktur file yang sudah dijelaskan pada bagian sebelumya.
2. Program menampilkan graf dari file input dengan representasi list ketetanggaan pada terminal.
3. Program menampilkan graf secara visual menggunakan matplotlib. Hal ini ditandai dengan munculnya window dari matplotlib. Selain itu, gambar graf juga disimpan ke dalam folder output dengan format nama sama dengan file input yang ekstensinya berupa png. Contohnya, jika file input bernama `itb.txt`, maka dihasilkan gambar graf `itb.png` pada folder output.
4. Jika ingin melanjutkan program, close window matplotlib
5. Program meminta simpul asal dan simpul tujuan, serta metode pencarian yang diinginkan.
6. Program menampilkan lintasan terpendek pada terminal beserta jaraknya. 
7. Program menampilkan lintasan terpendek secara visual menggunakan matplotlib. Hal ini ditandai dengan munculnya window dari matplotlib. Selain itu, gambar graf yang sudah ada lintasan terdekat antara dua simpul masukan tersebut disimpan ke dalam folder output dengan format nama berupa file input ditambah dengan metode pencarian yang ekstensinya berupa png. Contohnya, jika file input bernama `itb.txt` dan metode pencarian yang dipilih adalah UCS, maka dihasilkan gambar `itbUCS.png` pada folder output.
8. Program berhenti ketika window matplotlib ditutup.

## Identitas Kelompok
| NIM  | Nama |
| ------------- | ------------- |
| 13521098 | Fazel Ginanda |
| 13521168  | Satria Octavianus Nababan  |
