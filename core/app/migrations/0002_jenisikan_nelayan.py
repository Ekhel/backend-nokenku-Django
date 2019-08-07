# Generated by Django 2.2.4 on 2019-08-07 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jenisikan',
            fields=[
                ('id_ikan', models.IntegerField(primary_key=True, serialize=False)),
                ('nama_ikan', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Nelayan',
            fields=[
                ('id_nelayan', models.IntegerField(primary_key=True, serialize=False)),
                ('nama_nelayan', models.CharField(max_length=150)),
                ('armada', models.CharField(max_length=10)),
                ('tanggal_lahir', models.DateField()),
                ('no_kontak', models.CharField(max_length=15)),
                ('kabupaten', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Kabupaten')),
                ('provinsi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Provinsi')),
            ],
        ),
    ]