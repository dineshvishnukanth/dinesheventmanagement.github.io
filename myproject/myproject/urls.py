from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('firstapp.urls')),
    path('demo',views.demofunction,name="demo"),
    path('main/',views.mainpage,name="main"),
  

]
