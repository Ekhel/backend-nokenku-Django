from django.db import models

class Provinsi(models.Model):
    kode_provinsi = models.IntegerField()
    nama_provinsi = models.CharField(max_length=50)

    def __str__(self):
        return self.nama_provinsi

class Kabupaten(models.Model):
    provinsi = models.ForeignKey(Provinsi, on_delete=models.CASCADE)
    kode_kabupaten = models.IntegerField()
    nama_kabupaten = models.CharField(max_length=50)

    def __str__(self):
        return self.nama_kabupaten


class Nelayan(models.Model):
    id_nelayan = models.IntegerField(primary_key=True)
    provinsi = models.ForeignKey(Provinsi, on_delete=models.CASCADE)
    kabupaten = models.ForeignKey(Kabupaten, on_delete=models.CASCADE)
    nama_nelayan = models.CharField(max_length=150)
    armada = models.CharField(max_length=10)
    tanggal_lahir = models.DateField()
    no_kontak = models.CharField(max_length=15)

    def __str__(self):
        return self.nama_nelayan

class Jenisikan(models.Model):
    id_ikan = models.IntegerField(primary_key=True)
    nama_ikan = models.CharField(max_length=20)

    def __str__(self):
        return self.nama_ikan

class Hasil_laut(models.Model):
    id_hasil = models.AutoField(primary_key=True)
    ikan = models.OneToOneField(Jenisikan, on_delete=models.CASCADE)
    ukuran = models.CharField(max_length=20)
    harga = models.DecimalField(..., max_digits=10, decimal_places=3)
    status = models.CharField(max_length=10)
    min_order = models.DecimalField(..., max_digits=5, decimal_places=2)
    stock = models.DecimalField(..., max_digits=5, decimal_places=2)
    photo = models.ImageField(default='default.jpg', upload_to='hasil')

    def __str__(self):
        return self.ikan
