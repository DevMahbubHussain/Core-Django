from django.contrib import admin
from django.urls import path
from . import views

app_name = 'SylhetJobs'
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.syljobs,name='syljobs'),
    path('about-us/', views.about,name='about-us'),
    path('cumillajobs/', views.cumillajobs,name='cumillajobs'),
    path('drinks/<str:dish>',views.menuitems)
]
