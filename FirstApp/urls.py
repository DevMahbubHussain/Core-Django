from django.contrib import admin
from django.urls import path
from . import views

app_name = 'FirstApp'
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('hello/', views.welcome,name='hello'),
    path('msg/', views.msg,name='msg'),
]