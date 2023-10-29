# PageTurner - Kelompok C-06 PBP

## Anggota Kelompok:

> 1. Muhammad Najmi Briliant (2206082820)
> 2. Dinda Kirana Khairunnisa (2206082480)
> 3. Austin Susanto (2206025060)
> 4. Salsabila Aulia (2206082190)
> 5. Dimas Herjunodarpito Notoprayitno (2206081282)

## Deskripsi Aplikasi

PageTurner adalah platform e-commerce yang memungkinkan pengguna untuk membeli buku secara online. Selain fitur pembelian buku, platform ini juga memiliki sistem rekomendasi buku yang membantu pengguna menemukan buku-buku yang sesuai dengan minat dan preferensi mereka.

## Background

Saat ini, tingkat kesadaran literasi masyarakat Indonesia masih memprihatinkan. Menurut UNESCO, Indonesia berada di urutan kedua dari bawah soal literasi dunia dan minat baca masyarakat Indonesia hanya 0,0001%. Tingkat kesadaran literasi yang masih rendah dan minat baca yang sangat minim ini disebabkan oleh berbagai macam faktor. Salah satu faktornya adalah kurangnya ketertarikan dalam membaca karena salah pilih genre. Banyak masyarakat yang memutuskan untuk tidak membaca buku karena tidak menemukan buku-buku yang menarik bagi mereka sehingga minat mereka untuk membaca buku berkurang. Faktor lainnya yang menyebabkan tingkat literasi di Indonesia rendah adalah kendala aksesibilitas. Banyak masyarakat, terutama yang tinggal di daerah terpencil atau dengan akses terbatas ke perpustakaan fisik sehingga menghadapi kesulitan untuk mendapatkan buku. 

Kombinasi dari kurangnya ketertarikan karena salah pilih genre dan kendala aksesibilitas membentuk tantangan yang signifikan dalam upaya meningkatkan literasi. Inilah tempat dimana PageTurner dapat berperan. Dengan sistem rekomendasi buku yang cerdas, aplikasi ini dapat membantu masyarakat menemukan buku-buku yang sesuai dengan minat mereka, sehingga memotivasi mereka untuk membaca lebih banyak lagi. Selain itu, PageTurner menyediakan akses mudah ke berbagai jenis buku, mengatasi kendala aksesibilitas yang mungkin dihadapi oleh beberapa individu.

## Daftar Modul
Dataset: https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset

- **Library (Salsa)**
###### Menampilkan halaman rak buku yang berisi buku-buku sesuai pilihan user
-- User dapat membuat library yang disukai
-- User dapat melihat library yang dibuat user lainnya
-- User dapat edit dan delete library
-- User dapat menambahkan buku ke dalam library melalui page Detail Book

- **Wishlist (Dinda)**
###### Menampilkan halaman yang berisi buku-buku yang ingin dibeli oleh user suatu saat nanti
-- User dapat menambahkan buku ke dalam wishlist melalui page Catalogue dan Detail Book
-- User dapat delete buku dalam wishlist
-- User dapat menambahkan dan melihat notes

- **Review (Dimas)**
###### Menampilkan ulasan seperti rate dan komen mengenai suatu buku
-- User dapat mengakses fitur review melalui page Detail Book
-- User dapat memberikan review bintang dan komentar suatu buku
-- User dapat edit dan delete review bintang dan komentar suatu buku
-- User dapat melihat rating bintang dan komentar user lainnya

- **Book Catalogue (Austin)**
###### Halaman yang menampilkan detail buku dengan informasi seperti judul, penulis, sampul buku, ISBN, tahun, penerbit
-- User dapat menambahkan buku ke page Catalogue
-- User dapat delete buku yang telah ditambahkan ke katalog buku melalui page Detail Book
-- User dapat mengakses fitur menambahkan buku ke library, shopping cart, wishlist, review, delete buku

- **Shopping Cart (Najmi)**
###### Menampilkan dan mengelola isi keranjang belanja sebelum melakukan pembayaran
-- User dapat menambahkan buku ke shopping cart melalui page Catalogue dan Detail Book
-- User dapat delete buku dalam shopping cart
-- User dapat mengakses fitur detail buku dalam shopping cart
-- User dapat checkout shopping cart dengan autentikasi username


## User Role
| User | Login Page|Book Catalogue|Shopping List|Library|Recommended Library|Review|Wishlist|
| ------------ | ------------ |
|Guest           |  √ |   ||||||
|Logged in User||√|√|√||√||
|Premium Account||√|√|√|√|√|√|
