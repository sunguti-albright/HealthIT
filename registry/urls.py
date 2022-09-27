from django.urls import path as url
from . import views
from django.urls import re_path, path , include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView 
from .models import *

urlpatterns = [
    path('myprofile/',profile,name ='profile'),
    path('' , home , name='home'),
    path('search/',search_results, name ='search_results'),
    path('delete/<int:pk>',delete_project, name = 'deletepost'), 
    path('update/<str:pk>',update_project, name = 'updatepost'), 
    re_path(r'^api/profile/$', views.ProfileList.as_view()),
    re_path(r'^api/report/$', views.ReportList.as_view()),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)