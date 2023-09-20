# TUGAS 2

Tautan app Adaptable: 
https://malaymart.adaptable.app

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step?

    Tick pertama:
    
    - Membuat direktori baru dengan nama `malaymart`.
    - Buka command prompt dengan dalam direktori yang telah dibuat.
    - Buat virtual environment dengan cara menjalankan perintah 
        `python -m venv env`
    - Aktifkan virtual environment dengan menjalankan perintah 
        `env\Scripts\activate.bat`
    - Membuat berkas `requirements.txt` dan isi dengan beberapa dependencies yang tersedia
    - Pasang depencies dengan perintah berikut
        `pip install -r requirements.txt`
    - Buat proyek Django dengan perintah 
        `django-admin startproject malaymart .`
    - Tambahkan * pada ALLOWED_HOSTS di settings.py untuk mengizinkan akses dari semua host.
    - Nonaktifkan server dengan menekan Ctrl+C dan nonaktifkan virtual environment dengan memasukkan perintah `deactivate`.
    - Buat repositori baru bernama `malaymart`.
    - Inisiasi direktori lokal `malaymart` sebagai repostori Git dengan membuat Branch utama baru menggunakan perintah `git branch -M main`, kemudian gunakan perintah `git remote add origin <URL_repo>` untuk menghubungkan direktori lokal dengan repositori Git.
    - Tambah berkas `.gitignore` di direktori dan isi dengan teks yang tersedia. Berkas ini tidak akan dimasukkan ke dalam versi kontrol Git.
    - Lakukan add, commit, dan push untuk menyimpan ke dari direktori lokal ke repositori Git

    Tick kedua:
    - Aktifkan virtual environment lagi menggunakan perintah `env\Scripts\activate.bat` dalam direktori proyek yang sudah dibuat
    - Buat aplikasi baru bernama `main` dengan perintah `python manage.py startapp main`
    - Tambahkan 'main' ke dalam variabel `INSTALLED_APPS` yang terdapat di berkas `settings.py`

    Tick ketiga:
    - Buka berkas `urls.py` yang terdapat dalam direktori `malaymart`
    - Impor fungsi `include` dari `django.urls`
    - Tambahkan rute URL untuk mengarahkan ke tampilan `main` di dalam variabel `urlpatterns`
    - Jalankan proyek Django dengan perintah `python manage.py runserver`
    
    Tick keempat:
    - Buka berkas `models.py` pada direktori app `main`
    - Isi berkas tersebut dengan kode yang tersedia
    - Tambahkan atribut-atribut wajib seperti `main`, `amount`, dan `description` dalam berkas tersebut.
    - Migrasikan model dengan perintah `python manage.py makemigrations`
    - Jalankan perintah `python manage.py migrate` untuk menerapkan migrasi ke dalam data lokal
    
    Tick kelima:
    - Tambahkan kode `from django.shortcuts import render` pada berkas `views.py` dalam aplikasi `main` untuk mengimpor fungsi render. Fungsi ini digunakan untuk me-render tampilan HTML
    - Tambahkan pula fungsi `show_main` yang tersedia
    
    Tick keenam:
    
    - Buat berkas `urls.py` dalam direktori `main`
    - Isi berkas tersebut dengan kode yang tersedia
    
    Tick ketujuh:
    - Login kedalam `Adaptable.io` 
    - Tekan tombol `New App` lalu pilih `connect an existing repository`
    - Hubungkan Adaptable dengan Github dan pilih `All Repositories` saat instalasi.
    - Pilih repositori `malaymart` sebagai basis aplikasi yang akan di deploy. Kemudian pilih branch main sebagai deployment branch.
    - Pilih `python app template` kemudian pilih `PostgreSQL`.
    - Sesuaikan versi Python dengan spesifikasinya. Kemudian pada bagian `Start Command` masukkan perintah `python manage.py migrate && gunicorn malaymart.wsgi`
    - Masukkan nama aplikasi
    - Centang bagian `HTTP Listener on PORT` dan klik `Deploy`
    
2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

    ![Alt text](image.png)

3. Jelaskan mengapa kita menggunakan virtual environment! Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment? 
    Virtual environment merupakan sebuah tool yang membantu untuk memisahkan dependensi yang diperlukan oleh proyek berbeda dengan membuat virtual environment python yang terisolasi. Bisa saja, namun sangat disarankan untuk menggunakan virtual environment dikarenakan akan memungkinkan kita untuk mengisolasi dependensi proyek dan mencegah konflik antara dependensi proyek yang berbeda

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya!
    MVC:
    - Model: Berisi representasi data dan logika bisnis aplikasi. Model bertugas untuk mendapatkan dan memanipulasi data, berkomunikasi dengan controller, berinteraksi dengan database, dll.
    - View: Tampilan yang digunakan untuk menampilkan data kepada pengguna. Tidak memiliki logika bisnis dan hanya bertugas menampilkan informasi ynag diberikan model.
    - Controller: Bertindak sebagai perantara antara mode dan view. Mengatur aliran data antara keduanya serta menangani permintaan pengguna.

    MVT:
    - Model: Sama seperti dalam MVC, bagian ini berisi logika bisnis dan representasi data.
    - View: Komponen yang menangani logika presentasi dan juga mengontrol bagaimana data yang dikelola oleh model akan ditampilkan kepada pengguna.
    - Template: Digunakan untuk merancang tampilan yang akhirnya akan diisi dengan data dari model melalui view.

    MVVM:
    - Model: Model yang digunakan mirip dengan MVC dimana model tersebut terdiri dari data dasar yang digunakan untuk menjalankan perangkat lunak.
    - View: Digunakan sebagai antarmuka grafis antara pengguna dan pola desain, serta menampilkan output dari data yang telah diproses.
    - ViewModel: Merupakan abstraksi dari View, dan sebagai penyedia pembungkus data model yang ditautkan. Terdiri dari model yang diubah menjadi View.

    Perbedaan:
    Perbedaan utama antara ketiga pendekatan ini adalah cara ketiganya mengatur logika bisnis, aliran data, dan interaksi antara komponen-komponennya. MVC adalah pendekatan yang lebih tua dan memiliki peran Controller yang lebih khas. MVT adalah varian Django yang menggantikan Controller dengan View dalam MVC. Sedangkan MVVM mengenalkan ViewModel yang bertanggung jawab atas sebagian besar logika presentasi dan interaksi pengguna.


# TUGAS 3

1. Apa perbedaan antara form POST dan form GET dalam Django?
    - `GET` = Biasanya digunakan untuk mengambil sumber daya atau data dari server tanpa mengubah apa pun di yang ada di server. Operasi ini dianggap aman dan idempoten, dimana beberapa permintaan yang identik akan mengasilkan hasil yang sama.
    - `POST` = Metode ini sering digunakan bersisian dengan HTML di frontend untuk membuat objek baru di server. Metode ini juga bisa untuk mengirim data ke server untuk disimpan atau diproses secara lebih lanjut.

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
    - `XML` (Extensible Markup Language) = Lebih umum digunakan untuk pertukaran data antar sistem atau aplikasi yang berbeda karena fleksibilitasnya dalam merepresentasikan berbagai jenis data. XML ini didesain untuk membawa data, bukan untuk menampilkannya.
    - `JSON` (JavaScript Object Notation) = Merupakan format yang umum digunakan dalam pengembangan web modern dan sering digunakan dalam pertukaran data antara server dan klien. Sintaks yang ada juga lebih ringkas dan lebih mudah untuk dibaca manusia.
    - `HTML` (Hypertext Markup Language) = Digunakan untuk membangun halaman web dan menampilkan konten secara visual di browser. HTML ini tidak digunakan untuk pertukaran data mentah antar aplikasi seperti XML atau JSON.

    Kesimpulannya, XML digunakan untuk merepresentasikan data struktural dengan struktur yang ketat. JSON digunakan untuk merepresentasikan data dalam bentuk objek dengan sintaks yang lebih ringkas. Sementara HTML digunakan untuk membangun halaman pada web dan menampilkan konten secara visual.

3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

    Pada zaman aplikasi web modern saat ini, JSON merupakan format yang paling sering digunakan untuk melakukan pertukaran data. Alasannya adalah:
    - Memiliki kecepatan pertukaran data dan hasil pencarian web yang tinggi. Hal ini akan memungkinkan komunikasi yang lebih cepat antar klien dan server.
    - JSON berbasis teks, lebih ringan, dan mempunyai format data yang mudah untuk diuraikan karena tidak memerlukan kode tambahan untuk melakukan penguraian.
    - JSON mempunyai dukungan untuk Cross-Platform sehingga format ini dapat digunakan untuk berbagai platform yang ada saat ini seperti smartphone, dan lain-lain.

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step?

    Checklist pertama:
    - Membuat berkas baru pada direktori `main` dengan nama `forms.py` dan tambahkan kode yang tersedia kedalam berkas tersebut.
    - Menambahkan beberapa import yang sudah tersedia pada berkas `views.py` yang berada di dalam direktori `main`.
    - Membuat fungsi baru pada `views.py` tersebut dengan nama `create_product` yang menerima parameter `request`. Kemudian masukkan kode yang tersedia kedalam fungsi tersebut.
    - Merubah fungsi `show_main` pada berkas `views.py` dengan kode yang tersedia.
    - Membuka berkas `urls.py` pada direktori `main` dan import fungsi `create_product` yang telah dibuat sebelumnya.
    - Menambahkan path url ke dalam variabel `urlpatterns` pada berkas `urls.py` di `main` untuk mengakses fungsi yang sudah diimport sebelumnya.
    - Membuat berkas HTML baru pada direktori `main/templates` dengan nama `create_product.html`. Isilah berkas tersebut dengan kode yang tersedia.
    - Membuka berkas `main.html`dan tambahkan kode yang telah disediakan ke dalam `{% block content %}` untuk menampilkan data produk dalam bentuk tabel serta menambahkan tombol `Add New Product` yang akan redirect ke halaman form.

    Checklist kedua dan ketiga:
    - Membuka `views.py` yang ada pada direktori `main` dan mengimpor `HttpResponse` dan `Serializer` pada bagian atas.
    - Membuat fungsi `show_xml` dan `show_json` yang menerima parameter `request`. 
    - Mengimpor fungsi `show_xml` dan `show_json` tersebut pada `urls.py` dan tambahkan kedua path nya ke dalam variabel `urlpatterns`.
    - Kembali membuka file `views.py` pada folder `main` dan buat dua fungsi baru bernama `show_xml_by_id` dan `show_json_by_id`. 
    - Buat sebuah variabel dalam kedua fungsi tersebut yang menyimpan hasil query dari data dengan id tertentu pada `Product`.
    - Mengimpor fungsi `show_xml_by_id` dan `show_json_by_id` tersebut pada `urls.py` dan tambahkan kedua path nya ke dalam variabel `urlpatterns`.

4. Screenshot Postman

    - HTML
     ![Alt text](image-1.png)

    - XML
     ![Alt text](image-4.png)

    - JSON
     ![Alt text](image-5.png)
    
    - XML by ID
     ![Alt text](image-6.png)

    - JSON by ID
     ![Alt text](image-7.png)
