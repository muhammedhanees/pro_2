from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('test',views.testfun,name='test'),
    path('',views.loginfun,name='login'),
    path('profile',views.profilefun,name='profile'),
]