from django.urls import path, include
from UniversityApp.accounts import views

urlpatterns = [
    path('', include([
        path('register/', views.UserRegisterPage.as_view(), name='register'),
        path('login/', views.LoginView.as_view(), name='login'),
    ])),
    path('profile/<int:pk>/', include([
        path('details/', views.ProfileDetailsPage.as_view(), name='profile-details'),
        path('edit/', views.ProfileEditPage.as_view(), name='profile-edit'),
    ])),
]
