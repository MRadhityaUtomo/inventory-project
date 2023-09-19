<img width="114" alt="image" src="https://github.com/MRadhityaUtomo/inventory-project/assets/124948533/3d89fda0-9d44-48e2-8c6e-3aeac7b37439">

# TUGAS 1

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
# TUGAS 2

## Perbedaan form GET dan form POST <br>
GET, pada umumnya menyediakan parameter request dalam bentuk string yang langsung tertera pada URL seperti address tujuan, keys data, dan value dari key tersebut, Jika melakukan request GET pada server maka data akan dikembalikan tanpa ada modifikasi terhadap state/keadaan server.

POST, meletakkan parameter requestnya pada message body, serta melakukan modifikasi pada state server saat mengirim data kepada server.

## Perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data
![fish-spinning](https://github.com/MRadhityaUtomo/inventory-project/assets/124948533/107b791e-b53e-4866-ac27-ea5c943d8b20)


(Still in progress)

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
