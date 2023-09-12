<img width="597" alt="image" src="https://github.com/MRadhityaUtomo/inventory-project/assets/124948533/9a84cb2a-3b65-4959-9933-afc8fa0f72fa">[Application Link](https://arti-facts.adaptable.app/)
## 1.Membuat Sebuah Project Django Baru
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
# add, commit, push
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
INSTALLED_APPS = [
  ...,
  'main',
  ...
]
```
+ Buatlah `urls.py` pada folder `APPNAME` dengan kode:
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
INSTALLED_APPS = [
    ...,
    'main',
    ...
]
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
