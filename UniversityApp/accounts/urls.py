from django.urls import path
from UniversityApp.accounts import views

urlpatterns = [
    path('register/', views.UserRegisterPage.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
]
