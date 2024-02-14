from django.contrib import admin
from django.urls import path
from . import views

app_name = 'SylhetJobs'
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.syljobs,name='syljobs'),
    path('cumillajobs/', views.cumillajobs,name='cumillajobs'),
]
