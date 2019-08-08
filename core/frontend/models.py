from django.db import models
from app.models import Rekening, Hasil_laut

class order(models.Model):
    id_order = models.AutoField(primary_key=True)
    id_produk = models.OneToOneField(Hasil_laut, on_delete=models.CASCADE)
    nama_produk = models.CharField(max_length=150)
    qty = models.DecimalField(max_digits=10, decimal_places=2)
    tanggal = models.DateTimeField()
    id_username = models.IntegerField()
    username = models.CharField(max_length=150)
    alamat = models.CharField(max_length=250)
    metode_pembayaran = models.CharField(max_length=20)
    id_rekening = models.OneToOneField(Rekening, on_delete=models.CASCADE)
