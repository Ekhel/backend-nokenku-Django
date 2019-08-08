from django.contrib import admin
from .models import Provinsi, Kabupaten, Nelayan, Jenisikan, Hasil_laut, Rekening

class PageProvinsi(admin.ModelAdmin):
    list_display = ('id','kode_provinsi','nama_provinsi')
    list_display_links = ('id','kode_provinsi','nama_provinsi')
    search_fields = ('kode_provinsi','nama_provinsi')
    list_per_page = 5

class PageKabupaten(admin.ModelAdmin):
    list_display = ('id','provinsi','kode_kabupaten','nama_kabupaten')
    list_display_links = ('id','provinsi','kode_kabupaten','nama_kabupaten')
    search_fields = ('kode_kabupaten','nama_kabupaten')
    list_per_page = 5

class PageNelayan(admin.ModelAdmin):
    list_display = ('id_nelayan','nama_nelayan','provinsi','kabupaten','no_kontak')
    list_display_links = ('id_nelayan','nama_nelayan','provinsi','kabupaten','no_kontak')
    search_fields = ('id_nelayan','nama_nelayan','provinsi','kabupaten','no_kontak')
    list_per_page = 10

class PageIkan(admin.ModelAdmin):
    list_display = ('id_ikan','nama_ikan')
    list_display_links = ('id_ikan','nama_ikan')
    search_fields = ('id_ikan','nama_ikan')
    list_per_page = 5


class PageHasil(admin.ModelAdmin):
    list_display = ('id_hasil','ikan','stock','min_order','harga','status')
    list_display_links = ('id_hasil','ikan','stock','min_order','harga','status')
    search_fields = ('id_hasil','ikan','stock','min_order','harga','status')
    list_per_page = 10

class PageRekening(admin.ModelAdmin):
    list_display = ('id_rekening','nama_bank','nama_rek','nomor_rek')
    list_display_links = ('id_rekening','nama_bank','nama_rek','nomor_rek')
    search_fields = ('id_rekening','nama_bank','nama_rek','nomor_rek')
    list_per_page = 5

admin.site.register(Provinsi, PageProvinsi)
admin.site.register(Kabupaten, PageKabupaten)
admin.site.register(Nelayan, PageNelayan)
admin.site.register(Jenisikan, PageIkan)
admin.site.register(Hasil_laut, PageHasil)
admin.site.register(Rekening, PageRekening)
