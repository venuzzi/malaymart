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



    