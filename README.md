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


# Tugas 4

1. Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?

    Django `UserCreationForm` adalah sebuah modul build-in yang meng-inherit dari class `ModelForm`. Modul tersebut digunakan untuk membuat user yang baru. `UserCreationForm` memiliki tiga fiels, yaitu: `username`, `password1`, dan `password2`.
    Kelebihan :
    - `UserCreationForm`sudah merupakan modul built-in, sehingga tidak perlu menulis sendiri logika pendaftaran pengguna.
    - `UserCreationForm` dapat dengan mudah disesuaikan dengan kebutuhan kita masing-masing.
    Kekurangan:
    - Logika atau tampilan dari `UserCreationForm` mungkin tidak sesuai dengan keinginan kita, sehingga kita perlu menyesuaikan atau membuat *form* kustom.
    - `UserCreationForm` memiliki ketergantungan pada Django, sehingga akan sulit ketika kita memilih untuk menggunakan *framework* lainnya.

2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

    Dalam konteks Django, autentikasi dan otorisasi adalah dua hal yang sangat penting dalam mengelola akses pengguna ke aplikasi web. Perbedaan keduanya adalah:
    - Autentikasi = Proses yang memverifikasi identitas pengguna yang mencoba unutk mengakses aplikasi. Contohnya adalah proses login.
    - Otorisasi = Proses yang terjadi setelah pengguna berhasil melakukan autentikasi. Hal ini mengacu pada kontrol yang diberikan kepada pengguna yang terautentikasi untuk mengakses atau melakukan tindakan tertentu dalam aplikasi.

3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

    *Cookies* adalah salah satu cara untuk menyimpan informasi dalam bentuk teks di sisi klien. Informasi ini dapat digunakan oleh *server web* untuk mengidentifikasi dan melacak sesi pengguna atau menyimpan data yang diperlukan untuk interaksi antar pengguna. Cara Django menggunakan cookies adalah dengan menyimpan data sesi pengguna, menggunakan *session middleware*, mendapatkan kunci unik, mengamankan data, dan mengatur waktu kadaluwarsa sesi.

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

    Secara umum, penggunaan *cookies* aman secara default dalam pengembangan web jika digunakan dengan benar dan jika diikuti dengan prinsip keamanan yang baik. Namun, ada beberapa potensial resiko yang harus diwaspadai, seperti:
    - Serangan Cross-Site Scripting (XSS).
    - Serangan Cross-Site Request Forgery (CSRF).
    - Enkripsikan data sensitif.
    - Pemantauan cookie, hapus cookie yang tidak lagi diperlukan atau kadaluwarsa.
    - Pemisahan cookie yang digunakan untuk tujuan berbeda.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    Checklist pertama: 
    
        - Jalankan virtual environment.
        - Buka berkas `views.py` di subdirektori `main`.
        - Tambahkan import `redirect`, `UserCreationForm`, dan `messages`.
        - Tambahkan potongan kode yang tersedia ke dalam fungsi `register`.
        - Buat berkas HTML dengan nama `register.html` pada folder `main/templates` dan isi dengan kode yang tersedia.
        - Buka `urls.py` pada subdirektori `main` dan impor fungsi `register` yang telah dibuat.
        - Tambahkan path url ke dalam `urlpatterns`.
        - Buka `views.py` pada subdirektori `main` dan buat fungsi dengan nama `login_user` yang menerima parameter `request`.
        - Tambahkan import `aunthenticate` dan `login`.
        - Tambahkan kode yang tersedia ke fungsi `login_user` tersebut.
        - Buat berkas HTML dengan nama `login.html` pada folder `main/templates`. Lalu isi berkas tersebut dengan kode yang tersedia.
        - Buka `urls.py` pada subdirektori `main` dan impor fungsi `login_user`.
        - Tambahkan path url ke dalam `urlpatterns` untuk mengakses fungsi yang sudah diimpor tadi.
        - Buka `views.py` pada subdirektori `main` dan buat fungsi dengan nama `logout_user` yang menerima parameter `request`.
        - Tambahkan import `logout`.
        - Tambahkan kode yang tersedia ke dalam fungsi `logout_user` yang telah dibuat.
        - Buka berkas `main.html` yang ada pada folder `main/templates`.
        - Tambahkan potongan kode yang tersedia setelah *hyperlink tag* untuk *Add New Product* pada berkas `main.html`.
        - Buka `urls.py` pada subdirektori `main` dan impor fungsi `logout_user` yang telah dibuat.
        - Tambahkan path url dalam `urlpatterns` untuk mengakses fungsi tersebut.

    Checklist kedua:

        - Buka `views.py` pada subdirektori `main` dan tambahkan import `login_required` pada bagian paling atas.
        - Tambahkan kode `@login_required(login_url='/login')` di atas fungsi `show_main`.
        - Jalankan prokyek Django dengan perintah `manage.py runserver` dan buka `http://localhost:8000/` di browser.
        - Buat dua akun pengguna dengan menekan `Register Now`, lalu isi username dan password, kemudian klik daftar.
        - Login dengan akun yang sudah dibuat.
        - Buat tiga product baru dengan menekan `Add New Product`. 
        - Logout lalu login kembali dengan akun lain yang telah dibuat, lalu buat tiga product lagi.
    
    Checklist ketiga:

        - Buka `models.py` pada subdirektori `main` dan tambahkan kode untuk mengimpor model.
        - Tambahkan potongan kode pada model `Product`.
        - Buka `views.py` pada `main` dan ubah potongan kode pada fungsi `create_product` menjadi seperti yang tersedia.
        - Ubah fungsi `show_main` menjadi seperti kode yange tersedia.
        - Simpan semua perubahan, lalu migrasikan dengan `python manage.py makemigrations`.
        - Saat muncul error. pilih `1`.
        - Ketik angka `1` lagi untuk menetapkan user.
        - Lakukan `python manage.py migrate` untuk mengaplikasikan migrasi.
    
    Checklist keempat:

        - Lakukan logout pada aplikasi web.
        - Buka `views.py` pada subdirektori `main` dan tambahkan import `HttpResponseRedirect`, `reverse`, dan `datetime`.
        - Pada fungsi `login_user`, tambahkan fungsi untuk menambah cookie bernama `last_login` dengan cara mengganti kode yang ada pada blok `if user is not None` menjadi potongan kode seperti yang tersedia.
        - Pada fungsi `show_main`, tambahkan potongan kode "`last_login`:request.COOKIES[`last_login`]" ke dalam variabel `context`.
        - Ubah fungsi `logout_user` menjadi seperti yang tersedia.
        - Buka `main.html` dan tambahkan potongan kode yang tersedia ke antara tabel dan tombol logout.
        - Jalankan proyek Django dan coba untuk login.


