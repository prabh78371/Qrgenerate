from django.urls import path
from . import views
urlpatterns = [
    path('',views.qr_code,name='Qrcode'),
    
]
