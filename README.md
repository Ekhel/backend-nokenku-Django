# Sistem Digital Perikanan Terintegrasi
----------------------------------------------------

### Back End Applikasi

## System Requirements :
* Bahasa Utama :
  - Python
  - Version 3.6

* Framework :
  - Django
  - Version 2.2.3
  - Docker Version 2.2.3 - 3.0

* Database :
  - PostgreSQL

* Services :
  - Docker
  - travis-ci

* Library :
  - Django Rest Framework (DRF)
  - Django Crispy Forms

* Template :
  - Admin Pro (materialdesign)
----------------------------------------------------

## Develop

### Michael :

* Selasa 30 Juli 2019:
  - Buat Project Django
  - Instalasi requirements.txt
  - Memasang CI menggunakan https://travis-ci.org
  - Menambahkan dan Mengkonfigurasi File docker
  - Menambahkan Template
  - Install DRF(djangorestframework)
  - Membuat Modul users Cumstom User
  - Migrasi Database dan Menggunakan Database PostgreSQL
  - Menambahkan Halaman Login
  - Memanbahkan Fungsi Login dan Logout dan Memperbaiki urls app.

* Rabu 8 Agustus 2019:
  - Menambahkan models(Provinsi, Kabupaten, jenisikan, Nelayan, hasil_laut) [Solved]
  - Menambahkan Class Page Pada admin.py (Provinsi, Kabupaten, jenisikan, Nelayan, hasil_laut) [Solved]
  - Create Migrations [Solved]
  - Create Migrate [Not Solved]

* Kamis 9 Agustus 2019:
  - Menambahkan models(hasil_laut, Rekening) [Solved]
  - Menambahkan app frontend [Solved]
  - Menambahkan models order pada app frontend (frontend/models/order) [Solved]

* Sabtu 11 Agustus 2019:
  - Menambahkan Template Login [Solved]
  - Memperbaiki Fungsi Login dan Redirect dan Logout Redirect url [Solved]
  - Meperbaiki base_site.html untuk Master Layout [Solved]
  - Install lingting pylint member [Solved]
  - Setting django pylint [Solved]
  - Menambahkan View Nelayan [Solved]
  - Menambahkan View Hasil Laut [Solved]
