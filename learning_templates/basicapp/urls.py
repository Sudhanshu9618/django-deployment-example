from django.urls import path, include
# from django.conf.urls import include
from basicapp import views

app_name = 'basicapp'

urlpatterns = [
    path('urls/', views.url, name='url'),
    path('other/', views.other, name='other'),


]
