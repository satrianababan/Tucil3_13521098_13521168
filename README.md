# Pencarian Lintasan Terpendek dengan UCS dan A*
## Tugas Kecil 3 IF2211 Strategi Algoritma

## Daftar Isi
* [Deskripsi Permasalahan](#deskripsi-permasalahan)
* [Struktur](#struktur)
* [Cara Menjalankan Program](#cara-menjalankan-program)
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

## Struktur
```bash
└───Tucil3_13521098_13521168
    │ 
    ├───src
        ├───Astar.py
        ├───Coordinate.py
        ├───Graph.py
        ├───GUI.py
        ├───LinkedNode.py
        ├───main.py
        ├───Node.py
        ├───Path.py
        ├───UCS.py
        ├───Utility.py
        │ 
        └───test
            ├───alunalunbandung.txt
            ├───buahbatu.txt
            ├───gedebage.txt
            ├───itb.txt
```

## Cara Menjalankan Program
1. Clone repository ini menggunakan menggunakan command `git clone https://github.com/satrianababan/Tucil3_13521098_13521168.git`.
2. Buat file input sesuai dengan struktur yang dijelaskan pada bagian sebelumnya, kemudian save file tersebut pada folder test.
3. Jalankan program menggunakan command `python main.py`.

## Identitas Kelompok
### Nama Kelompok : pharserr
| NIM  | Nama |
| ------------- | ------------- |
| 13521098 | Fazel Ginanda |
| 13521168  | Satria Octavianus Nababan  |