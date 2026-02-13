# Pengertian ADT Array Satu Dimensi Meskipun Python memanfaatkan list, kita dapat membuat ADT Array untuk mewakili sekumpulan elemen linier dengan ukuran tetap. Berikut adalah fungsi-fungsi utama dalam ADT Array ini:
## Array(size): Membentuk array yang terdiri dari sejumlah elemen sesuai dengan size, di mana setiap elemen diatur dengan nilai None. Angka size harus lebih dari nol.

## length(): Menyediakan jumlah keseluruhan elemen dalam array.

## getitem(index): Mengambil nilai pada indeks tertentu menggunakan tanda kurung [].

## setitem(index, value): Memperbarui nilai pada indeks tertentu dengan value yang baru.

## clearing(value): Mengatur semua elemen dalam array menjadi nilai value yang telah ditentukan.

## iterator(): Menyediakan cara untuk melintasi setiap elemen array satu per satu.

Simulasi Game of Life
```bash
Menggunakan Array Dalam simulasi ini, array berfungsi untuk mengelola grid sel yang menggambarkan organisme yang hidup atau mati. Setiap perubahan generasi dilakukan dengan memeriksa tetangga di sekeliling sel berdasarkan aturan berikut:
```
Aturan Perkembangan Sel Setiap sel dalam grid akan mengubah statusnya di generasi berikutnya berdasarkan delapan tetangga yang ada di sekitarnya (baik secara vertikal, horizontal, maupun diagonal):

• Kelangsungan Hidup: Sel yang hidup akan tetap hidup jika dikelilingi oleh 2 atau 3 sel yang juga hidup.

• Kematian (Isolasi): Sel yang hidup akan mati jika tidak memiliki tetangga hidup atau hanya memiliki 1 tetangga hidup.

• Kematian (Overpopulasi): Sel yang hidup akan mati jika dikelilingi oleh 4 atau lebih sel hidup.

• Kelahiran: Sel yang mati akan menjadi hidup jika memiliki tepat 3 tetangga hidup.

## Implementasi Simulasi

• Pengaturan Awal: Pengguna menentukan lokasi organisme hidup di grid pada awalnya.

• Iterasi Generasi: Program menerapkan aturan yang telah disebutkan secara bersamaan pada semua sel untuk membentuk generasi baru.

• Pengamatan Pola: Simulasi dapat menghasilkan pola yang sepenuhnya mati, mencapai kondisi stabil (tidak ada perubahan lagi), atau menciptakan osilator yang berubah-ubah secara periodik.
