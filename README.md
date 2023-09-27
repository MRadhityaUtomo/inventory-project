![fish-spinning](https://github.com/MRadhityaUtomo/inventory-project/assets/124948533/da13490f-0e1e-45f1-995a-61a2af637637)

# TUGAS 2

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

## 2. Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet. (Note : Better practice untuk deploy saat semuanya sudah beres)
+ Melakukan deployment aplikasi menggunakan adaptable dengan repo pada github.
+ Setting pada deployment :
```
Python App Template sebagai template deployment, PostgreSQL sebagai tipe basis data yang akan digunakan, versi Python dengan spesifikasi aplikasimu (my case it's 3.10.)
Pada bagian Start Command masukkan perintah python manage.py migrate && gunicorn appname.wsgi.
Masukkan nama aplikasi yang juga akan menjadi nama domain situs web aplikasimu.
Centang bagian HTTP Listener on PORT dan klik Deploy App untuk memulai proses deployment aplikasi.
```

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
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

# TUGAS 3

## Perbedaan form GET dan form POST <br>
GET, pada umumnya menyediakan parameter request dalam bentuk string yang langsung tertera pada URL seperti address tujuan, keys data, dan value dari key tersebut, Jika melakukan request GET pada server maka data akan dikembalikan tanpa ada modifikasi terhadap state/keadaan server.

POST, meletakkan parameter requestnya pada message body, serta melakukan modifikasi pada state server saat mengirim data kepada server.

## Perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data
<br>
XML (eXtensible Markup Language):
- Struktur Data: XML menyimpan data dalam struktur pohon dengan namespace untuk mengkategorikan data. Ini memungkinkan untuk representasi hierarki yang kompleks.
- Tag: XML memiliki tag yang telah ditentukan, tetapi pengguna masih dapat membuat atau menambahkan tag kustom sesuai kebutuhan.
- Jenis Data: XML mendukung berbagai jenis data, seperti string, integer, boolean, tanggal, gambar, namespace, dan tipe kustom sesuai kebutuhan.
<br>
JSON (JavaScript Object Notation):
- Struktur Data: JSON menyimpan data dalam struktur mirip dengan dictionary pada Python, menggunakan pasangan key-value. Ini menghasilkan struktur data yang lebih sederhana dan ringkas dibandingkan dengan XML.
- Tag: JSON tidak menggunakan tag seperti XML, tetapi mengandalkan key-value pairs, sehingga sintaksisnya lebih ringkas.
- Jenis Data: JSON biasanya digunakan untuk mengirim data melalui internet karena formatnya ringkas dan mudah ditulis. Ini memiliki dukungan yang kuat dalam pengembangan aplikasi web dan API, terutama karena keterkaitannya dengan - JavaScript.
<br>
HTML (HyperText Markup Language):
- Struktur Data: HTML digunakan untuk membangun struktur dan tampilan halaman web, bukan untuk pengiriman data. Ini memiliki tag yang telah ditent

<br>

## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
### JSON sering digunakan dalam pertukaran data web modern karena :
- Menggunakan bahasa yang dapat dimengerti manusia
- Menggunakan format key dan value dengan array
- Dibanding XML, JSON tidak membutuhkan tag khusus, attributes, atau skema.
- compatible dengan banyak/semua bahasa programming
- memiliki native format JavaScript dan mudah diparse oleh browser.

## Step by Step <br>
1. Mengatur routing
- Agar lebih sesuai dengan format penampilan db yang kita incar akan lebih baik mengubah path `main/` menjadi `` pada `inventory_project` -> `urls.py` -> `urlpatterns` sebagai berikut

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    
]
```
menjadi 

```python
urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
]
```
<br>
<br>
2. Membuat kerangka Views
-- Kerangka atau skeleton dibutuhkan sebagai basis tampilan web, serta me-*refine* code sebelumnya

+ buat new folder `templates` dalam root folder (inventory_system) -> new file `base.html` -> gunakan kerangka berikut untuk merapihkan tampilan web :
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        />
        {% block meta %}
        {% endblock meta %}
    </head>

    <body>
        {% block content %}
        {% endblock content %}
    </body>
</html>
```

+ sambungkan base.html pada `inventory_project` melalui `inventory_project` -> `settings.py` -> `TEMPLATES` :
from 
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

menjadi 

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],   # <- Perubahan kode, akan menyambungkan folder templates dari root folder ke dalam project folder.
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

+ Ubahlah format pada folder `main` -> `templates` -> `main.html` dengan format yang sesuai :
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

menjadi 

```html
{% extends 'base.html' %}

{% block content %}
    <h1>Artifacts</h1>

    <h5>Name:</h5>
    <p>{{name}}</p>

    <h5>Class:</h5>
    <p>{{class}}</p>
{% endblock content %}
```
<br>
<br>
3. Membuat Form Input Data dan Menampilkan Data Produk Pada HTML
-- Untuk menambahkan suatu cara agar user dapat menginput atau berinteraksi dengan web, dilakukan dengan menambahkan form input yang akan memproses data dan menyimpannya di database
+ Buatlah `forms.py` pada `main`, lalu isi dengan kode berikut :

```python
from django.forms import ModelForm
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name",
                  "amount", 
                  "connection", 
                  "description"]
```
+ Tambahkan beberapa import pada `main` -> `views.py` :
dari  
```python
from django.shortcuts import render
...

```

menjadi
```python
from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
...

```

+ Tambahkan function baru untuk menambahkan suatu item dari mengisi form (tetap di `views.py`):
```python
def add_Item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "add_Item.html", context)
```
+ Tambahkan function dan form baru pada main page (`show_main`) :
```python
def show_main(request):
    context = {
        'name': 'Muhammad Radhitya Utomo',
        'class': 'PBP D',
        'description': 'The ultimate wizard in terms of attack and defense. come and enter your wares traveler, for they will be your memoirs, reminders, keepsakes, of your adventure',
        'attack': 2500,
        'defense': 2100,
    }

    return render(request, "main.html", context)
```

menjadi

```python
def show_main(request):
    item = Item.objects.all()  # Tambahkan import `from main.models import Item`

    context = {
        'name': 'Muhammad Radhitya Utomo',
        'class': 'PBP D',
        'description': 'The ultimate wizard in terms of attack and defense.'
        'attack': 2500,
        'defense': 2100,
        'items' : item,
    }
```

+ Sambungkan url function input pada `main` -> `urls.py` :
```python
# Tambahkan import `from main.views import show_main, add_Item`
# Tambahkan pada `urlpattern` :
urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-item', add_Item, name='add_item'),
]
```

+ Buat file html baru pada templates `main` dengan nama `add_item.html`dan isi dengan kode berikut :

```html
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Entry</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Item"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
ini akan mengubah tampilan main page dan menambahkan opsi baru untuk menambahkan item.

+ Tambahkan tampilan tabel untuk fungsi penambahan item pada `main` -> `templates` -> `main.html` :
```html
<table>
    <tr>
        <th>Name</th>
        <th>Amount</th>
        <th>Connection</th>
        <th>Description</th>
        <th>Date Added</th>
    </tr>

    {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}

    {% for item in items %}
        <tr>
            <td>{{item.name}}</td>
            <td>{{item.amount}}</td>
            <td>{{item.connection}}</td>
	    <td>{{item.description}}</td>
            <td>{{item.date_added}}</td>
        </tr>
    {% endfor %}
</table>

<br />

<a href="{% url 'main:add_item' %}">
    <button>
        Add New Entry
    </button>
</a>

```
<br>
<br>
4. Mengembalikan data (JSON dan XML)

+ Import beberapa resource dari django ke `main` -> `views.py`:

```python
from django.http import HttpResponse
from django.core import serializers
```

tambahkan function untuk menampilkan data dalam XML dan JSON :

XML :
```python
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

JSON :
```python
def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
<br>
<br>
5. Mengakses Data item dengan id
+ tambahkan function - function baru pada `main` -> `views.py`:

```python
def show_xml(request):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
+ import function tersebut ke dalam `main` -> `urls.py` :
```python
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 
```

+ Tambahkan lagi function kedalam `main` -> `urls.py` -> `urlpatterns`:
```python
path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
```

<br>
<br>

## Implementasi 
1. HTML <br>

   ![messageImage_1695131518037](https://github.com/MRadhityaUtomo/inventory-project/assets/124948533/a4d7aa6b-6b0c-459b-8244-3802947967a6)
   ![messageImage_1695131536131](https://github.com/MRadhityaUtomo/inventory-project/assets/124948533/23745c49-3d64-4878-8207-a3d25d2e8cb9)
   
<br>
2. XML <br>

   ![messageImage_1695131474363](https://github.com/MRadhityaUtomo/inventory-project/assets/124948533/b8f26b81-6c2a-4815-b2fd-02c8696958e1)
   ![messageImage_1695131496132](https://github.com/MRadhityaUtomo/inventory-project/assets/124948533/59f278f1-6e7e-44c3-8287-d9b3136e1ffb)
   
<br>
3. JSON <br>

   ![messageImage_1694880338823](https://github.com/MRadhityaUtomo/inventory-project/assets/124948533/a7f1f6f7-befc-4602-884c-73c4a0506e4c)
   ![messageImage_1694880358225](https://github.com/MRadhityaUtomo/inventory-project/assets/124948533/2e1f9ae9-4f5a-488d-816a-b15b8dc253ce)
   
<br>
4. XML by id <br>

   ![messageImage_1695132549760](https://github.com/MRadhityaUtomo/inventory-project/assets/124948533/04175b87-8b8e-45a3-981e-52783f6eccce)
   
<br>
5. JSON by id <br>

   ![messageImage_1695132656203](https://github.com/MRadhityaUtomo/inventory-project/assets/124948533/85bca61f-1e0c-418f-8c9a-86a008a46931)

<br>
<br>
<br>
<br>

# Tugas 4

Tugas 4 answers

1. Django `UserCreationForm`
Sebuah modul django yang merupakan subclass dari class `ModelForm`, biasa digunakan untuk menulis data seperti username dan password ke database. Seperti `ModelForm` yang digunakan untuk menuliskan atau menambahkan sebuah model object baru kedalam database, cara kerjanya mirip dengan tambahan sistem autentikasi untuk fungsi login dan access restriction.

+ Kelebihan:
> 1. Mudah digunakan karena sudah menyediakan basis form untuk registrasi user seperti username dan password.
> 2. Built-in validation. Artinya sudah memiliki sistem untuk otentikasi ketepatan username dan password saat login.
> 3. Terintegrasi dengan authentication system. sudah terintegrasi dengan user authentication system django.

<br>
- Kekurangan
> 1. Field yang disediakan hanya basis saja seperti `username` dan `password`. Jika ingin menambahkan form pengisian data user lagi dapat dilakukan dengan modifikasi form yang sudah ada atau membuatnya dari awal.
> 2. tidak ada verifikasi email -> tidak dapat melakukan integrasi 2fa protection dengan mudah.

note : Untuk menambahkan custom forms untuk data user dapat dilakukan dengan membuat class form baru yang terdapat `inheritance` dari `UserCreationForm`.

2. Difference between autentikasi and otorisasi <br>
i. Autentikasi : 
- Proses verifikasi identitas sebuah user dan melakukan konfirmasi sebelum memberikan akses kepada resource atau aksi kepada suatu aplikasi django
- Di dalam Django terdapat metode - metode autentikasi seperti login dan logout
- Django menggunakan sistem sessions dan middleware untuk autentikasi.
> - session dihandle dengan cookie yaitu sebuah session id yang menahan sebuah user yang sudah login, selama cookie tersebut masih menyimpan data login dari suatu user, user tersebut memiliki akses ke informasinya yang dibutuhkan dari suatu aplikasi.
(Ex : sebuah user login kedalam aplikasi seperti scele, maka scele akan mengambil data login tersebut sebagai cookie. User dapat pindah - pindah tab atau close tab dan membukannya lagi di browser yang sama tanpa harus login ulang karena cookie dengan data login user tersebut masih disimpan scele. Ini dinamakan `holding state`)

- Kepentingan dari autentikasi yaitu untuk menjaga keamanan informasi suatu user dari user lain atau faktor lain, misal suatu data sensitif user1 hanya dapat diakses dengan username dan password user1, user2 tidak dapat mengaksesnya dengan username dan password user2.

<br>

ii. Otorisasi:
- Sebuah proses pemberian akses dalam konteks apa saja aksi atau sumber daya suatu aplikasi yang dapat diakses oleh user
(Ex : akses user1 dalam mengatur regulasi user - user lain)
- Django menyediakan fitur - fitur seperti
```
1. groups
2. permissions
3. decorators
```
- Pentingnya otorisasi adalah untuk mengatur siapa yang dapat mengakses data dan sumber daya apa. User pengguna biasa hanya dapat menggunakan aplikasi sebagai pengguna -> berbeda dengan admin yang memiliki kekuatan untuk modifikasi user lain atau aplikasi itu sendiri. (Ex : sistem kekuasaan suatu negara).

<br>
<br>
3. Cookies dalam Django
- Cookies adalah text file berukuran kecil berisi informasi seperti session ID, preferensi user, authentication tokens, dan data lain berkaitan dengan interaksi seorang user dengan web app.
- HTTP memiliki `stateless protocol` yang berarti suatu request tidak berhubungan dengan request lain -> tiap request memilki connection terhadap server berbeda - beda yang harus dihubungkan ulang tiap kali melakukan request -> ini menyebabkan user diminta untuk login ulang jika membuka tab dengan web sama.
- Cookie dapat menghilangkan fenomena tersebut dengan `holding state`
- Django menggunakan cookies untuk mengatur sesi atau pemakaian aplikasi suatu user. Data user saat login disimpan di Cookie sebagai sessionid yang berisi identifier agar user bisa melakukan request banyak dalam satu sesi, ini disebut `holding state`.
(Ex : 2 atau lebih tab berbeda dalam suatu browser dengan web aplikasi yang sama akan tetap logged in ke akun yang sama)
<br>
<br>

4. Keamanan penggunaan `Cookies` dan resiko penggunaannya 
- Secara umum Cookie aman jika dilakukan dengan best practice berikut :
```
1. Menggunakan Cookies hanya jika dibutuhkan dengan membatasi jumlah dan ukurannya untuk optimisasi performa web
2. Memasang expiration date yang sesuai agar tidak disimpan selamanya
3. Mengamankan Cookies dengan menggunakan protokol HTTPS, mengatur atribut Secure dan HttpOnly, dan menerapkan perlindungan terhadap Cross-Site Request Forgery (CSRF).
4. Mengikuti regulasi data protections dengan menyediakan informasi tentang penggunaan Cookies yang jelas dan transparan kepada user serta mendapatkan perijinan penggunaan Cookies dari user, membolehkan user untuk keluar atau masuk dalam penggunaan Cookie.
5. Rajin melakukan review dan update pada peraturan atau policy Cookies.
```
- Berikut resiko dalam penggunaan Cookie yang tidak hati - hati:
```
1. Permasalahan privasi, cookies dapat melacak kelakuan user dan menyimpan informasi sensitif. Resiko dapat terlihat relasinya dengan Third-party cookies dan prizinan dari user.
2. Kerentanan keamanan, Cookies rentan terhadap penyerangan virtual seperti XSS dan CSRF.
3. Pelanggaran data, jika suatu Cookie mengandung informasi amat sensitif maka akan menjadi target bagi hacker dan berkontribusi ke data breach lainnya.
4. ketidakpatuhan kepada regulasi seperti the General Data Protection Regulation (GDPR).

```
<br>
<br>

## Step by Step

<br>
# TUGAS 4
## Registration, Login, and Logout functions

1. Import semua komponen yang dibutuhkan terlebih dahulu pada `main` -> `views.py` :

```python
# Registration form imports
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
```
<br>

```python
# Login functions imports 
from django.contrib.auth import authenticate, login
```
<br>

```python
# Logout function imports
from django.contrib.auth import logout
```
<br>
<br>

2. Menambahkan functions untuk masing - masing fitur dan finalisasi html page:
<br>
- 1. Register
<br>

> `main` -> `views.py`
```python
# Register function
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context
```
<br>

> html page <br>
masukkan code untuk menampilkan page `register` pada web. new file pada `main` -> `templates` -> [new]`register.html` :
```html
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```
<br>

> sambungkan url dengan menambahkan url function register ke `main` -> `urls.py` :
```python
from main.views import register
```
dan menambahkan path url pada `urlpatterns` :
```python
path('register/', register, name='register'),
```
<br>
<br>

- 2. Login
<br>

> `main` -> `views.py`
```python
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```
<br>

> html page <br>
masukkan code untuk menampilkan page `login` pada web. new file pada `main` -> `templates` -> [new]`login.html` :
```html
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

</div>

{% endblock content %}
```
<br>

> sambungkan url dengan menambahkan url function register ke `main` -> `urls.py` :
```python
from main.views import login_user
```
dan menambahkan path url pada `urlpatterns` :
```python
path('login/', login_user, name='login'),
```
<br>
<br>

- 3. Logout
<br>

> `main` -> `views.py`
```python
def logout_user(request):
    logout(request)
    return redirect('main:login')
```
<br>

> html page <br>
masukkan code untuk menampilkan page `logout` pada web. 'main' -> 'templates' -> `main.html` -> sesuaikan dengan lokasi yang logis (pada tugas ini akan di sebelah tombol create item) :
```html
...
<br />

<a href="{% url 'main:add_item' %}">
    <button>
        Add New Entry
    </button>
</a>

# LOKASI TOMBOL LOGOUT
<a href="{% url 'main:logout' %}">
    <button>
        Logout
    </button>
</a>
# LOKASI TOMBOL LOGOUT ^

{% endblock content %}
```
<br>
<br>

3. Menambahkan logika/metode perestriksian, agar dapat dilakukan otentikasi user dengan benar :
+ Tambahkan syarat login untuk masuk pada web. `main` -> `views.py`:
import
```python
from django.contrib.auth.decorators import login_required
```
<br>

tambahkan diatas function `show_main`
```python
@login_required(login_url='/login')
```
<br>
<br>

4. Menghubungkan model dengan user
Agar data user yang ditampilkan adalah user yang sedang login tanpa harus melakukan hardcoding :
+ to `main` -> `models.py` :
import
```python
from django.contrib.auth.models import User
```
tambahkan attribute baru pada model `Item`:
```python
user = models.ForeignKey(User, on_delete=models.CASCADE)
```
<br>
result :

```python
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  #NEW
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    omen = models.IntegerField(default=0)
    space = models.IntegerField(default=0)
    date_added = models.DateField(auto_now_add=True)
```
<br>

+ Ubah isi `add_item` pada `views.py`:
`main` -> `views.py` -> `add_item` :
from
```python
def add_Item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "add_Item.html", context)
```
ubah menjadi 
```python
def add_Item(request):
#NEW
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))
#NEW ^

    context = {'form': form}
    return render(request, "add_Item.html", context)
```
<br>
<br>

+ ubah data `show_main` pada `views.py` :
`main` -> `views.py` -> `show_main` :
from
```python
def show_main(request):
    item = Item.objects.all()

    context = {
        'name': 'Muhammad Radhitya Utomo',
...
```
to :
```python
def show_main(request):
    item = Item.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
...
```
<br>

+ Lakukan migrasi untuk menyimpan semua modifikasi file
```sh
python manage.py makemigrations
```
akan ada prompt untuk menambahkan default parameter. Masukan 1 lalu enter, masukan 1 lagi lalu enter. Ini akan menetapakan user 1 sebagai default.

<br>

```sh
python manage.py migrate
```
<br>
<br>

5. Menambahkan informasi `last login` untuk user
+ import `datetime` ke `main` -> `views.py`:
```python
import datetime
```
<br>

ubah `main` -> `views.py` -> `login_user` -> `if user is not None: ` :
from
```python
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
```
to
```python
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
```
<br>

+ `main` -> `views.py` -> `show_main` -> `context` :
add `'last_login': request.COOKIES['last_login'],`
```python
def show_main(request):
    item = Item.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        'class': 'PBP D',
        'description': 'The ultimate wizard in terms of attack and defense. come and enter your wares traveler, for they will be your memoirs, reminders, keepsakes, of your adventure',
        'items' : item,
        'count' : item.count,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)
```
<br>

+ add the notification text on the main page
`main` -> `templates` -> `main.html` :
letakkan di bawah `add item` :
```html
<h5>Sesi terakhir login: {{ last_login }}</h5>
```
<br>
<br>
<br>
<br>

## BONUS TUGAS 4
<br>
<img width="1197" alt="image" src="https://github.com/MRadhityaUtomo/inventory-project/assets/124948533/1eb7f95a-c932-4372-97a5-5129135b3b27">
-------------------------------------------------------------------------------------------------------------------------------------------------
<img width="1136" alt="image2" src="https://github.com/MRadhityaUtomo/inventory-project/assets/124948533/3de79b00-a77b-48c1-8504-714196a8d88c">




