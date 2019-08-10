from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('nelayan',views.datanelayan, name='datanelayan'),
    path('hasil_laut',views.hasillaut, name='hasillaut'),
]
