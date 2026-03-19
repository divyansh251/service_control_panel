from django.urls import path
from . import views

urlpatterns = [
    path('', views.auth_view, name='auth'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]