from django.contrib.auth.views import LogoutView
from django.urls import path, include
from UniversityApp.accounts import views

urlpatterns = [
    path('', include([
        path('register/', views.UserRegisterPage.as_view(), name='register'),
        path('login/', views.LoginView.as_view(), name='login'),
        path('logout/', LogoutView.as_view(), name='logout'),
    ])),
    path('profile/<int:pk>/', include([
        path('details/', views.ProfileDetailsPage.as_view(), name='profile-details'),
        path('edit/', views.ProfileCreateOrEditPage.as_view(), name='profile-edit'),
        path('delete/', views.ProfileDeletePage.as_view(), name='profile-delete'),
    ])),
]
