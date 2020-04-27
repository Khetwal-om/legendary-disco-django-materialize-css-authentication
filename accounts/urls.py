from django.urls import path
from .views import home,login_user,register_user,logout_user

app_name='accounts'

urlpatterns=[
    path('',home,name='home'),
    path('login/',login_user,name='login'),
    path('register/',register_user,name='register'),
    path('logout/',logout_user,name='logout'),
]