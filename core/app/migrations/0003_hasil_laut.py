# Generated by Django 2.2.4 on 2019-08-08 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_jenisikan_nelayan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hasil_laut',
            fields=[
                ('id_hasil', models.AutoField(primary_key=True, serialize=False)),
                ('ukuran', models.CharField(max_length=20)),
                ('harga', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(max_length=10)),
                ('min_order', models.DecimalField(decimal_places=2, max_digits=5)),
                ('stock', models.DecimalField(decimal_places=2, max_digits=5)),
                ('photo', models.ImageField(default='default.jpg', upload_to='hasil')),
                ('ikan', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Jenisikan')),
            ],
        ),
    ]