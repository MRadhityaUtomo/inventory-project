<img width="114" alt="image" src="https://github.com/MRadhityaUtomo/inventory-project/assets/124948533/3d89fda0-9d44-48e2-8c6e-3aeac7b37439">

[Application Link](https://arti-facts.adaptable.app/)
# Step by Step
## 1. Membuat Sebuah Project Django Baru
-- Inisiasi Repo Github --
+ Membuat direktori baru untuk repo pada github (serta melakukan config lain dan cloning)
+ Membuat berkas `requirements.txt` berisikan :
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
+ Install dependencies dari `requirements.txt` ke dalam repo proyek dengan :
(pada proses ini saya menggunakan env)
```sh
python -m venv venv # Membuat virtual
# Untuk menyalakan venv 
env\Scripts\activate.bat # pada proses saya menggunakan Windows
pip install -r requirements.txt # Instalasi dependencies
```
+ Membuat project django baru dengan :
`django-admin startproject <Nama Proyek> .`
+ Menambahkan `"*"` pada `ALLOWED_HOST` di settings.py dalam direktori proyek (settings.py muncul sebagai framework setelah inisiasi proyek django baru).
  + `python manage.py runserver` untuk menyalakan koneksi ke django dan dapat di test pada link ->   
    `http://localhost:8000 `, jika roket sudah beranimasi maka koneksi sudah established
## add, commit, push
+ Membuat `.gitignore` yang akan mengabaikan folder env dan db.sqlite3 saat melakukan add,commit,push.

## 2. Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
+ Melakukan deployment aplikasi menggunakan adaptable dengan repo pada github.

## 3. Membuat aplikasi dengan nama main pada proyek tersebut.
+ Menjalankan command :
`python manage.py startapp main` pada command terminal direktori proyek.
+ Membuat folder `templates` pada main, dan didalamnya membuat file `main.html`

## 4. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
+ Menambahkan 'main' pada `INSTALLED_APPS` dalam `settings.py` direktori proyek :
```python
INSTALLED_APPS = [
    ...,
    'main',
    ...
]
```
+ Inisiasi link aplikasi main dengan menambahkan pola url pada `urlpatterns` difile proyek (bukan main)
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    
]
```

## 5. Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib
+ Implementasi django import : models dan membuat model `item` dengan attribute pada tugas, serta attribute tambahan :
```python
from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    attack = models.IntegerField(default='0000000', editable=False)
    defense = models.IntegerField(default='0000000', editable=False)
```

## 6. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
+ Menambahkan render pada `views.py` untuk menampilkan data pada `models.py`
```python
from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Muhammad Radhitya Utomo',
        'class': 'PBP D',
        'description': 'The ultimate wizard in terms of attack and defense',
        'attack': 2500,
        'defense': 2100,
        'amount': 64,

    }

    return render(request, "main.html", context)
```
+ Menyesuaikan tampilan pada templates `main.html`
```html
<h1>Arti-Facts</h1>

<h5>Name: </h5>
<p>{{ name }}</p> <!-- Ubahlah sesuai dengan nama kamu -->
<h5>Class: </h5>
<p>{{ class }}</p> <!-- Ubahlah sesuai dengan kelas kamu -->
<h5>Description: </h5>
<p>{{ description }}</p> <!-- Ubahlah sesuai dengan kelas kamu -->
<h5>Attack: </h5>
<p>{{ attack }}</p> <!-- Ubahlah sesuai dengan kelas kamu -->
<h5>Defense: </h5>
<p>{{ defense }}</p> <!-- Ubahlah sesuai dengan kelas kamu -->
<h5>Amount: </h5>
<p>{{ amount }}</p> <!-- Ubahlah sesuai dengan kelas kamu -->
```

## 7. Finishing
+ Melakukan migration untuk mengubah models dengan command :
```sh
python manage.py makemigrations
python manage.py migrate
```
+ Add, Commit, Push dan menunggu deploy dari adaptable.

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![Flowchart](https://github.com/MRadhityaUtomo/inventory-project/assets/124948533/524162bc-8c91-4699-bea1-b01d1cd17dda)
1. Link atau request user akan diproses sebagai client yang mengirim request kepada browser
2. Request tersebut bernama HTTP Request dan akan diproses oleh `urls.py` dengan mencari url pattern yang cocok dengan request client didalam file tersebut
3. Jika url pattern ditemukan, `urls.py` akan memanggil function dalam `views.py` sesuai dengan url pada request
4. `views.py` mendapatkan data serta cara kerja/logika aplikasi dari model - model  pada `models.py`
5. `views.py` akan mengirimkan render atau tampilan halaman request menggunakan template, dalam contoh ini `main.html`
6. tampilan tersebut lalu dikirim kembali ke client/user sebagai HTTP Response


## Mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
+ Virtual enviroment dibutuhkan untuk melakukan organisasi dependencies antara proyek agar tidak saling mengganggu development satu sama lain.
+ Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, namun bad-practice dengan beberapa resiko sebagai berikut :
```
+ Dependency conflicts antar proyek
+ Tidak adanya control terhadap versi
+ Security vulnerabilities
+ Kurangnya portability dan reproducibility
+ Mempersulit setup dan maintenance
```

## Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
1. MVC (Model-View-Controller) : Sebuah pola pada industri software, dikemukakan oleh Trygve Reenskaug pada 1970. Inti dari pola tersebut adalah membagi masalah dalam aplikasi mejadi 3 bagian :
- Model : Merepresentasikan data dan logika business aplikasi. Memproses, penyimpanan, dan mengatur data dilakukan pada Model.
- View : Fokus kepada user interface aplikasi atau visual dari pengoperasian aplikasi yang dapat digunakan user. Data untuk di tampilkan diambil dari model.
- Controller : Perantara antara Model dan View, Controller akan menerima input user dari View dan di proses untuk memperbaharui Model. Model akan melakukan notifikasi kepada controller untuk me-refresh View dengan data baru.


2. MVT (Model-View-Template) : Sebuah achitecture untuk programming, paling umum dipakai oleh Django.
Terdapat 3 bagian dari MVT : 
- Model : interface data dan struktur logika untuk sebuah aplikasi
- View : Melakukan render pada template, menerima request HTTP dan mengembalikan respons HTTP
- Template : sebuah presentasi data dari Model, dapat menjadi static atau dinamis.

Perbedaannya dengan MVC adalah controller diimplementasi oleh framework dan menggunakan URL mapping. Modifikasi juga lebih mudah dilakukan dibanding MVC.


3. MVVM (Model-View-ViewModel) : Sebuah lanjutan dari MVP, lebih fokus kepada simplifikasi development UI serta memisahkan concern dan meningkatkan testability (kejelasan suatu hasil tes untuk program).
- Model : Merepresentasikan data dan logika business aplikasi, bertanggung jawab dalam penyimpanan, pengambilan, dan proses data penting.
- View : User Interface, menampilkan data kepada user. Biasanya didesain dengan bahasa seperti XAML.
- ViewModel : Sebuah perantara untuk Model dan View. Menjalankan operasi - operasi untuk mengubah data Model ke dalam format yang dapat diterima View.