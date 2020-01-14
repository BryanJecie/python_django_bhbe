from django.urls import path, include
from . import views


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    # path('login', views.login, name='login'),
    path('register/', views.register, name='register')
]